# Generated by Django 3.1.6 on 2021-02-08 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_topic_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='image',
            field=models.ImageField(default='d.jpg', null=True, upload_to='images/'),
        ),
    ]
