# Generated by Django 3.2.15 on 2022-08-25 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_cartlist_cart_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='active',
            field=models.BooleanField(default='True'),
        ),
    ]