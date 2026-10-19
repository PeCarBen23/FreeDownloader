# 🎵 FreeDownloader

<p align="center">
  <b>Una aplicación de escritorio moderna y ligera para descargar música y videos de YouTube y Spotify a formato MP3.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Tkinter-GUI-orange.svg" alt="Tkinter">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>

---

## 🚀 Características

* **Interfaz Gráfica Intuitiva (GUI):** Desarrollada con Tkinter, limpia y fácil de usar.
* **Soporte Multiplataforma / Servicios:**
  * 🔴 **YouTube:** Descarga videos individuales o listas de reproducción completas (`yt-dlp`).
  * 🟢 **Spotify:** Descarga canciones directamente (`spotdl`).
* **Personalización de Rutas:** Cambia el directorio de descarga predeterminado de forma sencilla con un solo clic.
* **Temas Oscuro / Claro:** Alterna entre modos visuales según tu comodidad (Modo Oscuro activado por defecto).
* **Consola en Tiempo Real:** Visualiza el progreso detallado de la descarga dentro de la misma aplicación.

---

## 🛠️ Tecnologías Utilizadas

* [Python](https://www.python.org/) - Lenguaje de programación principal.
* [Tkinter](https://docs.python.org/3/library/tkinter.html) - Librería para la interfaz gráfica.
* [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Motor de descarga para YouTube.
* [spotdl](https://github.com/spotdl/spotify-downloader) - Motor de descarga para Spotify.

---

## 📦 Instalación y Uso (Desarrolladores)

Si deseas clonar el repositorio y ejecutar el código fuente:

1. Clona el repositorio:
   ```bash
   git clone [https://github.com/PeCarBen23/FreeDownloader.git](https://github.com/PeCarBen23/FreeDownloader.git)

2. Descarga las dependencias:
    pip install yt-dlp spotdl

3. Ejecuta el main():
    python src/main.py