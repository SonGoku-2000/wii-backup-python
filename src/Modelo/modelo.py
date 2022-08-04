import subprocess
import os
from pathlib import Path
from tkinter.filedialog import askdirectory, askopenfilename


class modelo():
    def __init__(self) -> None:
        self.dirUsb = ''
        self.dirWBFS = ''
    
    def selectUsb(self):
        self.dirUsb = self.__selectorCarpeta('Seleccione la carpeta raiz de su usb',self.dirUsb)
    
    def comprobarDisponible(self):
        return self.dirUsb != '' and self.dirWBFS != ''
            
    def __selectorCarpeta(self,titulo: str = '', dirBase: str = 'C://', usb: bool = True):
        if os.name == 'posix':  # Saber si es linux
            if dirBase == 'C://':
                dirBase = Path.home().resolve().__str__()
            if usb:
                dirBase = Path('/media').joinpath(Path.home().resolve().name).__str__()
        if os.name == 'nt':  # Saber si es windows
            pass
        fileName = askdirectory(title=titulo, initialdir=dirBase)
        return fileName
    
    def selectWBFS(self):
        self.dirWBFS = self.__selectorWBFS()

    def __selectorWBFS(self):
        archivo = askopenfilename(title='Seleccione un juego',
                                  filetypes=(('Juegos', ('*.iso', '*.wbfs')),
                                             ('All', '*.*')))
        return archivo

    def pasarUSB(self, dirUSB: str, dirWBFS: str):
        dirWBFS = Path(dirWBFS).__str__()
        dirUSB = Path(dirUSB).joinpath('wbfs', '%Y/%+').__str__()
        comando = ['wit', 'copy', dirWBFS, '--split', '-D', dirUSB]  # %1uT/%+']
        subprocess.run(args=comando)

