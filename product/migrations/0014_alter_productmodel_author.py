# Generated by Django 4.2.6 on 2023-11-20 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
        ('product', '0013_remove_productmodel_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='author.authormodel'),
        ),
    ]
