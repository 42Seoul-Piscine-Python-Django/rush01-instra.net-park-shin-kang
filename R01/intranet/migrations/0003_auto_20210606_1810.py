# Generated by Django 2.2.24 on 2021-06-06 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intranet', '0002_comment_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='writter',
        ),
    ]