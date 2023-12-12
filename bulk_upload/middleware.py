from django.apps import apps
from rest_framework.response import Response

from bulk_upload.verfiy_token import verify_token
from vehicle.models import ModelData


def response_handler(status, msg):
    return Response({"message": f'{msg}'}, status=status)


def get_model(app_name, model_name):
    return apps.get_model(app_label=app_name, model_name=model_name)


def verify_login(function):
    def wrap(request, *args, **kwargs):
        model_key = kwargs.get('model_key')
        model_data = ModelData.objects.filter(model_key=model_key).first()
        if not model_data:
            return response_handler(422, "Model with key does not exists")
        kwargs['model_data'] = model_data
        is_authorized, msg = None, None
        if not getattr(model_data, 'public'):
            is_authorized, msg = verify_token(request=request)
        if is_authorized == False:
            return Response({"message": msg}, status=422)
        model = get_model(app_name=getattr(model_data, 'app_name'), model_name=getattr(model_data, 'model_name'))
        if not model:
            return Response({"message": "Model doesnot exists in database"}, status=422)
        kwargs['model'] = model
        if getattr(model_data, 'foreign_key_app_name') and getattr(model_data, 'foreign_key_model_name'):
            kwargs['relational_model'] = get_model(app_name=getattr(model_data, 'foreign_key_app_name'),
                                                   model_name=getattr(model_data, 'foreign_key_model_name'))
        return function(request, *args, **kwargs)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
