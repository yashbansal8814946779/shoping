# Generated by Django 4.0 on 2023-01-27 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_order12'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order12',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='order12',
            old_name='last_name',
            new_name='lastname',
        ),
    ]
