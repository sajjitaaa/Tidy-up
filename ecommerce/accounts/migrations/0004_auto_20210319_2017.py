# Generated by Django 3.0.8 on 2021-03-19 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_emailconfirmed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailconfirmed',
            old_name='hashkey',
            new_name='activation_key',
        ),
    ]
