# Generated by Django 3.1.6 on 2021-02-07 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210207_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='app.profile'),
        ),
    ]