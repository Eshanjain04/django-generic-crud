"""
URL configuration for bulk_upload project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from bulk_upload.bulk_upload_api import make_bulk_upload
from generic_api.create import generic_create, generic_get_obj, generic_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('make-bulk-upload/', make_bulk_upload),

    # Generic APIs
    path('generic/<str:model_key>/add/', generic_create),
    path('generic/<str:model_key>/list/', generic_list),
    path('generic/<str:model_key>/get/<int:object_id>/', generic_get_obj),
]
