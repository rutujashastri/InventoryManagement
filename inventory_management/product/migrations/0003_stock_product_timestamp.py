# Generated by Django 4.0.4 on 2022-05-23 16:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_stock_product_export_to_csv_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='product_timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
