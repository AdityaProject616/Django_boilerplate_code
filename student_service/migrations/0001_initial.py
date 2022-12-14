# Generated by Django 4.1.3 on 2022-11-22 18:11

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('firstname', models.CharField(max_length=200, null=True)),
                ('lastname', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=200)),
                ('registration_id', models.CharField(max_length=11, null=True, unique=True)),
                ('roll_no', models.IntegerField(null=True, unique=True)),
                ('contact_no', models.BigIntegerField(null=True, unique=True)),
                ('branch', models.CharField(choices=[('Computer', 'Computer'), ('Information Technology', 'Information Technology'), ('Electronics and Telecommunication', 'Electronics and Telecommunication')], max_length=200)),
                ('ssc_score', models.FloatField(default=1, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('hsc_score', models.FloatField(default=0, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('diploma_score', models.FloatField(default=0, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('CGPA', models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('active_backlog_count', models.IntegerField(default=0)),
                ('passive_backlog_count', models.IntegerField(default=0)),
            ],
        ),
    ]
