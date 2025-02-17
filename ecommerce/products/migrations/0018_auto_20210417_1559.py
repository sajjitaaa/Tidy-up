# Generated by Django 3.0.8 on 2021-04-17 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20210417_1543'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Schools',
            new_name='School',
        ),
        migrations.AlterModelOptions(
            name='school',
            options={'verbose_name_plural': 'schools'},
        ),
        migrations.AlterUniqueTogether(
            name='school',
            unique_together={('slug', 'name')},
        ),
    ]
