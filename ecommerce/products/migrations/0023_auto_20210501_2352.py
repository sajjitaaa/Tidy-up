# Generated by Django 3.0.8 on 2021-05-01 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_school_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='product',
        ),
        migrations.AddField(
            model_name='school',
            name='product',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]
