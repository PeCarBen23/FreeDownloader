# 🎵 FreeDownloader

**Una aplicación de escritorio moderna y ligera para descargar música y videos de YouTube y Spotify a formato MP3.**

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange.svg)](https://docs.python.org/3/library/tkinter.html)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#)

---

## 🚀 Características

- **Interfaz Gráfica Intuitiva (GUI):** Desarrollada con Tkinter, limpia y fácil de usar.
- **Soporte Multiplataforma / Servicios:**
  * 🔴 **YouTube:** Descarga videos individuales o listas de reproducción completas (`yt-dlp`).
  * 🟢 **Spotify:** Descarga canciones directamente (`spotdl`).
- **Personalización de Rutas:** Cambia el directorio de descarga predeterminado de forma sencilla con un solo clic.
- **Temas Oscuro / Claro:** Alterna entre modos visuales según tu comodidad (Modo Oscuro activado por defecto).
- **Consola en Tiempo Real:** Visualiza el progreso detallado de la descarga dentro de la misma aplicación.
- **Dependencias siempre al día:** Al abrir la aplicación se comprueba si `yt-dlp` y `spotdl` están instalados en su última versión y, si no, se instalan o actualizan automáticamente.
- **Sin consolas externas:** Todo el progreso se muestra dentro de la aplicación, y el botón de descarga es siempre visible aunque reduzcas la ventana.

---

## 🆕 Novedades de la v1.1.0

- Corregido: ya no se abre una consola externa al descargar.
- Corregido: el botón **Iniciar Descarga** se ve siempre al reducir el tamaño de la ventana.
- Nuevo: comprobación y actualización automática de `yt-dlp` y `spotdl` en cada arranque.

---

## 🛠️ Tecnologías Utilizadas

- [Python](https://www.python.org/) - Lenguaje de programación principal.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - Librería para la interfaz gráfica.
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Motor de descarga para YouTube.
- [spotdl](https://github.com/spotdl/spotify-downloader) - Motor de descarga para Spotify.

---

## 💾 Instalación (Usuarios)

Descarga **`FreeDownloader-Installer.exe`** desde la [última release](https://github.com/PeCarBen23/FreeDownloader/releases/latest) y ejecútalo.

Requisitos previos (no se instalan solos):

- **Python 3.11+ con `pip`** en el `PATH`. Con él, `yt-dlp` y `spotdl` se instalan y actualizan automáticamente.
- **FFmpeg** en el `PATH`, necesario para convertir el audio a MP3.

---

## 📦 Instalación y Uso (Desarrolladores)

Si deseas clonar el repositorio y ejecutar el código fuente:

1. Clona el repositorio:

   ```
   git clone https://github.com/PeCarBen23/FreeDownloader.git
   ```

2. Descarga las dependencias: `pip install yt-dlp spotdl`

3. Ejecuta el main(): `python src/main.py`
