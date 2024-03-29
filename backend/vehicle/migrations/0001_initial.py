# Generated by Django 4.2.2 on 2023-06-22 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import vehicle.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mileage', models.FloatField()),
                ('brand_name', models.CharField(max_length=100)),
                ('model_name', models.CharField(max_length=100, null=True)),
                ('rate_per_hour', models.IntegerField()),
                ('free_kms', models.IntegerField(null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('vehicle_image', models.ImageField(null=True, upload_to=vehicle.models.uploads)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_creator', to=settings.AUTH_USER_MODEL)),
                ('vehicle_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.vehicletype')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_status', models.CharField(max_length=100)),
                ('from_time', models.DateTimeField()),
                ('to_time', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('booked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booked_user', to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.vehicledetail')),
            ],
        ),
    ]
