from django import forms

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class UploadFileForm(forms.Form):
    file = MultipleFileField(label='Select a file')
    format_choices = [
        ('mp3', 'MP3'),
        ('mp4', 'MP4'),
        # Add more formats if needed
    ]
    output_format = forms.ChoiceField(choices=format_choices, label='Output Format')
    
    # Add bitrate field
    bitrate_choices = [
        ('128k', '128 kbps'),
        ('192k', '192 kbps'),
        ('256k', '256 kbps'),
        ('320k', '320 kbps'),
    ]
    bitrate = forms.ChoiceField(choices=bitrate_choices, label='Bitrate', required=False)