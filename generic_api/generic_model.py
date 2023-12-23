from django.db import models
from django.core.serializers import serialize


class BaseModel(models.Model):
    class Meta:
        abstract = True

    def to_json(self):
        return serialize('python', [self])[0]
