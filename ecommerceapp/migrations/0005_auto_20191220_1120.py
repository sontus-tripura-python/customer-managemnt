# Generated by Django 3.0.1 on 2019-12-20 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0004_customer_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(blank=True),
        ),
    ]
