from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import MediaFile
from .converters.ffmpeg_converter import convert_media

from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import MediaFile
from .converters.ffmpeg_converter import convert_media

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            media_file = form.save()
            output_format = form.cleaned_data['output_format']
            converted_file_path = convert_media(media_file.file.path, output_format)
            if converted_file_path:
                # Set the relative path to the converted_file field
                media_file.converted_file.name = converted_file_path
                media_file.save()
                return redirect('result', file_id=media_file.id)
    else:
        form = UploadFileForm()
    return render(request, 'website/upload.html', {'form': form})

def result(request, file_id):
    media_file = MediaFile.objects.get(id=file_id)
    return render(request, 'website/result.html', {'media_file': media_file})


def result(request, file_id):
    media_file = MediaFile.objects.get(id=file_id)
    print(media_file.converted_file.path)
    print(media_file.converted_file.url)
    return render(request, 'website/result.html', {'media_file': media_file})
