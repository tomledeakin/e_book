# Generated by Django 4.2.6 on 2023-12-04 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_productmodel_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='image_promotion',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
