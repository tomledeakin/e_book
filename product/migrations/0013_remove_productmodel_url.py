# Generated by Django 4.2.6 on 2023-11-20 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_productmodel_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='url',
        ),
    ]
