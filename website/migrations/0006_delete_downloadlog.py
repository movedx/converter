# Generated by Django 5.0.6 on 2024-07-07 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_downloadlog'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DownloadLog',
        ),
    ]