import os
import queue
import threading
import subprocess
import tkinter as tk
from tkinter import messagebox

# Variable global para almacenar la ruta personalizada de descargas
RUTA_PERSONALIZADA = None

# En Windows evita que yt-dlp / spotdl abran una consola externa.
# (En otros sistemas la constante no existe y el valor es 0, sin efecto.)
CREATE_NO_WINDOW = getattr(subprocess, "CREATE_NO_WINDOW", 0)


def establecer_ruta_descarga(nueva_ruta):
    """Establece una nueva ruta personalizada para las descargas."""
    global RUTA_PERSONALIZADA
    RUTA_PERSONALIZADA = nueva_ruta


def ejecutar_descarga(url, opcion, servicio, cola):
    """Se ejecuta en un hilo. NO toca la interfaz: manda mensajes a la cola."""
    # Usar la ruta personalizada si se ha definido y es válida, de lo contrario usar la por defecto
    if RUTA_PERSONALIZADA and os.path.isdir(RUTA_PERSONALIZADA):
        downloads_path = RUTA_PERSONALIZADA
    else:
        user_profile = os.environ.get("USERPROFILE") or os.path.expanduser("~")
        downloads_path = os.path.join(user_profile, "Downloads")

    os.makedirs(downloads_path, exist_ok=True)

    # Definir la herramienta y comandos según el servicio seleccionado
    if servicio == "youtube":
        tool = "yt-dlp"
        if opcion == 1:
            comando = [
                tool, "-x", "--audio-format", "mp3", "--no-playlist",
                "--extractor-args", "youtube:player-client=android",
                "-o", "%(title)s.%(ext)s", url
            ]
        else:
            comando = [
                tool, "-x", "--audio-format", "mp3", "--yes-playlist",
                "--extractor-args", "youtube:player-client=android",
                "-o", os.path.join("%(playlist)s", "%(playlist_index)s - %(title)s.%(ext)s"), url
            ]
    else:  # Spotify con spotdl
        tool = "spotdl"
        comando = [tool, url]

    cola.put(("texto", f"Iniciando descarga en: {downloads_path}\n"))
    cola.put(("texto", f"Iniciando descarga con {tool}...\n"))

    try:
        proceso = subprocess.Popen(
            comando,
            cwd=downloads_path,
            stdin=subprocess.DEVNULL,        # sin consola no hay stdin válido
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="ignore",
            creationflags=CREATE_NO_WINDOW,  # <- sin ventana de consola externa
        )

        for linea in iter(proceso.stdout.readline, ''):
            cola.put(("texto", linea))

        proceso.stdout.close()
        proceso.wait()

        if proceso.returncode == 0:
            cola.put(("texto", "\n[Éxito] ¡Proceso finalizado correctamente!\n"))
            cola.put(("info", "La descarga ha finalizado con éxito."))
        else:
            cola.put(("texto", "\n[Aviso] El proceso finalizó con códigos de error.\n"))

    except FileNotFoundError:
        cola.put(("texto", "\n[Error] No se encontró el comando requerido. Asegúrate de tenerlo instalado y en el PATH.\n"))
        cola.put(("error", f"No se encontró '{tool}' en el sistema."))
    except Exception as e:
        cola.put(("texto", f"\n[Error inesperado]: {e}\n"))
    finally:
        cola.put(("fin", None))


def _procesar_cola(cola, text_widget, btn_descargar):
    """Se ejecuta en el hilo principal (tkinter): vuelca los mensajes del hilo a la UI."""
    terminado = False
    try:
        while True:
            tipo, dato = cola.get_nowait()
            if tipo == "texto":
                text_widget.insert(tk.END, dato)
                text_widget.see(tk.END)
            elif tipo == "info":
                messagebox.showinfo("Completado", dato)
            elif tipo == "error":
                messagebox.showerror("Error", dato)
            elif tipo == "fin":
                terminado = True
    except queue.Empty:
        pass

    if terminado:
        btn_descargar.config(state=tk.NORMAL)
    else:
        text_widget.after(50, _procesar_cola, cola, text_widget, btn_descargar)


def iniciar_hilo(url_entry, opcion, servicio_actual, text_widget, btn_descargar):
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Campo vacío", "Por favor, introduce una URL válida.")
        return

    btn_descargar.config(state=tk.DISABLED)
    text_widget.delete(1.0, tk.END)

    cola = queue.Queue()
    hilo = threading.Thread(
        target=ejecutar_descarga,
        args=(url, opcion.get(), servicio_actual.get(), cola),
        daemon=True,
    )
    hilo.start()
    _procesar_cola(cola, text_widget, btn_descargar)
