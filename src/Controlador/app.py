import tkinter as Tk

from pathlib import Path
from src.Modelo.modelo import modelo
from src.Vista.ventana_principal import ventanaPrincipal


class Controller():
    def __init__(self):
        self.root = Tk.Tk()

        self.modelo = modelo()
        self.view = ventanaPrincipal(self.root)
        self.view.panelLateral.botonUSB.configure(command=self.seleccionarUSB)
        self.view.panelLateral.botonWBFS.configure(
            command=self.seleccionarWBFS)
        self.view.panelLateral.botonTransferir.configure(
            command=self.transferirISO)
        self.view.panelLateral.botonDescargarImagen.configure(
            command=self.descargarImagenes)

    def run(self):
        self.root.title("Python Wii Backup")
        self.root.deiconify()
        self.root.mainloop()

    def transferirISO(self):
        iso = Path(self.modelo.dirWBFS).name
        self.view.panelLateral.setTextoEstado(f'Transfiriendo {iso} ...')
        self.root.update()
        self.modelo.pasarUSB(dirUSB=self.modelo.dirUsb,
                             dirISO=self.modelo.dirWBFS)
        self.view.panelLateral.setTextoEstado(f'{iso} Transferido')
        self.root.update()

    def descargarImagenes(self):
        iso = Path(self.modelo.dirWBFS).name
        self.view.panelLateral.setTextoEstado(
            f'Descargando portadas {iso} ...')
        self.root.update()
        self.modelo.descargarImagenes(
            dirUSB=self.modelo.dirUsb, dirISO=self.modelo.dirWBFS)
        self.view.panelLateral.setTextoEstado(f'Portadas descargadas')
        self.root.update()

    def comprobarDisponible(self):
        if self.modelo.comprobarDisponible():
            self.view.panelLateral.activarBotonTransferir()
            self.view.panelLateral.activarBotonDescargar()
        else:
            self.view.panelLateral.desactivarBotonTransferir()
            self.view.panelLateral.desactivarBotonDescargar()

    def seleccionarUSB(self):
        self.modelo.selectUsb()
        self.comprobarDisponible()
        self.view.panelLateral.setTextoUSB(f'USB: {self.modelo.dirUsb}')
        self.root.mainloop()

    def seleccionarWBFS(self):
        self.modelo.selectWBFS()
        self.comprobarDisponible()
        self.view.panelLateral.setTextoWBFS(f'WBFS: {self.modelo.dirWBFS}')
        self.root.mainloop()
