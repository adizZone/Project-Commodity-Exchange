# Generated by Django 5.0.3 on 2024-04-05 20:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0022_remove_deal_grievance_count_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razorpay_order_id', models.CharField(blank=True, max_length=100)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100)),
                ('razorpay_signature', models.CharField(blank=True, max_length=100)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('paid', models.BooleanField(default=False)),
                ('for_grievance', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='community.grievance')),
            ],
        ),
    ]
