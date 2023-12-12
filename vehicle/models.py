from bulk_upload.generic_model import BaseModel
from django.db import models

sample_validation_schema = {
    "type": {
        "type": "string",
        "required": True,
        "maxlength": 200
    },
    "name": {
        "type": "string",
        "required": True,
        "maxlength": 200
    },
    "number": {
        "type": "int",
        "required": True,
        "maxlength": 200
    }
}


# Create your models here.
class Make(BaseModel):
    name = models.CharField()
    display_name = models.CharField()


class Model(BaseModel):
    type = models.CharField()
    name = models.CharField()
    number = models.IntegerField()


class Battery(BaseModel):
    type = models.CharField()
    name = models.CharField()
    max_volt = models.IntegerField()


class Product(BaseModel):
    type = models.CharField()
    name = models.CharField()
    description = models.CharField()

    @property
    def validation_schema(self):
        return {
            "type": {
                "type": "string",
                "required": True,
                "maxlength": 200
            },
            "name": {
                "type": "string",
                "required": True,
                "maxlength": 200
            },
            "description": {
                "type": "string",
                "maxlength": 200
            }
        }


class User(BaseModel):
    name = models.CharField()
    username = models.CharField()
    password = models.CharField()


class ExcelData(BaseModel):
    name = models.CharField(unique=True)
    app_name = models.CharField()
    model_name = models.CharField()
    structure = models.JSONField()
    multiple_table_upload = models.BooleanField(default=False)


class ModelData(BaseModel):
    model_key = models.CharField(unique=True)
    app_name = models.CharField()
    model_name = models.CharField()
    public = models.BooleanField(default=False)
    foreign_key_app_name = models.CharField(default='vehicle')
    foreign_key_model_name = models.CharField(default='user')
