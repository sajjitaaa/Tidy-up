# Generated by Django 3.0.8 on 2021-03-08 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_variation_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='category',
            field=models.CharField(choices=[('size', 'size'), ('package', 'package')], default='size', max_length=120),
        ),
    ]
