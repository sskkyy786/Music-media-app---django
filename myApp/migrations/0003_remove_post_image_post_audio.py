# Generated by Django 5.0 on 2023-12-23 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='audio_files/'),
        ),
    ]
