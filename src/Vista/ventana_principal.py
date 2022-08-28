import tkinter as Tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from numpy import size
from tkinter import TclError

class ventanaPrincipal():
    def __init__(self, master):
        self.frame = Tk.Frame(master)

        # vvv Ocultar archivos ocultos
        try:
            self.frame.tk.call('tk_getOpenFile', '-foobarbaz')
        except TclError:
            pass
        self.frame.tk.call('set', '::tk::dialog::file::showHiddenVar', '0')
        self.frame.tk.call('set', '::tk::dialog::file::showHiddenBtn', '1')
        # *** Ocultar archivos ocultos

        self.frame.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
        self.panelLateral = PanelLateral(master)

class PanelLateral():
    def __init__(self, root):
        self.frame = Tk.Frame(root)
        self.frame.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)

        self.textoUSB = Tk.Label(self.frame, text= 'USB')
        self.textoUSB.pack(side='top', fill=Tk.BOTH)
        self.botonUSB = Tk.Button(self.frame, text="Selecionar USB")
        self.botonUSB.pack(side="top", fill=Tk.BOTH)

        self.textoWBFS = Tk.Label(self.frame, text='WBFS')
        self.textoWBFS.pack(side='top', fill=Tk.BOTH)
        self.botonWBFS = Tk.Button(self.frame, text="Seleccionar Juego")
        self.botonWBFS.pack(side="top", fill=Tk.BOTH)

        self.botonTransferir = Tk.Button(self.frame,state='disabled',text='Transferir Juego')
        self.botonTransferir.pack(side='top', fill=Tk.BOTH)

        self.botonDescargarImagen = Tk.Button(self.frame, state='disabled', text='Transferir Imagen')
        self.botonDescargarImagen.pack(side='top', fill=Tk.BOTH)

        self.textoEstado = Tk.Label(self.frame, text='Estado')
        self.textoEstado.pack(side='top', fill=Tk.BOTH)
    
    def desactivarBotonTransferir(self):
        self.botonTransferir['state'] = Tk.DISABLED

    def activarBotonTransferir(self):
        self.botonTransferir['state'] = Tk.NORMAL
    
    def desactivarBotonDescargar(self):
        self.botonDescargarImagen['state'] = Tk.DISABLED

    def activarBotonDescargar(self):
        self.botonDescargarImagen['state'] = Tk.NORMAL

    def cambiarEstadoBotonTransferir(self):
        if (self.botonTransferir['state'] == Tk.NORMAL):
            self.botonTransferir['state'] = Tk.DISABLED
        else:
            self.botonTransferir['state'] = Tk.NORMAL
    
    def setTextoEstado(self, texto:str):
        self.textoEstado.config( text=texto )

    def setTextoUSB(self, texto:str):
        self.textoUSB.config( text=texto )
    
    def setTextoWBFS(self, texto:str): 
        self.textoWBFS.config( text=texto )



if __name__ == '__main__':
    pass
