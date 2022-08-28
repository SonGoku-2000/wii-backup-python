import tkinter as Tk

from pathlib import Path
from src.Modelo.modelo import modelo
from src.Vista.ventana_principal import ventanaPrincipal



class Controller():
    def __init__(self):
        self.root = Tk.Tk()
        
        self.modelo = modelo()
        self.view = ventanaPrincipal(self.root)
        self.view.panelLateral.botonUSB.bind("<Button>", self.seleccionarUSB)
        self.view.panelLateral.botonWBFS.bind("<Button>", self.seleccionarWBFS)
        self.view.panelLateral.botonTransferir.bind("<Button>", self.transferirISO)
        self.view.panelLateral.botonDescargarImagen.bind("<Button>", self.descargarImagenes)

    def run(self):
        self.root.title("Tkinter MVC example")
        self.root.deiconify()
        self.root.mainloop()
    
    def transferirISO(self, event):
        iso = Path(self.modelo.dirWBFS).name
        self.view.panelLateral.setTextoEstado(f'Transfiriendo {iso} ...')
        self.root.update()
        self.modelo.pasarUSB(dirUSB = self.modelo.dirUsb, dirISO = self.modelo.dirWBFS)
        self.view.panelLateral.setTextoEstado(f'{iso} Transferido')
        self.root.update()
    
    def descargarImagenes(self, event):
        iso = Path(self.modelo.dirWBFS).name
        self.view.panelLateral.setTextoEstado(f'Descargando portadas {iso} ...')
        self.root.update()
        self.modelo.descargarImagenes(dirUSB=self.modelo.dirUsb, dirISO=self.modelo.dirWBFS)
        self.view.panelLateral.setTextoEstado(f'Portadas descargadas')
        self.root.update()

    def comprobarDisponible(self):
        if self.modelo.comprobarDisponible():
            self.view.panelLateral.activarBotonTransferir()
            self.view.panelLateral.activarBotonDescargar()
        else:
            self.view.panelLateral.desactivarBotonTransferir()
            self.view.panelLateral.desactivarBotonDescargar()
            
    def seleccionarUSB(self, event):
        self.modelo.selectUsb()
        self.comprobarDisponible()
        self.view.panelLateral.setTextoUSB(f'USB: {self.modelo.dirUsb}')
        self.root.mainloop()
    
    def seleccionarWBFS(self, event):
        self.modelo.selectWBFS()
        self.comprobarDisponible()
        self.view.panelLateral.setTextoWBFS(f'WBFS: {self.modelo.dirWBFS}')
        self.root.mainloop()