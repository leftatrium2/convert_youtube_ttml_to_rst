import hashlib

import yt_dlp

from convert_youtube_ttml_to_srt.convert_subtitle_ttml_to_srt import convert_subtitle_ttml_to_srt

G_SUBTITLE_FILE_PATH = None


def progress_hook(d):
    global G_SUBTITLE_FILE_PATH
    if d['status'] == 'finished':
        G_SUBTITLE_FILE_PATH = d['filename']


def url_md5(url):
    hash_object = hashlib.md5(url.encode())
    hash_hex = hash_object.hexdigest()
    return hash_hex


if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=jE4V73Y0YH0"
    ydl_opts_subtitles = {
        'progress_hooks': [progress_hook],
        'outtmpl': f'st_{url_md5(url)}.%(ext)s',
        # 'writesubtitles': True,  # download subtitle by user
        'writeautomaticsub': True,  # download subtitle by google machine
        'subtitlesformat': 'ttml',
        'skip_download': True,  # skip download
        'noplaylist': True
    }
    ydl_opts_subtitle_list = {
        'simulate': True,
        'listsubtitles': True,
        'skip_download': True,  # skip download
        'noplaylist': True
    }
    with yt_dlp.YoutubeDL(ydl_opts_subtitles) as ydl_subtitles:
        with yt_dlp.YoutubeDL(ydl_opts_subtitle_list) as ydl_subtitle_list:
            info = ydl_subtitle_list.extract_info(url)
            subtitleslangs = []
            automatic_captions = info['automatic_captions']
            for key in automatic_captions.keys():
                if 'en' in key:
                    subtitleslangs.append(key)
                    break
            ydl_subtitles.params['subtitleslangs'] = subtitleslangs
            ydl_subtitles.download(url)
            if G_SUBTITLE_FILE_PATH:
                convert_rst_file_path = G_SUBTITLE_FILE_PATH.replace('ttml', 'srt')
                convert_subtitle_ttml_to_srt(G_SUBTITLE_FILE_PATH, convert_rst_file_path, True)
