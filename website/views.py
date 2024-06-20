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
            media_file = MediaFile(file=request.FILES['file'], output_format=form.cleaned_data['output_format'])
            media_file.save()

            # Retrieve the selected bitrate from the form data
            bitrate = form.cleaned_data['bitrate']
            converted_file_path = convert_media(media_file.file.path, media_file.output_format, bitrate)

            if converted_file_path:
                media_file.converted_file = converted_file_path
                media_file.save()
                return redirect('result', media_file_id=media_file.id)
    else:
        form = UploadFileForm()
    return render(request, 'website/upload.html', {'form': form})


def result(request, media_file_id):
    media_file = MediaFile.objects.get(id=media_file_id)
    return render(request, 'website/result.html', {'media_file': media_file})
