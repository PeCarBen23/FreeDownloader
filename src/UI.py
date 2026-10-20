import os
import tkinter as tk
from tkinter import scrolledtext, messagebox
from downloader import iniciar_hilo, establecer_ruta_descarga

def cambiar_servicio(servicio, lbl_servicio, rb1, rb2, btn_yt, btn_spotify, servicio_actual):
    servicio_actual.set(servicio)
    if servicio == "youtube":
        lbl_servicio.config(text="Descargador de YouTube a MP3", fg="#FF0000")
        rb1.config(text="1. Descargar SOLO la canción / video")
        rb2.config(text="2. Descargar TODA la playlist")
        btn_yt.config(relief=tk.SUNKEN, bd=4)
        btn_spotify.config(relief=tk.RAISED, bd=2)
    else:
        lbl_servicio.config(text="Descargador de Spotify a MP3", fg="#1DB954")
        rb1.config(text="1. Descargar SOLO la canción")
        rb2.config(text="2. Descargar TODO el álbum / playlist")
        btn_spotify.config(relief=tk.SUNKEN, bd=4)
        btn_yt.config(relief=tk.RAISED, bd=2)

def abrir_carpeta_descargas():
    user_profile = os.environ.get("USERPROFILE")
    downloads_path = os.path.join(user_profile, "Downloads")
    os.makedirs(downloads_path, exist_ok=True)
    os.startfile(downloads_path)

def limpiar_consola(txt_consola):
    txt_consola.delete(1.0, tk.END)

def guardar_nueva_ruta(entry_ruta):
    nueva_ruta = entry_ruta.get().strip()
    if not nueva_ruta:
        messagebox.showwarning("Campo vacío", "Por favor, introduce una ruta válida.")
        return
    if not os.path.exists(nueva_ruta):
        try:
            os.makedirs(nueva_ruta, exist_ok=True)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo crear la ruta: {e}")
            return
            
    establecer_ruta_descarga(nueva_ruta)
    messagebox.showinfo("Ruta Actualizada", f"La ruta de descargas se ha establecido en:\n{nueva_ruta}")

def alternar_tema(root, toolbar, titulo_label, entry_url, btn_descargar, widgets_texto, widgets_botones_toolbar, modo_oscuro):
    if modo_oscuro.get():
        root.config(bg="#f0f0f0")
        toolbar.config(bg="#e0e0e0")
        titulo_label.config(bg="#f0f0f0", fg="#000000")
        entry_url.config(bg="#ffffff", fg="#000000", insertbackground="#000000")
        btn_descargar.config(bg="#4CAF50", fg="#ffffff")
        
        for w in widgets_botones_toolbar:
            w.config(bg="#e0e0e0", fg="#000000")
            
        for w in widgets_texto:
            if isinstance(w, scrolledtext.ScrolledText):
                w.config(bg="#ffffff", fg="#000000", insertbackground="#000000")
            elif isinstance(w, tk.Label):
                w.config(bg="#f0f0f0", fg="#000000")
            elif isinstance(w, tk.LabelFrame):
                w.config(bg="#f0f0f0", fg="#000000")
            elif isinstance(w, tk.Radiobutton):
                w.config(bg="#f0f0f0", fg="#000000", selectcolor="#f0f0f0")
            elif isinstance(w, tk.Frame):
                w.config(bg="#f0f0f0")
                
        modo_oscuro.set(False)
    else:
        root.config(bg="#2d2d2d")
        toolbar.config(bg="#1e1e1e")
        titulo_label.config(bg="#2d2d2d", fg="#ffffff")
        entry_url.config(bg="#3d3d3d", fg="#ffffff", insertbackground="#ffffff")
        btn_descargar.config(bg="#388E3C", fg="#ffffff")
        
        for w in widgets_botones_toolbar:
            w.config(bg="#1e1e1e", fg="#ffffff")
            
        for w in widgets_texto:
            if isinstance(w, scrolledtext.ScrolledText):
                w.config(bg="#1e1e1e", fg="#ffffff", insertbackground="#ffffff")
            elif isinstance(w, tk.Label):
                w.config(bg="#2d2d2d", fg="#ffffff")
            elif isinstance(w, tk.LabelFrame):
                w.config(bg="#2d2d2d", fg="#ffffff")
            elif isinstance(w, tk.Radiobutton):
                w.config(bg="#2d2d2d", fg="#ffffff", selectcolor="#2d2d2d")
            elif isinstance(w, tk.Frame):
                w.config(bg="#2d2d2d")
                
        modo_oscuro.set(True)

