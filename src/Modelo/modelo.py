import subprocess
import os
from pathlib import Path
from tkinter.filedialog import askdirectory, askopenfilename
from .descargar_portadas.descargar import descargar2D, descargar3D, descargarCD, descargarCoverFull



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
    
    def descargarImagenes(self, dirUSB: str = '', dirISO: str = '/home/songoku/ROMS Juegos/Wii/wbfs/Tetris Party Deluxe [STEETR].wbfs'):
        dirISO = Path(dirISO).__str__()
        dirUSB = Path(dirUSB).__str__()
        ID = subprocess.getoutput(f'wit ID "{dirISO}"')
        descargar3D(ID,dirUSB)
        descargar2D(ID,dirUSB)
        descargarCD(ID,dirUSB)
        descargarCoverFull(ID,dirUSB)
        print("Portadas descargadas")

    def pasarUSB(self, dirUSB: str, dirISO: str):
        dirISO = Path(dirISO).__str__()
        dirUSB = Path(dirUSB).joinpath('wbfs', '%Y/%+').__str__()
        comando = ['wit', 'copy', dirISO, '--split', '-B', '-P', '-D', dirUSB]  # %1uT/%+']
        subprocess.run(args=comando)

if __name__ == '__main__':
    #descargarCD()
    comando = ['wit', 'ID', '/home/songoku/ROMS Juegos/Wii/wbfs/Tetris Party Deluxe [STEETR].wbfs']  # %1uT/%+']
    model = modelo()
    model.descargarImagenes()
    #print(subprocess.getoutput(' '.join(comando)))
