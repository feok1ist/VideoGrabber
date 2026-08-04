import json
from pathlib import Path

from flask import Flask, render_template, request  # type: ignore[import]

from utils import (
    download_video,
    find_downloaded_file,
    folder_for_tmp,
    generation_ydl_opts,
    move_to_result,
)

app = Flask(__name__, template_folder="template")

CONFIG_PATH = Path(__file__).resolve().parent.parent / "config.json"


def load_proxy() -> str:
    if CONFIG_PATH.exists():
        try:
            data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
            return data.get("proxy", "")
        except (json.JSONDecodeError, OSError):
            return ""
    return ""


def save_proxy(proxy: str) -> None:
    CONFIG_PATH.write_text(
        json.dumps({"proxy": proxy}, ensure_ascii=False, indent=4),
        encoding="utf-8",
    )


@app.route("/", methods=["POST", "GET"])
def main():
    filename = None
    error = None
    if request.method == "POST":
        url = request.form.get("url")
        format_file = request.form.get("format")
        quality = request.form.get("quality")
        proxy = request.form.get("proxy", "").strip()
        save_proxy(proxy)

        tmp = folder_for_tmp()  # Создаёт папку под временное хранение файлов
        try:
            ydl_opts = generation_ydl_opts(
                tmp, format_file, quality, proxy
            )  # Генерирует настройки для yt-dlp
            download_video(url, ydl_opts)  # Скачивает видео по заданным настройкам yt-dlp
            filename = find_downloaded_file(tmp, format_file)  # Указывает на скаченный файл в tmp
            if filename:
                move_to_result(filename)  # Перемещает файл из tmp в папку result
            for f in tmp.iterdir():
                try:
                    f.unlink()
                except Exception:
                    pass
        except Exception as e:
            error = f"Invalid URL or download failed: {e}"

    proxy = load_proxy()
    return render_template("index.html", filename=filename, error=error, proxy=proxy)


if __name__ == "__main__":
    app.run()
