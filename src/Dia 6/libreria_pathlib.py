from pathlib import Path, PureWindowsPath

carpeta = Path('C:\\Users\\Hbiondini\\Desktop\\lalala.txt')
print(carpeta.read_text())
print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)

if not carpeta.exists():
    print('Este archivo no existe')
else:
    print('Este archivo existe')

ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)