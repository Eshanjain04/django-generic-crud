# Generated by Django 4.2.6 on 2023-12-10 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0006_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Battery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField()),
                ('name', models.CharField()),
                ('max_volt', models.IntegerField()),
            ],
        ),
    ]