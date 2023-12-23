from generic_api.model_handler import BaseModel
from django.db import models


# Create your models here.
class Make(BaseModel):
    name = models.CharField()
    display_name = models.CharField()

    @property
    def validation_schema(self):
        return {
            "name": {
                "type": "string",
                "required": True,
                "maxlength": 200
            },
            "display_name": {
                "type": "string",
                "maxlength": 200
            }
        }


class Model(BaseModel):
    type = models.CharField()
    name = models.CharField()
    number = models.IntegerField()

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
            "number": {
                "type": "int",
                "maxlength": 200
            }
        }


class Battery(BaseModel):
    type = models.CharField()
    name = models.CharField()
    max_volt = models.IntegerField()

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
            "max_volt": {
                "type": "integer",
                "maxlength": 200
            }
        }


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


class ModelData(BaseModel):  # it stores model configurations for which we are going to open crud.
    model_key = models.CharField(unique=True)
    app_name = models.CharField()
    model_name = models.CharField()
    public = models.BooleanField(default=False)
    foreign_key_app_name = models.CharField(default='vehicle')
    foreign_key_model_name = models.CharField(default='user')
