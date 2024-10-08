# Generated by Django 5.0.3 on 2024-04-04 14:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0014_alter_otpverification_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatbox',
            name='timeStamp',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='deal',
            name='timeStamp',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='demand',
            name='timeStamp',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='timeStamp',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='offering',
            name='timeStamp',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
