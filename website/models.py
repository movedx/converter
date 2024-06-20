from django.db import models

class MediaFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    converted_file = models.FileField(upload_to='converted/', blank=True, null=True)
    output_format = models.CharField(max_length=10, default='mp4')  # Add this line to include output_format field

    def __str__(self):
        return self.file.name