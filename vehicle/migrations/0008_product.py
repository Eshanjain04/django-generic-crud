# Generated by Django 4.2.6 on 2023-12-10 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0007_battery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField()),
                ('name', models.CharField()),
                ('description', models.CharField()),
            ],
        ),
    ]