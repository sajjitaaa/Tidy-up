# Generated by Django 3.0.8 on 2021-04-15 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20210415_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(choices=[('Boys Summer', 'boys summer'), ('Boys Winter', 'boys winter'), ('girls Summer', 'girls summer'), ('Girls Winter', 'girls summer'), ('Kindergarten', 'kindergarten')], max_length=120),
        ),
    ]
