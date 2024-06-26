# Generated by Django 5.0.6 on 2024-06-20 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_mediafile_converted_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mediafile',
            name='uploaded_at',
        ),
        migrations.AddField(
            model_name='mediafile',
            name='output_format',
            field=models.CharField(default='mp4', max_length=10),
        ),
        migrations.AlterField(
            model_name='mediafile',
            name='converted_file',
            field=models.FileField(blank=True, null=True, upload_to='converted/'),
        ),
    ]
