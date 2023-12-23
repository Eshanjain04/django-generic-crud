from rest_framework.decorators import api_view
from bulk_upload.middleware import verify_login
from generic_api.utility.get_model_obj import ModelDataHandler
from generic_api.utility.response_handler import ResponseHandler
from generic_api.utility.validate_user_input import validate_data


# class DynamicSerializer(serializers.ModelSerializer):
#
#     def __init__(self, model_obj, *args, **kwargs):
#         self.model_obj = model_obj
#         super().__init__(*args, **kwargs)
#
#         self.Meta.model = model_obj
#
#         for field_name in model_obj._meta.fields:
#             self.fields[field_name.name] = serializers.CharField()
#
#     class Meta:
#         fields = '__all__'


@api_view(['POST'])
@verify_login
def generic_create(request, *args, **kwargs):
    data = request.data
    model_data = kwargs.get('model_data')
    model = kwargs.get('model')

    validation_schema = getattr(model(), 'validation_schema')
    is_valid, errors = validate_data(data_schema=validation_schema, data=data)
    if not is_valid:
        return ResponseHandler(body=f'{errors}').error_response()
    if not ModelDataHandler(model=model, data=data).create_model_object():
        return ResponseHandler(
            body=f'Some error occured while adding data for {model_data.model_key}').error_response()
    return ResponseHandler(body=f'{model_data.model_key} data added successfully').success_response()


@api_view(['GET'])
@verify_login
def generic_get_obj(request, *args, **kwargs):
    object_id = kwargs.get('object_id')
    model_data = kwargs.get('model_data')
    model = kwargs.get('model')
    obj = ModelDataHandler(model=model, object_id=object_id).get_model_obj()
    if not obj:
        return ResponseHandler(
            body=f'object for {model_data.model_key} with given id does not exists').error_response()
    json_data = obj.to_json()['fields']
    return ResponseHandler(body=json_data).success_response()


@api_view(['GET'])
@verify_login
def generic_list(request, *args, **kwargs):
    model = kwargs.get('model')
    model_obj = model.objects.all()
    response_array = []
    for item in model_obj:
        response_array.append(item.to_json()['fields'])
    return ResponseHandler(body=response_array).success_response()


@api_view(['DELETE'])
@verify_login
def generic_delete_obj(request, *args, **kwargs):
    object_id = kwargs.get('object_id')
    model_data = kwargs.get('model_data')
    model = kwargs.get('model')
    obj = ModelDataHandler(model=model, object_id=object_id).delete_model_object()
    if not obj:
        return ResponseHandler(
            body=f'object for {model_data.model_key} with given id does not exists').error_response()
    return ResponseHandler(body=f'{model_data.model_key} data deleted Successfully').success_response()


@api_view(['PUT'])
@verify_login
def generic_update_obj(request, *args, **kwargs):
    data = request.data
    object_id = kwargs.get('object_id')
    model_data = kwargs.get('model_data')
    model = kwargs.get('model')
    validation_schema = getattr(model(), 'validation_schema')
    is_valid, errors = validate_data(data_schema=validation_schema, data=data)
    if not is_valid:
        return ResponseHandler(body=f'{errors}').error_response()

    obj = ModelDataHandler(model=model, object_id=object_id, data=data).update_model_object()
    if not obj:
        return ResponseHandler(
            body=f'object for {model_data.model_key} with given id does not exists').error_response()
    return ResponseHandler(body=f'{model_data.model_key} data updated Successfully').success_response()
