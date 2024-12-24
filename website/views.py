import mimetypes
import os
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import MediaFile
from .converters.ffmpeg_converter import convert_media
from django.contrib import messages
from urllib.parse import quote

import logging

logger = logging.getLogger(__name__)

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
                    else:
                        logger.error(f"Conversion failed for file: {file.name}")
            except Exception as e:
                logger.error(f"Error processing file {file.name}: {str(e)}")
                messages.error(request, f"Error processing file {file.name}: {str(e)}")

            if converted_media_ids:
                return redirect('result', media_file_ids=','.join(map(str, converted_media_ids)))
            else:
                messages.error(request, "No files were successfully converted.")
                return redirect('upload_file')
    else:
        form = UploadFileForm()
    return render(request, 'website/upload.html', {'form': form})


def result(request: HttpRequest, media_file_ids):
    media_file_ids_list = list(map(int, media_file_ids.split(',')))
    media_files = []
    for id in media_file_ids_list:
        media_files.append(MediaFile.objects.get(id=id))

    return render(request, 'website/result.html', {'media_files': media_files})


def download_file(request, media_file_id):
    try:
        media_file = MediaFile.objects.get(id=media_file_id)
        file_path = media_file.converted_file.path
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_path)[0])
                response['Content-Disposition'] = f'attachment; filename={quote(media_file.converted_file.name)}'
                # Log the download event
                log_download_event(request, media_file)

                # Get the paths for both the uploaded and converted files
                uploaded_file_path = media_file.file.path
                converted_file_path = media_file.converted_file.path

                # Close the file handle
                fh.close()

                # Delete the files
                if os.path.exists(uploaded_file_path):
                    os.remove(uploaded_file_path)
                if os.path.exists(converted_file_path):
                    os.remove(converted_file_path)

                media_file.delete()  # Delete the database record

                return response
        else:
            raise Http404("File not found")
    except MediaFile.DoesNotExist:
        raise Http404("File not found")

def log_download_event(request, media_file):
    print(f"User {request.user} downloaded the file {media_file.converted_file.name}")


def test_response(request: HttpRequest):
    return HttpResponseRedirect('/')