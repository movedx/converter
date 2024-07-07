from django.contrib import admin
from .models import MediaFile


@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    pass