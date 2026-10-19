[Setup]
AppName=FreeDownloader
AppVersion=1.0
DefaultDirName={autopf}\FreeDownloader
DefaultGroupName=FreeDownloader
OutputDir=output
OutputBaseFilename=FreeDownloaderInstaller
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Files]
; Archivo principal compilado con PyInstaller
Source: "..\dist\DescargadorMultimedia.exe"; DestDir: "{app}"; DestName: "FreeDownloader.exe"; Flags: ignoreversion

[Icons]
Name: "{group}\FreeDownloader"; Filename: "{app}\FreeDownloader.exe"
Name: "{autodesktop}\FreeDownloader"; Filename: "{app}\FreeDownloader.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Crear un acceso directo en el &escritorio"; GroupDescription: "Tareas adicionales:"; Flags: unchecked

[Run]
; Instalar yt-dlp y spotdl automáticamente usando pip al finalizar la instalación
Filename: "pip"; Parameters: "install --upgrade yt-dlp spotdl"; Flags: shellexec waituntilterminated; Description: "Instalando dependencias necesarias (yt-dlp y spotdl)..."; StatusMsg: "Actualizando e instalando motores de descarga..."