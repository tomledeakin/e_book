# Generated by Django 4.2.6 on 2023-11-20 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
    ]
