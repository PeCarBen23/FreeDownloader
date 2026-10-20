import tkinter as tk
import threading
import subprocess
import urllib.request
import json
from UI import construir_interfaz

# REEMPLAZA con tu usuario y repositorio real en GitHub
GITHUB_REPO_API = "https://api.github.com/repos/PeCarBen23/FreeDownloader/releases/latest"
VERSION_ACTUAL = "v1.0.0"  # Sube esta versión cuando lances actualizaciones

def actualizar_y_verificar(root, txt_consola=None):
    """Ejecuta tareas en segundo plano al iniciar la app."""
    try:
        # 1. Actualizar yt-dlp de forma silenciosa en segundo plano
        # Usamos CREATE_NO_WINDOW para que no aparezca ninguna ventana negra de CMD en Windows
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        
        subprocess.run(
            ["pip", "install", "--upgrade", "yt-dlp"],
            startupinfo=startupinfo,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except Exception:
        pass  # Si no hay internet o falla pip, la app sigue funcionando con normalidad

    try:
        # 2. Comprobar si hay nueva versión en GitHub
        req = urllib.request.Request(
            GITHUB_REPO_API, 
            headers={'User-Agent': 'FreeDownloader-App'}
        )
        with urllib.request.urlopen(req, timeout=4) as response:
            data = json.loads(response.read().decode())
            latest_version = data.get("tag_name")
            
            if latest_version and latest_version != VERSION_ACTUAL:
                # Si hay una versión más nueva, podemos mostrar un aviso en consola o un pop-up suave
                if txt_consola:
                    root.after(0, lambda: txt_consola.insert(
                        tk.END, f"\n[Aviso] ¡Hay una nueva versión disponible ({latest_version})! Descárgala desde GitHub.\n"
                    ))
    except Exception:
        pass  # Si falla la conexión con GitHub, se ignora silenciosamente

def main():
    root = tk.Tk()
    
    # Construir la interfaz gráfica principal
    construir_interfaz(root)
    
    # Intentar obtener la referencia de la consola si existe en la UI (opcional)
    # Lanzar los procesos en segundo plano usando un hilo para no congelar la ventana al abrir
    hilo_inicio = threading.Thread(target=actualizar_y_verificar, args=(root,))
    hilo_inicio.daemon = True
    hilo_inicio.start()
    
    root.mainloop()

if __name__ == "__main__":
    main()