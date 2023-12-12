from django.contrib import admin

from vehicle.models import Make, ExcelData, ModelData, Battery, Model, Product

# Register your models here.
admin.site.register(Make)
admin.site.register(ExcelData)
admin.site.register(ModelData)
admin.site.register(Model)
admin.site.register(Battery)
admin.site.register(Product)
