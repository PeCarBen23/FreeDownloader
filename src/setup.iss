[Setup]
AppName=Descargador Multimedia a MP3
AppVersion=1.0
DefaultDirName={autopf}\DescargadorMultimedia
DefaultGroupName=DescargadorMultimedia
OutputDir=output
OutputBaseFilename=Instalador_DescargadorMultimedia
Compression=lzma
SolidCompression=yes
SetupIconFile=

[Files]
; Aquí indicas dónde se guardará el ejecutable compilado por PyInstaller
Source: "dist\DescargadorMultimedia.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Descargador Multimedia"; Filename: "{app}\DescargadorMultimedia.exe"
Name: "{autodesktop}\Descargador Multimedia"; Filename: "{app}\DescargadorMultimedia.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Crear un acceso directo en el &escritorio"; GroupDescription: "Adicionales:"