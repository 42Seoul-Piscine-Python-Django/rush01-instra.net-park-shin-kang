# Generated by Django 3.2.3 on 2021-06-08 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intranet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
