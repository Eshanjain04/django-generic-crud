from django.contrib import admin

from vehicle.models import Make, ExcelData

# Register your models here.
admin.site.register(Make)
admin.site.register(ExcelData)
