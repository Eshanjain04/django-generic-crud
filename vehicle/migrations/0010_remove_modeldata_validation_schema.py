# Generated by Django 4.2.6 on 2023-12-23 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0009_user_modeldata_foreign_key_app_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modeldata',
            name='validation_schema',
        ),
    ]