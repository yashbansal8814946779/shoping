# Generated by Django 4.0 on 2023-01-22 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='contact_no',
            field=models.CharField(max_length=250),
        ),
    ]