def construir_interfaz(root):
    root.title("Descargador Multimedia a MP3")
    root.geometry("600x700")
    root.minsize(550, 600)
    
    servicio_actual = tk.StringVar(value="youtube")
    modo_oscuro = tk.BooleanVar(value=False)
    
    # ==========================================
    # BARRA DE HERRAMIENTAS (Toolbar) SUPERIOR
    # ==========================================
    toolbar = tk.Frame(root, bd=1, relief=tk.RAISED, bg="#e0e0e0")
    toolbar.pack(side=tk.TOP, fill=tk.X)
    
    btn_carpeta = tk.Button(toolbar, text="📁 Abrir Ruta", font=("Arial", 9), relief=tk.FLAT, bg="#e0e0e0", fg="#000000", command=abrir_carpeta_descargas)
    btn_carpeta.pack(side=tk.LEFT, padx=2, pady=2)
    
    separador1 = tk.Frame(toolbar, width=2, bg="gray")
    separador1.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=2)
    
    btn_cambiar_ruta = tk.Button(toolbar, text="⚙️ Cambiar Ruta", font=("Arial", 9), relief=tk.FLAT, bg="#e0e0e0", fg="#000000")
    btn_cambiar_ruta.pack(side=tk.LEFT, padx=2, pady=2)
    
    separador2 = tk.Frame(toolbar, width=2, bg="gray")
    separador2.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=2)
    
    btn_limpiar = tk.Button(toolbar, text="🗑️ Limpiar Consola", font=("Arial", 9), relief=tk.FLAT, bg="#e0e0e0", fg="#000000")
    btn_limpiar.pack(side=tk.LEFT, padx=2, pady=2)
    
    separador3 = tk.Frame(toolbar, width=2, bg="gray")
    separador3.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=2)
    
    btn_theme_mode = tk.Button(toolbar, text="🌓 Tema Oscuro/Claro", font=("Arial", 9), relief=tk.FLAT, bg="#e0e0e0", fg="#000000")
    btn_theme_mode.pack(side=tk.LEFT, padx=2, pady=2)
    # ==========================================

    # ==========================================
    # CONTENEDOR VISTA PRINCIPAL (Usando GRID)
    # ==========================================
    frame_principal = tk.Frame(root)
    frame_principal.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

    # Configurar filas y columnas del grid principal
    frame_principal.rowconfigure(4, weight=1) # La consola se expande verticalmente
    frame_principal.columnconfigure(0, weight=1)

    # Fila 0: Título
    titulo_label = tk.Label(frame_principal, text="Descargador de YouTube a MP3", font=("Arial", 14, "bold"))
    titulo_label.grid(row=0, column=0, pady=(0, 10))
    
    # Fila 1: Botones de servicio (YouTube / Spotify)
    frame_botones_superiores = tk.Frame(frame_principal)
    frame_botones_superiores.grid(row=1, column=0, pady=5)
    
    btn_youtube = tk.Button(frame_botones_superiores, text="YouTube", font=("Arial", 10, "bold"), bg="#FF0000", fg="white", padx=15, pady=5, relief=tk.SUNKEN, bd=4)
    btn_youtube.pack(side=tk.LEFT, padx=5)
    
    btn_spotify = tk.Button(frame_botones_superiores, text="Spotify", font=("Arial", 10, "bold"), bg="#1DB954", fg="white", padx=15, pady=5, relief=tk.RAISED, bd=2)
    btn_spotify.pack(side=tk.LEFT, padx=5)
    
    # Fila 2: Opciones de descarga (Radiobuttons)
    frame_opciones = tk.LabelFrame(frame_principal, text=" Opciones de Descarga ", font=("Arial", 10, "bold"))
    frame_opciones.grid(row=2, column=0, sticky="ew", pady=8)
    
    opcion = tk.IntVar(value=1)
    
    rb1 = tk.Radiobutton(frame_opciones, text="1. Descargar SOLO la canción (ignora la playlist)", variable=opcion, value=1, font=("Arial", 10))
    rb1.pack(anchor=tk.W, padx=10, pady=4)
    
    rb2 = tk.Radiobutton(frame_opciones, text="2. Descargar TODA la playlist", variable=opcion, value=2, font=("Arial", 10))
    rb2.pack(anchor=tk.W, padx=10, pady=4)
    
    btn_youtube.config(command=lambda: cambiar_servicio("youtube", titulo_label, rb1, rb2, btn_youtube, btn_spotify, servicio_actual))
    btn_spotify.config(command=lambda: cambiar_servicio("spotify", titulo_label, rb1, rb2, btn_youtube, btn_spotify, servicio_actual))
    
    # Fila 3: Campo de URL
    frame_url = tk.Frame(frame_principal)
    frame_url.grid(row=3, column=0, sticky="ew", pady=5)
    
    lbl_url = tk.Label(frame_url, text="URL del contenido (Video, Canción o Playlist):", font=("Arial", 10))
    lbl_url.pack(anchor=tk.W)
    
    entry_url = tk.Entry(frame_url, font=("Arial", 10))
    entry_url.pack(fill=tk.X, pady=3)
    
    # Fila 4: Consola de texto (expandible)
    frame_consola = tk.Frame(frame_principal)
    frame_consola.grid(row=4, column=0, sticky="nsew", pady=5)
    
    txt_consola = scrolledtext.ScrolledText(frame_consola, wrap=tk.WORD, font=("Consolas", 9), bg="#1e1e1e", fg="#ffffff", height=6)
    txt_consola.pack(fill=tk.BOTH, expand=True)
    
    btn_limpiar.config(command=lambda: limpiar_consola(txt_consola))

    # Fila 5: Botón Iniciar Descarga (siempre fijo y visible al fondo)
    btn_descargar = tk.Button(frame_principal, text="Iniciar Descarga", font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", padx=15, pady=8)
    btn_descargar.grid(row=5, column=0, pady=10)

    # Asignar comando de descarga
    btn_descargar.config(command=lambda: iniciar_hilo(entry_url, opcion, servicio_actual, txt_consola, btn_descargar))

    # ==========================================
    # CONTENEDOR VISTA CAMBIAR RUTA
    # ==========================================
    frame_ruta = tk.Frame(root)
    
    lbl_ruta_titulo = tk.Label(frame_ruta, text="Configuración de Ruta de Descarga", font=("Arial", 14, "bold"))
    lbl_ruta_titulo.pack(pady=20)
    
    lbl_instruccion = tk.Label(frame_ruta, text="Introduce la nueva ruta absoluta de la carpeta:", font=("Arial", 10))
    lbl_instruccion.pack(anchor=tk.W, padx=30, pady=5)
    
    entry_nueva_ruta = tk.Entry(frame_ruta, font=("Arial", 10))
    entry_nueva_ruta.pack(fill=tk.X, padx=30, pady=5)
    
    btn_establecer = tk.Button(frame_ruta, text="Establecer", font=("Arial", 10, "bold"), bg="#2196F3", fg="white", padx=15, pady=5,
                               command=lambda: guardar_nueva_ruta(entry_nueva_ruta))
    btn_establecer.pack(pady=10)

    btn_volver = tk.Button(frame_ruta, text="Volver al Descargador", font=("Arial", 10), padx=10, pady=5,
                           command=lambda: cambiar_vista("principal"))
    btn_volver.pack(pady=5)

    def cambiar_vista(vista):
        if vista == "ruta":
            frame_principal.pack_forget()
            frame_ruta.pack(fill=tk.BOTH, expand=True)
        else:
            frame_ruta.pack_forget()
            frame_principal.pack(fill=tk.BOTH, expand=True)

    btn_cambiar_ruta.config(command=lambda: cambiar_vista("ruta"))

    # Agrupar contenedores y elementos para el tema
    widgets_texto = [root, frame_principal, frame_botones_superiores, lbl_url, frame_url, frame_opciones, rb1, rb2, frame_consola, txt_consola, frame_ruta, lbl_ruta_titulo, lbl_instruccion]
    widgets_botones_toolbar = [btn_carpeta, btn_cambiar_ruta, btn_limpiar, btn_theme_mode]

    btn_theme_mode.config(command=lambda: alternar_tema(root, toolbar, titulo_label, entry_url, btn_descargar, widgets_texto, widgets_botones_toolbar, modo_oscuro))

    # Aplicar modo oscuro por defecto al iniciar
    alternar_tema(root, toolbar, titulo_label, entry_url, btn_descargar, widgets_texto, widgets_botones_toolbar, modo_oscuro)