from django.db import models


# Create your models here.
class Make(models.Model):
    name = models.CharField()
    display_name = models.CharField()


class ExcelData(models.Model):
    name = models.CharField(unique=True)
    app_name = models.CharField()
    model_name = models.CharField()
    structure = models.JSONField()
    multiple_table_upload = models.BooleanField(default=False)

