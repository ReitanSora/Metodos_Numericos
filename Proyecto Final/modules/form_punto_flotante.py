'''
Tema: Métodos Numéricos
#Grupo #
#Integrantes:

•	Kevin Josue Amaguaña Rivadeneira
•	Priscila Veronica Chisag Pillajo
•	Andy RIcardo Galarza Morales
•	Stiven Anthony Pilca Sánchez

#Carrera: Ingeniería en Sistemas de la información
#Paralelo: SI4 - 002
'''

import tkinter as tk
from tkinter import messagebox
import random as r
from static import style
from functions import ordenamiento

class PuntoFlotante(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BG)
        self.controller = controller
        self.init_widgets()

    def move_to_0(self):
        self.matriz.clear()
        self.count = 0
        self.auxiliar_numeros_ingresados = ""
        self.numeros_ingresados.set("")
        self.resultado.set("")
        self.controller.show_frame(Home)

    def aleatorio(self):
        aux = r.randint(-1000, 1000)
        self.matriz.insert(self.count, aux)
        self.count += 1
        self.auxiliar_numeros_ingresados = "{} , {}".format(
            self.auxiliar_numeros_ingresados, aux) if self.count > 1 else " {}".format(aux)
        self.numeros_ingresados.set(self.auxiliar_numeros_ingresados)

    def ingreso(self):
        try:
            aux = int(self.dato.get())
            self.matriz.insert(self.count, aux)
            self.count += 1
            self.auxiliar_numeros_ingresados = "{} , {}".format(
                self.auxiliar_numeros_ingresados, aux) if self.count > 1 else " {}".format(aux)
            self.numeros_ingresados.set(self.auxiliar_numeros_ingresados)
        except ValueError:
            self.entry.insert(0, "")
            messagebox.showerror(
                "Error de valor", "Solamente puede ingresar números")

    def eliminar(self):
        try:
            self.matriz.pop(self.count-1)
            self.count -= 1
            self.auxiliar_numeros_ingresados = ""
            for posicion in range(self.count):
                self.auxiliar_numeros_ingresados = "{} , {}".format(
                    self.auxiliar_numeros_ingresados, self.matriz[posicion]) if self.auxiliar_numeros_ingresados != "" else " {}".format(self.matriz[posicion])

            self.numeros_ingresados.set(self.auxiliar_numeros_ingresados)

        except IndexError:
            messagebox.showwarning(
                "Error de indice", "No ha ingresado ningún número")

    def calculo(self):
        ordenamiento.burbuja(self.matriz)
        resultado = str(self.matriz)[1:len(str(self.matriz))-1]
        self.resultado.set(str(resultado).replace(",", ", "))

    def init_widgets(self):
        tk.Label(
            self,
            text="Punto Flotante",
            **style.STYLE_TITTLE,
        ).pack(side=tk.TOP, fill=tk.BOTH, pady=30)

        optionsFrame = tk.Frame(self, background=style.BG)
        optionsFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True,)

        tk.Label(
            optionsFrame,
            text="Ingrese un número",
            # desempaquetado del diccionario STYLE
            **style.STYLE_SUBTITTLE,
        ).pack(side=tk.LEFT, expand=True,)

        self.dato = tk.StringVar()

        self.entry = tk.Entry(
            optionsFrame,
            textvariable=self.dato,
            **style.STYLE_ENTRY,
        )
        self.entry.pack(side=tk.LEFT, expand=True,)

        # botones pertenecientes al ingreso de numeros
        # Primer boton, boton para ingresar numeros
        borde_1 = tk.LabelFrame(optionsFrame, **style.STYLE_BUTTON_BORDER)
        borde_1.pack(side=tk.TOP, expand=True)

        boton_1 = tk.Button(
            borde_1,
            text="Ingresar",
            command=self.ingreso,
            **style.STYLE_BUTTON,
        )
        boton_1.pack(expand=True, fill=tk.BOTH)

        boton_1.bind('<Enter>', on_enter)
        boton_1.bind('<Leave>', on_leave)

        # Segundo boton, boton para ingresar numeros aleatorios
        borde_2 = tk.LabelFrame(optionsFrame, **style.STYLE_BUTTON_BORDER)
        borde_2.pack(side=tk.TOP, expand=True, padx=50)

        boton_2 = tk.Button(
            borde_2,
            text="Aleatorio",
            command=self.aleatorio,
            **style.STYLE_BUTTON,
        )
        boton_2.pack(expand=True, fill=tk.BOTH)

        boton_2.bind('<Enter>', on_enter)
        boton_2.bind('<Leave>', on_leave)

        # tercer boton, boton para eliminar un numero
        borde_3 = tk.LabelFrame(optionsFrame, **style.STYLE_BUTTON_BORDER)
        borde_3.pack(side=tk.TOP, expand=True)

        boton_3 = tk.Button(
            borde_3,
            text="Eliminar",
            command=self.eliminar,
            **style.STYLE_BUTTON,
        )
        boton_3.pack(expand=True, fill=tk.BOTH)

        boton_3.bind('<Enter>', on_enter)
        boton_3.bind('<Leave>', on_leave)

        # frame para visualizar la informacion ingresada y el resultado
        visualFrame = tk.Frame(self, background=style.BG)
        visualFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True,
                         )

        tk.Label(
            visualFrame,
            text="Numeros ingresados",
            # desempaquetado del diccionario STYLE
            **style.STYLE_SUBTITTLE,
        ).pack(side=tk.TOP, pady=20, expand=True,)

        self.numeros_ingresados = tk.StringVar()
        self.entry_1 = tk.Entry(
            visualFrame,
            textvariable=self.numeros_ingresados,
            **style.STYLE_ENTRY_DES
        )
        self.entry_1.pack(side=tk.TOP, expand=True,)

        # para mostrar el resultado final
        tk.Label(
            visualFrame,
            text="Resultado",
            # desempaquetado del diccionario STYLE
            **style.STYLE_SUBTITTLE,
        ).pack(side=tk.TOP, pady=20, expand=True,)

        self.resultado = tk.StringVar()
        self.entry_2 = tk.Entry(
            visualFrame,
            textvariable=self.resultado,
            **style.STYLE_ENTRY_DES
        )
        self.entry_2.pack(side=tk.TOP, expand=True,)

        # Cuarto boton, boton para mostrar el resultado
        borde_4 = tk.LabelFrame(self, **style.STYLE_BUTTON_BORDER)
        borde_4.pack(side=tk.LEFT, expand=True, pady=50)

        boton_4 = tk.Button(
            borde_4,
            text="Ordenar",
            command=self.calculo,
            **style.STYLE_BUTTON
        )
        boton_4.pack(expand=True, fill=tk.BOTH)

        boton_4.bind('<Enter>', on_enter)
        boton_4.bind('<Leave>', on_leave)

        # Quinto boton, boton para regresar al menu principal
        borde_5 = tk.LabelFrame(self, **style.STYLE_BUTTON_BORDER)
        borde_5.pack(side=tk.LEFT, expand=True, padx=50)

        boton_5 = tk.Button(
            borde_5,
            text="Regresar",
            command=self.move_to_0,
            **style.STYLE_BUTTON
        )
        boton_5.pack(expand=True, fill=tk.BOTH)

        boton_5.bind('<Enter>', on_enter)
        boton_5.bind('<Leave>', on_leave)