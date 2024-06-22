import ffmpeg
import os
from django.conf import settings

def convert_media(input_file_path, output_format, bitrate=None):
    base_dir = os.path.dirname(input_file_path)
    output_file_name = f"{input_file_path}_converted.{output_format}"
    output_file_path = os.path.join(base_dir, output_file_name)

    try:
        # Prepare the ffmpeg command with bitrate if specified and format is mp3
        ffmpeg_cmd = ffmpeg.input(input_file_path)
        if output_format == 'mp3' and bitrate:
            ffmpeg_cmd = ffmpeg_cmd.output(output_file_path, audio_bitrate=bitrate)
        else:
            ffmpeg_cmd = ffmpeg_cmd.output(output_file_path)

        # Run the ffmpeg command and convert the file
        ffmpeg_cmd.run(overwrite_output=True)
        return os.path.relpath(output_file_path, settings.MEDIA_ROOT)
    except ffmpeg.Error as e:
        print(f"FFmpeg error: {e}")
        return None