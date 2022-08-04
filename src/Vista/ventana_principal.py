import tkinter as Tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from numpy import size

class ventanaPrincipal():
    def __init__(self, master):
        self.frame = Tk.Frame(master)
        self.frame.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)

        #self.fig = Figure(figsize=(7.5, 4), dpi=80)  # type: ignore
        #self.ax0 = self.fig.add_axes((0.05, .05, .90, .90),
        #                             facecolor=(.75, .75, .75),
        #                             frameon=False)

        self.panelLateral = PanelLateral(master)

        #self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        #self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        #self.canvas.draw()

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

        self.botonTransferir = Tk.Button(self.frame,state='disabled',text='Transferir')
        self.botonTransferir.pack(side='top', fill=Tk.BOTH)

        self.textoTransferir = Tk.Label(self.frame, text='Estado')
        self.textoTransferir.pack(side='top', fill=Tk.BOTH)
    
    def desactivarBotonTransferir(self):
        self.botonTransferir['state'] = Tk.DISABLED

    def activarBotonTransferir(self):
        self.botonTransferir['state'] = Tk.NORMAL

    def cambiarEstadoBotonTransferir(self):
        if (self.botonTransferir['state'] == Tk.NORMAL):
            self.botonTransferir['state'] = Tk.DISABLED
        else:
            self.botonTransferir['state'] = Tk.NORMAL
    
    def setTextoTransferir(self, texto:str):
        self.textoTransferir.config( text=texto )

    def setTextoUSB(self, texto:str):
        self.textoUSB.config( text=texto )
    
    def setTextoWBFS(self, texto:str): 
        self.textoWBFS.config( text=texto )



if __name__ == '__main__':
    pass
