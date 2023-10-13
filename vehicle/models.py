from django.db import models


# Create your models here.
class Make(models.Model):
    name = models.CharField()
    display_name = models.CharField()
