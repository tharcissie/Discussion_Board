# Generated by Django 3.1.6 on 2021-02-07 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210207_1516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='Author',
            new_name='author',
        ),
    ]
