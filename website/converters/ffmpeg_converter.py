import ffmpeg
import os
from django.conf import settings

def convert_media(input_file_path, output_format):
    base_dir = os.path.dirname(input_file_path)
    output_file_name = f"{os.path.splitext(os.path.basename(input_file_path))[0]}.{output_format}"
    output_file_path = os.path.join(base_dir, output_file_name)
    try:
        ffmpeg.input(input_file_path).output(output_file_path).run(overwrite_output=True)
        return os.path.relpath(output_file_path, settings.MEDIA_ROOT)
    except ffmpeg.Error as e:
        print(f"FFmpeg error: {e}")
        return None
