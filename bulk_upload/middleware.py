from django.apps import apps
from generic_api.utility.verfiy_token import verify_token
from generic_api.utility.response_handler import ResponseHandler
from vehicle.models import ModelData


def get_model(app_name, model_name):
    return apps.get_model(app_label=app_name, model_name=model_name)


def verify_login(function):
    def wrap(request, *args, **kwargs):
        model_key = kwargs.get('model_key')
        model_data = ModelData.objects.filter(model_key=model_key).first()
        if not model_data:
            return ResponseHandler(body="Model with key does not exists").error_response()
        kwargs['model_data'] = model_data
        is_authorized, msg = True, None
        if not getattr(model_data, 'public'):
            is_authorized, msg = verify_token(request=request)
        if not is_authorized:
            return ResponseHandler(body=msg).error_response()
        model = get_model(app_name=getattr(model_data, 'app_name'), model_name=getattr(model_data, 'model_name'))
        if not model:
            return ResponseHandler(body="Model doesnot exists in database").error_response()
        kwargs['model'] = model
        if getattr(model_data, 'foreign_key_app_name') and getattr(model_data, 'foreign_key_model_name'):
            kwargs['relational_model'] = get_model(app_name=getattr(model_data, 'foreign_key_app_name'),
                                                   model_name=getattr(model_data, 'foreign_key_model_name'))
        return function(request, *args, **kwargs)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
