# Generated by Django 4.0.4 on 2022-05-25 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_stock_product_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='product_receive_quantity',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
    ]