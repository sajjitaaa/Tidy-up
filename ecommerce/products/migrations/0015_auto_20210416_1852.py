# Generated by Django 3.0.8 on 2021-04-16 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20210416_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='products.Product'),
        ),
    ]
