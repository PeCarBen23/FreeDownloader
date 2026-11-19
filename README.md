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

Esta guía está pensada para cualquier persona, aunque no tenga conocimientos de informática. Solo hay que hacerla **una vez**. Son 3 pasos:

1. Instalar **Python** (el programa necesita que esté en el ordenador).
2. Instalar **FFmpeg** (convierte el audio a MP3).
3. Instalar **FreeDownloader**.

> 💡 No te preocupes por `yt-dlp` y `spotdl`: **se instalan y se actualizan solos** cuando abres FreeDownloader, siempre que tengas Python.

### Paso 1: Instalar Python

1. Entra en [python.org/downloads](https://www.python.org/downloads/) y pulsa el botón amarillo **Download Python 3.x**.
2. Abre el archivo descargado.
3. **MUY IMPORTANTE:** en la primera pantalla del instalador, marca la casilla **"Add python.exe to PATH"** (abajo del todo) antes de pulsar nada más.
4. Pulsa **Install Now** y espera a que termine.

Para comprobar que se ha instalado bien, pulsa la tecla `Windows`, escribe `PowerShell`, ábrelo y escribe estos dos comandos (pulsa Enter después de cada uno):

```
python --version
pip --version
```

Si ambos muestran un número de versión (por ejemplo `Python 3.11.9`), todo está correcto. Si dicen que no se reconoce el comando, vuelve a ejecutar el instalador de Python, elige **Modify** y marca la casilla de añadir Python al PATH (o desinstálalo y vuelve a instalarlo marcándola).

### Paso 2: Instalar FFmpeg

FFmpeg es el programa que convierte lo descargado a MP3. Sin él, las descargas de YouTube fallarán al convertir el audio.

1. Pulsa la tecla `Windows`, escribe `PowerShell` y ábrelo.
2. Copia y pega este comando y pulsa Enter:

   ```
   winget install --id Gyan.FFmpeg
   ```

3. Si te pregunta algo, escribe `S` (o `Y`) y pulsa Enter. Espera a que termine.
4. **Cierra PowerShell y ábrelo de nuevo**, y comprueba que funciona:

   ```
   ffmpeg -version
   ```

   Si aparece información de la versión, está listo. Si no se reconoce el comando, reinicia el ordenador y prueba otra vez.

### Paso 3: Instalar FreeDownloader

1. Entra en la [última release](https://github.com/PeCarBen23/FreeDownloader/releases/latest).
2. En el apartado **Assets**, haz clic en **`FreeDownloader-Installer.exe`** para descargarlo.
3. Ábrelo. Si Windows muestra el aviso azul **"Windows protegió su PC"**, pulsa **Más información** y después **Ejecutar de todas formas** (aparece porque el programa no tiene firma digital de pago, no porque sea peligroso).
4. Sigue el asistente con **Siguiente**. Si quieres un acceso directo en el escritorio, marca la casilla correspondiente.
5. Al terminar, el instalador descarga `yt-dlp` y `spotdl` automáticamente. Puede tardar un minuto; no cierres nada.

### Primer uso

1. Abre **FreeDownloader** desde el menú Inicio (o el acceso directo del escritorio).
2. Durante unos segundos, el botón **Iniciar Descarga** aparecerá apagado y la consola mostrará `[Inicio] Comprobando actualizaciones...`. Es normal: la aplicación está comprobando que tiene lo último. Cuando aparezca `[OK]`, el botón se enciende.
3. Elige **YouTube** o **Spotify**.
4. Elige si quieres **solo la canción/video** o **toda la playlist**.
5. Pega el enlace en el campo **URL** y pulsa **Iniciar Descarga**.
6. Cuando termine, aparecerá un mensaje de "Completado". Por defecto, los archivos se guardan en tu carpeta **Descargas**; puedes cambiarlo con **Cambiar Ruta** y abrirla con **Abrir Ruta**.

### ❓ Problemas frecuentes

| Mensaje o problema | Qué hacer |
| --- | --- |
| `[Aviso] No se encontró pip` | Python no está instalado o no se marcó "Add python.exe to PATH". Repite el Paso 1. |
| `No se encontró el comando requerido` / `No se encontró 'yt-dlp'` | `yt-dlp` o `spotdl` no se han instalado. Comprueba el Paso 1 y abre FreeDownloader con conexión a internet para que se instalen. |
| La descarga termina con error al convertir a MP3 | Falta FFmpeg o no está en el PATH. Repite el Paso 2 y reinicia el ordenador. |
| `[Aviso] No se pudo comprobar las actualizaciones` | No hay conexión a internet. La aplicación sigue funcionando con las versiones que ya tengas instaladas. |
| El botón **Iniciar Descarga** está apagado | Espera unos segundos: se está comprobando `yt-dlp` y `spotdl`. Se enciende solo al terminar. |

---

## 📦 Instalación y Uso (Desarrolladores)

Si deseas clonar el repositorio y ejecutar el código fuente:

1. Clona el repositorio:

   ```
   git clone https://github.com/PeCarBen23/FreeDownloader.git
   ```

2. Descarga las dependencias: `pip install yt-dlp spotdl`

3. Ejecuta el main(): `python src/main.py`
