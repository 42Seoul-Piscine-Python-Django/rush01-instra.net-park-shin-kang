# Generated by Django 2.2.24 on 2021-06-06 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intranet', '0005_recomment_writter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['-last_updated']},
        ),
    ]