from django.db import models

class MediaFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    converted_file = models.FileField(upload_to='uploads/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
