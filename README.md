# VideoGrabber

> Пет-проект — обёртка над yt-dlp с веб-интерфейсом на Flask.

## 📖 О проекте

**VideoGrabber** — это веб-приложение для скачивания видео и аудио с YouTube, Vimeo и ещё 1000+ сайтов. Вставляешь ссылку, выбираешь формат и качество — получаешь готовый файл.

## ✨ Возможности

*   ✂️ Скачивание видео с YouTube, Vimeo, Dailymotion и других сайтов
*   🎞️ Выбор формата: MP4, WebM, MP3, FLAC
*   📐 Выбор качества (разрешение для видео, битрейт для аудио)
*   🖼️ Автоматическое встраивание обложки (thumbnail)
*   🌙 Тёмная тема

## 🔧 Установка и запуск

```bash
# 1. Клонировать репозиторий
git clone https://github.com/EnotPolzovatel/VideoGrabber.git
cd VideoGrabber

# 2. Установить uv (если ещё не установлен)
# Windows (PowerShell):
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
# macOS/Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh

# 3. Создать виртуальное окружение и установить зависимости
uv sync

# 4. Запустить
uv run python src/main.py

# Готово — открыть http://127.0.0.1:5000
```

> **FFmpeg** нужен для конвертации аудио (MP3/FLAC) и встраивания обложек.
> Скачай с [ffmpeg.org](https://ffmpeg.org/download.html) и добавь `ffmpeg` в `PATH`, либо положи `ffmpeg.exe` в папку проекта.

## 🛠 Технологии

*   **Бэкенд:** Python, Flask
*   **Фронтенд:** HTML, CSS, JavaScript (vanilla)
*   **Загрузчик:** yt-dlp
*   **Обработка:** FFmpeg (конвертация аудио, встраивание обложек)

## 📚 Что я изучил в процессе

*   Интеграция yt-dlp в веб-приложение
*   Обработка POST-запросов и рендеринг шаблонов Flask
*   Динамическое переключение опций на фронтенде (формат → качество)
*   Работа с файловой системой (временные папки, перенос файлов)
*   Настройка pre-commit, ruff, mypy
*   Конфигурация Python-проекта (pyproject.toml)

## 📝 Итог

Проект делал в несколько подходов. Получился минималистичный, но рабочий инструмент для скачивания медиа. Без излишеств — вставил ссылку, выбрал формат, получил файл.

[Следующий проект — Shorty](https://github.com/EnotPolzovatel/Shortly)
