# Generated by Django 4.2.2 on 2023-06-28 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_vehicledetail_pickup_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicledetail',
            name='status',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
