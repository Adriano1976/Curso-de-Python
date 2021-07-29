import fnmatch
import os
import sys

if sys.platform == 'linux':
    command_ffmpeg = 'ffmpeg'
else:
    command_ffmpeg = r'ffmpeg\ffmpeg.exe'

codec_video = '-c:v libx264'
crf = '-crf 23'
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:10'
debug = ''

file_path = r'C:\Users\user\Videos\Vídeos de Neide'

for root, folders, files in os.walk(file_path):
    for file in files:
        if not fnmatch.fnmatch(file, '*.mp4'):
            continue

        full_path = os.path.join(root, file)
        file_name, file_extension = os.path.splitext(full_path)
        subtitle_path = file_name + '.srt'

        if os.path.isfile(subtitle_path):
            input_subtitle = f'-i "{subtitle_path}"'
            map_subtitle = '-c:s srt -map v:0 -map a -map 1:0'
        else:
            input_subtitle = ''
            map_subtitle = ''

        file_name, file_extension = os.path.splitext(file)

        new_file = file_name + ' - Cópia' + file_extension
        file_output = os.path.join(root, new_file)

        command = f'{command_ffmpeg} -i "{full_path}" {input_subtitle}' \
                  f'{codec_video} {crf} {preset} {codec_audio} {bitrate_audio}' \
                  f'{debug} {map_subtitle} "{file_output}"'

        os.system(command)
