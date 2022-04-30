# Generated by Django 4.0.2 on 2022-04-07 16:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hostels', '0003_room_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='district',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=15, null=True, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
        migrations.AlterField(
            model_name='room',
            name='pin',
            field=models.IntegerField(blank=True, default=None, null=True, validators=[django.core.validators.MaxValueValidator(999999), django.core.validators.MinValueValidator(100000)]),
        ),
        migrations.AlterField(
            model_name='room',
            name='state',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='town',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_image', models.ImageField(upload_to='images/')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostels.room', verbose_name='Room')),
            ],
        ),
    ]
