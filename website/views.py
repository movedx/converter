from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import MediaFile
from .converters.ffmpeg_converter import convert_media
from django.contrib import messages


def upload_file(request: HttpRequest):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('file')
            converted_media_ids = []
            try:
                for file in files:
                    media_file = MediaFile(file=file, output_format=form.cleaned_data['output_format'])
                    media_file.save()
                
                    bitrate = form.cleaned_data['bitrate']
                    converted_file_path = convert_media(media_file.file.path, media_file.output_format, bitrate)

                    if converted_file_path:
                        media_file.converted_file = converted_file_path
                        media_file.save()
                        converted_media_ids.append(media_file.id)
            except Exception as e:
                messages.error(request, f"Error processing file {file.name}: {str(e)}")

            return redirect('result', media_file_ids=','.join(map(str, converted_media_ids)))
    else:
        form = UploadFileForm()
    return render(request, 'website/upload.html', {'form': form})


def result(request: HttpRequest, media_file_ids):
    media_file_ids_list = list(map(int, media_file_ids.split(',')))
    media_files = []
    for id in media_file_ids_list:
        media_files.append(MediaFile.objects.get(id=id))

    return render(request, 'website/result.html', {'media_files': media_files})


def test_response(request: HttpRequest):
    return HttpResponseRedirect('/')