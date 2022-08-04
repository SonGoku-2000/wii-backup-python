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
        self.view.panelLateral.botonTransferir.bind("<Button>", self.transferirWBFS)

    def run(self):
        self.root.title("Tkinter MVC example")
        self.root.deiconify()
        self.root.mainloop()

    #def clear(self, event):
    #    self.view.ax0.clear()
     #   self.view.fig.canvas.draw()
    
    def transferirWBFS(self, event):
        wbfs = Path(self.modelo.dirWBFS).name
        self.view.panelLateral.setTextoTransferir(f'Transfiriendo {wbfs} ...')
        self.root.update()
        self.modelo.pasarUSB(dirUSB = self.modelo.dirUsb,
                             dirWBFS=self.modelo.dirWBFS)
        self.view.panelLateral.setTextoTransferir(f'{wbfs} Transferido')
        self.root.update()

    def comprobarDisponible(self):
        if self.modelo.comprobarDisponible():
            self.view.panelLateral.activarBotonTransferir()
        else:
            self.view.panelLateral.desactivarBotonTransferir()

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