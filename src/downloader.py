import os
import threading
import subprocess
import tkinter as tk
from tkinter import messagebox

# Variable global para almacenar la ruta personalizada de descargas
RUTA_PERSONALIZADA = None

def establecer_ruta_descarga(nueva_ruta):
    """Establece una nueva ruta personalizada para las descargas."""
    global RUTA_PERSONALIZADA
    RUTA_PERSONALIZADA = nueva_ruta

def ejecutar_descarga(url, opcion, servicio, text_widget, btn_descargar):
    # Usar la ruta personalizada si se ha definido y es válida, de lo contrario usar la por defecto
    if RUTA_PERSONALIZADA and os.path.isdir(RUTA_PERSONALIZADA):
        downloads_path = RUTA_PERSONALIZADA
    else:
        user_profile = os.environ.get("USERPROFILE")
        downloads_path = os.path.join(user_profile, "Downloads")
        
    os.makedirs(downloads_path, exist_ok=True)
    os.chdir(downloads_path)
    
    # Definir la herramienta y comandos según el servicio seleccionado
    if servicio == "youtube":
        tool = "yt-dlp"
        if opcion.get() == 1:
            comando = [tool, "-x", "--audio-format", "mp3", "--no-playlist", "-o", "%(title)s.%(ext)s", url]
        else:
            comando = [tool, "-x", "--audio-format", "mp3", "--yes-playlist", "-o", os.path.join("%(playlist)s", "%(playlist_index)s - %(title)s.%(ext)s"), url]
    else:  # Spotify con spotdl
        tool = "spotdl"
        comando = [tool, url]
    
    text_widget.insert(tk.END, f"Iniciando descarga en: {downloads_path}\n")
    text_widget.insert(tk.END, f"Iniciando descarga con {tool}...\n")
    text_widget.see(tk.END)
    
    try:
        proceso = subprocess.Popen(
            comando, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT, 
            text=True, 
            encoding="utf-8",
            errors="ignore"
        )
        
        for linea in iter(proceso.stdout.readline, ''):
            text_widget.insert(tk.END, linea)
            text_widget.see(tk.END)
            
        proceso.stdout.close()
        proceso.wait()
        
        if proceso.returncode == 0:
            text_widget.insert(tk.END, "\n[Éxito] ¡Proceso finalizado correctamente!\n")
            messagebox.showinfo("Completado", "La descarga ha finalizado con éxito.")
        else:
            text_widget.insert(tk.END, "\n[Aviso] El proceso finalizó con códigos de error.\n")
            
    except FileNotFoundError:
        text_widget.insert(tk.END, "\n[Error] No se encontró el comando requerido. Asegúrate de tenerlo instalado y en el PATH.\n")
        messagebox.showerror("Error", f"No se encontró '{tool}' en el sistema.")
    except Exception as e:
        text_widget.insert(tk.END, f"\n[Error inesperado]: {e}\n")
    
    btn_descargar.config(state=tk.NORMAL)

def iniciar_hilo(url_entry, opcion, servicio_actual, text_widget, btn_descargar):
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Campo vacío", "Por favor, introduce una URL válida.")
        return
    
    btn_descargar.config(state=tk.DISABLED)
    text_widget.delete(1.0, tk.END)
    
    hilo = threading.Thread(target=ejecutar_descarga, args=(url, opcion, servicio_actual.get(), text_widget, btn_descargar))
    hilo.daemon = True
    hilo.start()