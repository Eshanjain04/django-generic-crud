# Generated by Django 4.2.6 on 2023-10-13 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(unique=True)),
                ('app_name', models.CharField()),
                ('model_name', models.CharField()),
                ('structure', models.JSONField()),
                ('multiple_table_upload', models.BooleanField(default=False)),
            ],
        ),
    ]
