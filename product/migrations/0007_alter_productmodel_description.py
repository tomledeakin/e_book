# Generated by Django 4.2.5 on 2023-11-05 15:36

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_productmodel_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='description',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
