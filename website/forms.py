from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Select a file')
    format_choices = [
        ('mp4', 'MP4'),
        ('mp3', 'MP3'),
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