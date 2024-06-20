from django import forms
from .models import MediaFile

class UploadFileForm(forms.ModelForm):
    output_format = forms.ChoiceField(choices=[('mp3', 'MP3'), ('wav', 'WAV'), ('mp4', 'MP4')])

    class Meta:
        model = MediaFile
        fields = ['file', 'output_format']
