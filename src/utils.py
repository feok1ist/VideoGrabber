import os
from pathlib import Path

import yt_dlp


def folder_for_result():
    base_dir = Path(__file__).parent.absolute()
    up_dir = base_dir.parent.absolute()
    folder = up_dir / "result"
    folder.mkdir(exist_ok=True)
    return folder


def move_to_result(filename):
    src = folder_for_tmp() / filename
    dst = folder_for_result() / filename
    if src.exists():
        src.rename(dst)
        return True
    return False


def find_downloaded_file(tmp_dir, ext):
    files = list(tmp_dir.glob(f"*.{ext}"))
    if not files:
        return None
    return max(files, key=os.path.getmtime).name


def folder_for_tmp():
    base_dir = Path(__file__).parent.absolute()
    up_dir = base_dir.parent.absolute()
    folder = up_dir / "tmp"
    folder.mkdir(exist_ok=True)
    return folder


def download_video(url, ydl_opts):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def generation_ydl_opts(file_path, format_file: str, quality: str, proxy: str):
    base = {"outtmpl": f"{str(file_path)}/%(title)s.%(ext)s", "proxy": proxy}

    formats = {
        "mp4": {
            "format_sort": ["vcodec:avc", f"res:{quality}", "acodec:aac"],
            "postprocessors": [{"key": "EmbedThumbnail", "already_have_thumbnail": False}],
            "writethumbnail": True,
            "merge_output_format": format_file,
        },
        "mp3": {
            "format": "bestaudio/best",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": quality,
                },
                {"key": "EmbedThumbnail", "already_have_thumbnail": False},
            ],
        },
        "webm": {
            "format_sort": ["vcodec:vp9", f"res:{quality}", "acodec:opus"],
            "writethumbnail": True,
            "merge_output_format": format_file,
        },
        "flac": {
            "format": "bestaudio/best",
            "postprocessors": [
                {"key": "EmbedThumbnail", "already_have_thumbnail": False},
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "flac",
                    "preferredquality": quality,
                },
            ],
        },
    }

    fmt_opts = formats.get(format_file)
    if fmt_opts:
        base.update(fmt_opts)  # type: ignore[arg-type]
    return base
