from rest_framework.decorators import api_view
from rest_framework.response import Response

from bulk_upload.bulk_upload import bulk_upload


@api_view(['POST'])
def make_bulk_upload(request, *args, **kwargs):
    name = request.POST.get('name')
    excel_file = request.FILES.get('file')
    is_valid, errors = bulk_upload(name, excel_file)
    if is_valid:
        return Response({"message": "Data uploaded successfully."}, status=200)
    else:
        return Response({"message": "Validation errors", "errors": errors}, status=422)
