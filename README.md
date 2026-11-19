# 🎵 FreeDownloader

**Una aplicación de escritorio moderna y ligera para descargar música y videos de YouTube y Spotify a formato MP3.**

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange.svg)](https://docs.python.org/3/library/tkinter.html)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#)
[![Release](https://img.shields.io/github/v/release/PeCarBen23/FreeDownloader)](https://github.com/PeCarBen23/FreeDownloader/releases/latest)

---

## 🚀 Características

- **Interfaz gráfica intuitiva (GUI):** desarrollada con Tkinter, limpia y fácil de usar.
- **Soporte para varios servicios:**
  - 🔴 **YouTube:** descarga videos individuales o listas de reproducción completas (`yt-dlp`).
  - 🟢 **Spotify:** descarga canciones directamente (`spotdl`).
- **Dependencias siempre al día:** al abrir la aplicación se comprueba si `yt-dlp` y `spotdl` están instalados y en su última versión; si no, se instalan o actualizan automáticamente.
- **Aviso de nuevas versiones:** la aplicación avisa en su consola cuando hay una versión nueva en GitHub.
- **Sin ventanas de consola externas:** todo el progreso se muestra dentro de la propia aplicación.
- **Diseño adaptable:** el botón de descarga es siempre visible, aunque se reduzca el tamaño de la ventana.
- **Personalización de rutas:** cambia el directorio de descarga predeterminado con un solo clic.
- **Temas oscuro / claro:** alterna entre modos visuales (modo oscuro por defecto).
- **Consola en tiempo real:** visualiza el progreso detallado de la descarga dentro de la misma aplicación.

---

## 🆕 Novedades de la v1.1.0

- Corregido: ya no se abre una consola externa al descargar.
- Corregido: el botón **Iniciar Descarga** se ve siempre al reducir la ventana, que ahora tiene un tamaño mínimo calculado según su contenido.
- Nuevo: comprobación y actualización automática de `yt-dlp` y `spotdl` en cada arranque (el botón de descarga se desactiva unos segundos mientras tanto).
- Mejora: las descargas ya no escriben en la interfaz desde un hilo secundario, lo que evita cuelgues ocasionales.

---

## 📥 Instalación (usuarios)

1. Descarga **`FreeDownloader-Installer.exe`** desde la [última release](https://github.com/PeCarBen23/FreeDownloader/releases/latest).
2. Ejecútalo y sigue el asistente (puedes crear un acceso directo en el escritorio).
3. Abre **FreeDownloader** desde el menú Inicio.

### Requisitos

- **Windows 10/11** y conexión a internet.
- **Python 3.11+ con `pip`** instalado y en el `PATH` (requisito previo, no se instala solo). Con él, `yt-dlp` y `spotdl` **se instalan y actualizan automáticamente**, tanto al instalar la aplicación como en cada arranque.
- **FFmpeg** instalado y en el `PATH` (requisito previo, no se instala solo): necesario para convertir el audio a MP3. Si tienes `spotdl`, puedes instalarlo con `spotdl --download-ffmpeg`.

---

## 🧑‍💻 Uso

1. Elige el servicio: **YouTube** o **Spotify**.
2. Elige si quieres descargar **solo la canción/video** o **toda la playlist/álbum**.
3. Pega la **URL** del contenido.
4. Pulsa **Iniciar Descarga** y sigue el progreso en la consola integrada.

Desde la barra superior puedes **abrir la carpeta de descargas**, **cambiar la ruta**, **limpiar la consola** y **alternar el tema**.

---

## 🛠️ Tecnologías utilizadas

- [Python](https://www.python.org/) - lenguaje de programación principal.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - librería para la interfaz gráfica.
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - motor de descarga para YouTube.
- [spotdl](https://github.com/spotdl/spotify-downloader) - motor de descarga para Spotify.
- [PyInstaller](https://pyinstaller.org/) e [Inno Setup](https://jrsoftware.org/isinfo.php) - empaquetado y creación del instalador.

---

## 📦 Ejecución desde el código fuente (desarrolladores)

1. Clona el repositorio:

   ```bash
   git clone https://github.com/PeCarBen23/FreeDownloader.git
   cd FreeDownloader
   ```

2. Instala las dependencias:

   ```bash
   pip install yt-dlp spotdl
   ```

3. Ejecuta la aplicación (con `pythonw` para que no se abra una consola):

   ```bash
   python src/main.py
   ```

### Compilar el `.exe` y el instalador

```bash
pyinstaller DescargadorMultimedia.spec
```

Después, compila `src/setup.iss` con Inno Setup. El instalador se genera en `src/output/FreeDownloader-Installer.exe`.

---

## 📁 Estructura del proyecto

```
FreeDownloader/
├── src/
│   ├── main.py          # Punto de entrada, comprobación de dependencias y versión
│   ├── UI.py            # Interfaz gráfica (Tkinter)
│   ├── downloader.py    # Lógica de descarga (yt-dlp / spotdl)
│   └── setup.iss        # Script del instalador (Inno Setup)
├── DescargadorMultimedia.spec   # Configuración de PyInstaller
└── README.md
```

---

## ⚠️ Aviso legal

Esta herramienta es solo para uso personal. Descarga únicamente contenido que tengas derecho a descargar y respeta los términos de servicio de YouTube y Spotify y las leyes de propiedad intelectual de tu país.
