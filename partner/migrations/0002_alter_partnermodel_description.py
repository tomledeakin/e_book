# Generated by Django 4.2.5 on 2023-11-15 01:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partnermodel',
            name='description',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]