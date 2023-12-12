import json

import cerberus
from django.core.serializers import serialize
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bulk_upload.middleware import verify_login
from rest_framework import serializers


class DynamicSerializer(serializers.ModelSerializer):

    def __init__(self, model_obj, *args, **kwargs):
        self.model_obj = model_obj
        super().__init__(*args, **kwargs)

        self.Meta.model = model_obj

        for field_name in model_obj._meta.fields:
            self.fields[field_name.name] = serializers.CharField()

    class Meta:
        fields = '__all__'


def validate_data(data_schema, data):
    validation_schema = cerberus.Validator(data_schema)
    is_valid = validation_schema.validate(data)
    if is_valid:
        return True, []
    else:
        validation_errors = validation_schema.errors
        return False, validation_errors


def response_handler(status, msg):
    return Response({"message": f'{msg}'}, status=status)


@api_view(['POST'])
@verify_login
def generic_create(request, *args, **kwargs):
    data = request.data
    model_data = kwargs.get('model_data')
    model = kwargs.get('model')

    validation_schema = getattr(model(), 'validation_schema')
    is_valid, errors = validate_data(data_schema=validation_schema, data=data)
    if not is_valid:
        return Response({"message": f'{errors}'}, status=422)
    model.objects.create(**data)
    return Response({"message": f'{model_data.model_key} data added successfully'}, status=200)


@api_view(['GET'])
@verify_login
def generic_get_obj(request, *args, **kwargs):
    object_id = kwargs.get('object_id')
    model_data = kwargs.get('model_data')
    model = kwargs.get('model')
    obj = model.objects.filter(pk=object_id).first()
    if not obj:
        return response_handler(200, f'object for {model_data.model_key} with given id does not exists')
    json_data = obj.to_json()
    return JsonResponse(json_data, safe=False)


@api_view(['GET'])
@verify_login
def generic_list(request, *args, **kwargs):
    model = kwargs.get('model')
    model_obj = model.objects.all()
    json_data = (serialize('python', model_obj))
    response_array = []
    for item in json_data:
        response_array.append(item.get('fields'))
    return JsonResponse(response_array, safe=False)
