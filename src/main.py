import tkinter as tk
import threading
import subprocess
import shutil
import urllib.request
import json
from UI import construir_interfaz

# REEMPLAZA con tu usuario y repositorio real en GitHub
GITHUB_REPO_API = "https://api.github.com/repos/PeCarBen23/FreeDownloader/releases/latest"
VERSION_ACTUAL = "v1.1.0"  # Sube esta versión cuando lances actualizaciones

# Dependencias que se comprueban/actualizan en cada arranque (pip install --upgrade ...)
DEPENDENCIAS = ["yt-dlp", "spotdl"]

# En Windows evita que pip abra una ventana de consola
CREATE_NO_WINDOW = getattr(subprocess, "CREATE_NO_WINDOW", 0)


def escribir(root, txt_consola, texto):
    """Escribe en la consola de la app de forma segura desde otro hilo."""
    def _insertar():
        txt_consola.insert(tk.END, texto)
        txt_consola.see(tk.END)
    try:
        root.after(0, _insertar)
    except Exception:
        pass  # La ventana ya se cerró


def _comando_pip():
    """Devuelve el comando para ejecutar pip, o None si no hay ninguno disponible."""
    for candidato in (["pip"], ["py", "-m", "pip"], ["python", "-m", "pip"]):
        if shutil.which(candidato[0]):
            return candidato
    return None


def actualizar_dependencias(root, txt_consola):
    """Instala yt-dlp y spotdl si faltan y los actualiza si hay una versión más nueva."""
    escribir(root, txt_consola, "[Inicio] Comprobando actualizaciones de yt-dlp y spotdl...\n")

    pip = _comando_pip()
    if pip is None:
        escribir(root, txt_consola, "[Aviso] No se encontró pip; se usarán las versiones ya instaladas.\n")
        return

    try:
        resultado = subprocess.run(
            pip + ["install", "--upgrade", "--disable-pip-version-check",
                   "--retries", "1", "--timeout", "10", *DEPENDENCIAS],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="ignore",
            creationflags=CREATE_NO_WINDOW,
            timeout=300,
        )
    except Exception:
        escribir(root, txt_consola, "[Aviso] No se pudo comprobar las actualizaciones; se usarán las versiones ya instaladas.\n")
        return

    if resultado.returncode != 0:
        escribir(root, txt_consola, "[Aviso] No se pudo comprobar las actualizaciones (¿sin internet?); se usarán las versiones ya instaladas.\n")
    else:
        instalado = [l for l in resultado.stdout.splitlines() if l.startswith("Successfully installed")]
        if instalado:
            escribir(root, txt_consola, f"[OK] {instalado[0]}\n")
        else:
            escribir(root, txt_consola, "[OK] yt-dlp y spotdl ya están en la última versión.\n")


def comprobar_version_app(root, txt_consola):
    """Comprueba si hay una nueva versión de la app en GitHub."""
    try:
        req = urllib.request.Request(
            GITHUB_REPO_API,
            headers={'User-Agent': 'FreeDownloader-App'}
        )
        with urllib.request.urlopen(req, timeout=4) as response:
            data = json.loads(response.read().decode())
            latest_version = data.get("tag_name")

            if latest_version and latest_version != VERSION_ACTUAL:
                escribir(root, txt_consola,
                         f"\n[Aviso] ¡Hay una nueva versión disponible ({latest_version})! Descárgala desde GitHub.\n")
    except Exception:
        pass  # Si falla la conexión con GitHub, se ignora silenciosamente


def tareas_de_inicio(root, txt_consola, btn_descargar):
    """Se ejecuta en un hilo al abrir la app, para no congelar la ventana."""
    try:
        actualizar_dependencias(root, txt_consola)
    finally:
        # Se vuelve a habilitar el botón aunque falle algo
        try:
            root.after(0, lambda: btn_descargar.config(state=tk.NORMAL))
        except Exception:
            pass
    comprobar_version_app(root, txt_consola)


def main():
    root = tk.Tk()

    # Construir la interfaz gráfica principal
    txt_consola, btn_descargar = construir_interfaz(root)

    # Mientras se actualizan yt-dlp/spotdl no se puede iniciar una descarga
    # (evita que pip sustituya un ejecutable que se está usando)
    btn_descargar.config(state=tk.DISABLED)

    hilo_inicio = threading.Thread(target=tareas_de_inicio, args=(root, txt_consola, btn_descargar), daemon=True)
    hilo_inicio.start()

    root.mainloop()


if __name__ == "__main__":
    main()
