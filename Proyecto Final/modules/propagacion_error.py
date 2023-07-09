'''
Tema: Métodos Numéricos
Grupo 6
Integrantes:

•	Kevin Josue Amaguaña Rivadeneira
•	Priscila Veronica Chisag Pillajo
•	Andy Ricardo Galarza Morales
•	Stiven Anthony Pilca Sánchez

Carrera: Ingeniería en Sistemas de la información
Paralelo: SI4 - 002
'''

import tkinter as tk
import matplotlib.figure
import numpy as np
import functions.events as event
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from static import style
from functions import funcion_propagacion as propagacion
from validation import validacion


class PropErrores(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BG)
        self.controller = controller

        self.init_widgets()

    def validar_campo(self):
        if validacion.validate_number_float(self.exponente.get()) is True and int(self.exponente.get()) > 250:
            self.texto_alerta_exponente.set("")
            self.calcular()
        else:
            self.texto_alerta_exponente.set("Ingrese un valor mayor a 250")

    def calcular(self):
        self.respuesta = propagacion.propagacion_errores(
            int(self.exponente.get()))
        self.valor_respuesta.set(self.respuesta)
        self.graficar()

    def graficar(self):
        self.ax.clear()
        x = np.linspace(int(self.exponente.get())-5,
                        int(self.exponente.get())+5)
        self.ax.scatter(int(self.exponente.get()), self.respuesta, label="Respuesta", c=style.COLOR_BLANCO, zorder=10)
        self.ax.plot(x, propagacion.e(x), label="Función",
                     c=style.COLOR_MAGENTA_CLARO, zorder=5)
        self.ax.grid(alpha=0.2, lw=1.75, ls="--")
        self.ax.annotate("[{}]".format(self.respuesta), xy=(self.respuesta+0.25, self.respuesta+2), c=style.COLOR_BLANCO)
        self.ax.legend(loc="upper left", facecolor=style.BG,
                       edgecolor=style.BG, labelcolor=style.COLOR_BLANCO)
        self.canvas_figura.draw()

    def init_widgets(self):
        tk.Label(self,
                 text="Propagación de Errores",
                 **style.STYLE_TITTLE,
                 ).pack(side=tk.TOP, fill=tk.BOTH, pady=30)

        input_frame = tk.Frame(self, background=style.BG)
        input_frame.columnconfigure(0, weight=1)
        input_frame.columnconfigure(1, weight=2)
        input_frame.columnconfigure(2, weight=1)
        input_frame.pack(side=tk.TOP, fill=tk.BOTH)

        # label ecuacion
        tk.Label(input_frame,
                 text="Ecuación",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=0)

        # label exponente
        tk.Label(input_frame,
                 text="Exponente (x)",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=1, column=0)

        # label respuesta
        tk.Label(input_frame,
                 text="Respuesta",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=2, column=0)

        # label ecuacion usada
        tk.Label(input_frame,
                 text="(e^x)/(e^x)-1",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=1, columnspan=2, pady=10, padx=(20, 0))

        # entry exponente
        borde_entry_1 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_1.grid(row=1, column=1, columnspan=2,
                           pady=10, padx=(20, 0), sticky=tk.EW)

        self.exponente = tk.StringVar()
        tk.Entry(borde_entry_1,
                 textvariable=self.exponente,
                 **style.STYLE_ENTRY,
                 ).pack(side=tk.TOP, expand=True)

        canvas_linea_1 = tk.Canvas(
            borde_entry_1, **style.STYLE_CANVAS, width=250)
        canvas_linea_1.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_1.create_line(0, 0, 250, 0, **style.STYLE_CANVAS_LINE)

        # label alerta exponente
        self.texto_alerta_exponente = tk.StringVar()
        tk.Label(borde_entry_1,
                 textvariable=self.texto_alerta_exponente,
                 **style.STYLE_WARNING
                 ).pack()

        # entry desactivado respuesta
        borde_entry_2 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_2.grid(row=2, column=1, columnspan=2,
                           pady=10, padx=(20, 0), sticky=tk.EW)

        self.valor_respuesta = tk.StringVar()
        tk.Entry(borde_entry_2,
                 textvariable=self.valor_respuesta,
                 **style.STYLE_ENTRY_DES,
                 ).pack(side=tk.TOP, expand=True)

        canvas_linea_2 = tk.Canvas(
            borde_entry_2, **style.STYLE_CANVAS, width=250)
        canvas_linea_2.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_2.create_line(0, 0, 250, 0, **style.STYLE_CANVAS_LINE)

        # boton para calcular
        borde_1 = tk.LabelFrame(input_frame, **style.STYLE_BUTTON_BORDER)
        borde_1.grid(row=0, rowspan=3, column=3, pady="30", padx="20")

        boton_calculo = tk.Button(borde_1,
                                  text="Calcular",
                                  **style.STYLE_BUTTON,
                                  command=self.validar_campo
                                  )
        boton_calculo.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        boton_calculo.bind('<Enter>', event.on_enter)
        boton_calculo.bind('<Leave>', event.on_leave)

        output_frame = tk.Frame(self, background=style.BG)
        output_frame.pack(side=tk.TOP, fill=tk.BOTH,
                          expand=True, padx=10, pady=10)

        # label titulo de la gráfica
        tk.Label(output_frame,
                 text="Función e^x/(e^x)-1",
                 **style.STYLE_SUBTITTLE,
                 ).pack(side=tk.TOP, fill=tk.X, expand=True)

        self.fig = matplotlib.figure.Figure(facecolor=style.BG)
        self.ax = self.fig.add_subplot(facecolor=style.BG)

        self.ax.spines['bottom'].set_color(style.COLOR_AQUA)
        self.ax.spines['bottom'].set_linewidth(2)
        self.ax.spines['left'].set_color(style.COLOR_AQUA)
        self.ax.spines['left'].set_linewidth(2)
        self.ax.spines['right'].set_color(style.COLOR_AQUA)
        self.ax.spines['right'].set_linewidth(2)
        self.ax.spines['top'].set_color(style.COLOR_AQUA)
        self.ax.spines['top'].set_linewidth(2)

        self.ax.tick_params(axis='both', colors=style.COLOR_AQUA,
                            labelsize=10, size=7, width=2)

        self.canvas_figura = FigureCanvasTkAgg(self.fig, master=output_frame)
        self.canvas_figura.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH,
                                                expand=True)
