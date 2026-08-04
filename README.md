# VideoGrabber

[![Python](https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.3-000000)](https://flask.palletsprojects.com/)
[![yt-dlp](https://img.shields.io/badge/yt--dlp-2026.7.4-red)](https://github.com/yt-dlp/yt-dlp)
[![uv](https://img.shields.io/badge/uv-0.11.24-8B5CF6)](https://docs.astral.sh/uv/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

<img width="1920" height="994" alt="изображение" src="https://github.com/user-attachments/assets/48efc582-fd71-4be9-af37-28e70ace2c1e" />


## 📖 О проекте

**VideoGrabber** — это веб-интерфейс (обёртка над yt-dlp) для скачивания видео и аудио с YouTube, Vimeo и ещё многих сайтов.

## 🛠 Технологии
*   **Бэкенд:** Python, Flask
*   **Фронтенд:** HTML, CSS, JavaScript
*   **Загрузчик:** yt-dlp
*   **Обработка:** FFmpeg

## ✨ Возможности
*   🎞️ Выбор формата: MP4, WebM, MP3, FLAC
*   📐 Выбор качества (разрешение для видео, битрейт для аудио)
*   🖼️ Автоматическое встраивание обложки (thumbnail)

## 🔧 Установка и запуск
Для запуска понадобиться:
* **[FFmepg](https://ffmpeg.org/download.html)** - конвертер.
* **[Deno](https://deno.com/)** - js движок.
* **[uv](https://docs.astral.sh/uv/)** - пакетный менеджер для Python.

Установите их и укажите на их расположение в переменную среду PATH.

```bash
# 1. Клонировать репозиторий
git clone https://github.com/feok1ist/VideoGrabber.git

# 2. Запустить start.bat

# Готово — открыть http://127.0.0.1:5000
```

## ❗ Важно
*   Все скаченные файлы храняться в папке **`result/`** (в корне проекта).
*   В VideoGrabber нет обхода блокировок, используйте VPN или на сайте в Advanced введите прокси (поддерживает http, https, socks5, socks4)

## ❓ Почему VideoGrabber?
*   **Анонимно** - сервер разворачиваеться локально и только под вас, все скаченные файлы доступны только вам.
*	**Бесплатно** - абсолютно бесплатно и без лимитов.
*	**Открытый код** - весь код можно просмотреть, узнать как всё работает.
