from flask import Flask, render_template, request  # type: ignore[import]

from utils import (
    download_video,
    find_downloaded_file,
    folder_for_tmp,
    generation_ydl_opts,
    move_to_result,
)

app = Flask(__name__, template_folder="template")


@app.route("/", methods=["POST", "GET"])
def main():
    filename = None
    error = None
    if request.method == "POST":
        url = request.form.get("url")
        format_file = request.form.get("format")
        quality = request.form.get("quality")

        tmp = folder_for_tmp()
        try:
            ydl_opts = generation_ydl_opts(tmp, format_file, quality)
            download_video(url, ydl_opts)
            filename = find_downloaded_file(tmp, format_file)
            if filename:
                move_to_result(filename)
            for f in tmp.iterdir():
                try:
                    f.unlink()
                except Exception:
                    pass
        except Exception as e:
            error = f"Invalid URL or download failed: {e}"

    return render_template("index.html", filename=filename, error=error)


if __name__ == "__main__":
    app.run(debug=True)
