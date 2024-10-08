# Generated by Django 5.0.3 on 2024-03-31 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_notification_deal_demand_grievance_offering_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='grievance',
            name='faulty_item_image',
            field=models.ImageField(blank=True, null=True, upload_to='grievances/images'),
        ),
        migrations.AlterField(
            model_name='demand',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='demands/images'),
        ),
        migrations.AlterField(
            model_name='offering',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='offerings/images'),
        ),
    ]
