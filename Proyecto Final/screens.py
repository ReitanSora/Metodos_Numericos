'''
Tema: Algoritmos de ordenamiento(iterativos y recursivos)
#Grupo #3
#Integrantes:
#- Stiven Pilca           CI: 1750450262
#- Tulcanza Juan          CI: 1755962485
#Carrera: Ingeniería en Sistemas de la información
#Paralelo: SI4 - 002
#Fecha de entrega: 21/06/2023
'''

import tkinter as tk
from tkinter import messagebox
import random as r
from static import style
from functions import ordenamiento

# from PIL import ImageTk, Image


def on_enter(e):
    e.widget.config(**style.STYLE_BUTTON_ENTER)


def on_leave(e):
    e.widget.config(**style.STYLE_BUTTON)


class Home(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BG, pady=50)
        self.controller = controller
        self.init_widgets()

    def move_to_1(self):
        self.controller.show_frame(Burbuja)

    def move_to_2(self):
        self.controller.show_frame(Insercion)

    def move_to_3(self):
        self.controller.show_frame(Seleccion)

    def move_to_4(self):
        self.controller.show_frame(Shellsort)

    def move_to_5(self):
        self.controller.show_frame(Mergesort)

    def move_to_6(self):
        self.controller.show_frame(Quicksort)

    def move_to_7(self):
        self.controller.show_frame(Heapsort)

    def move_to_8(self):
        self.controller.show_frame(ShellsortRecursivo)

    def init_widgets(self):

        tk.Label(
            self,
            text="Bienvenido al programa de\nAlgoritmos de ordenamiento",
            # desempaquetado del diccionario STYLE
            **style.STYLE_TITTLE,
        ).pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        optionsFrame = tk.Frame(self, background=style.BG, pady=0)
        optionsFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True,)

        tk.Label(
            optionsFrame,
            text="Algoritmos Iterativos",
            justify=tk.CENTER,
            **style.STYLE_SUBTITTLE
        ).pack(side=tk.TOP, fill=tk.X, expand=True, pady=20)

        # Primer boton
        borde_1 = tk.LabelFrame(optionsFrame, **style.STYLE_BUTTON_BORDER)
        borde_1.pack(side=tk.LEFT, expand=True,)

        boton_1 = tk.Button(
            borde_1,
            text="Burbuja",
            command=self.move_to_1,
            ** style.STYLE_BUTTON,
        )
        boton_1.pack(expand=True, fill=tk.BOTH)

        boton_1.bind('<Enter>', on_enter)
        boton_1.bind('<Leave>', on_leave)

        # Segundo boton
        borde_2 = tk.LabelFrame(optionsFrame, **style.STYLE_BUTTON_BORDER)
        borde_2.pack(side=tk.LEFT, expand=True,)

        boton_2 = tk.Button(
            borde_2,
            text="Insercion",
            command=self.move_to_2,
            ** style.STYLE_BUTTON,
        )
        boton_2.pack(expand=True, fill=tk.BOTH)

        boton_2.bind('<Enter>', on_enter)
        boton_2.bind('<Leave>', on_leave)

        # Tercer boton
        borde_3 = tk.LabelFrame(optionsFrame, **style.STYLE_BUTTON_BORDER)
        borde_3.pack(side=tk.LEFT, expand=True,)

        boton_3 = tk.Button(
            borde_3,
            text="Seleccion",
            command=self.move_to_3,
            ** style.STYLE_BUTTON,
        )
        boton_3.pack(expand=True, fill=tk.BOTH)

        boton_3.bind('<Enter>', on_enter)
        boton_3.bind('<Leave>', on_leave)

        # Cuanto boton
        borde_4 = tk.LabelFrame(optionsFrame, **style.STYLE_BUTTON_BORDER)
        borde_4.pack(side=tk.LEFT, expand=True,)

        boton_4 = tk.Button(
            borde_4,
            text="Shellsort",
            command=self.move_to_4,
            ** style.STYLE_BUTTON,
        )
        boton_4.pack(expand=True, fill=tk.BOTH)

        boton_4.bind('<Enter>', on_enter)
        boton_4.bind('<Leave>', on_leave)

        # Segundo subtitulo
        tk.Label(
            self,
            text="Algoritmos Recursivos",
            justify=tk.CENTER,
            ** style.STYLE_SUBTITTLE
        ).pack(side=tk.TOP, fill=tk.X, expand=True, pady=5)

        # Quinta opcion
        borde_5 = tk.LabelFrame(self, **style.STYLE_BUTTON_BORDER)
        borde_5.pack(side=tk.LEFT, expand=True,)

        boton_5 = tk.Button(
            borde_5,
            text="Mergesort",
            command=self.move_to_5,
            ** style.STYLE_BUTTON,
        )
        boton_5.pack(expand=True, fill=tk.BOTH)

        boton_5.bind('<Enter>', on_enter)
        boton_5.bind('<Leave>', on_leave)

        # Sexta opcion
        borde_6 = tk.LabelFrame(self, **style.STYLE_BUTTON_BORDER)
        borde_6.pack(side=tk.LEFT, expand=True,)

        boton_6 = tk.Button(
            borde_6,
            text="Quicksort",
            command=self.move_to_6,
            ** style.STYLE_BUTTON,
        )
        boton_6.pack(expand=True, fill=tk.BOTH)

        boton_6.bind('<Enter>', on_enter)
        boton_6.bind('<Leave>', on_leave)

         # Septimo boton
        borde_7 = tk.LabelFrame(self, **style.STYLE_BUTTON_BORDER)
        borde_7.pack(side=tk.LEFT, expand=True)

        boton_7 = tk.Button(
            borde_7,
            text="Heapsort",
            command=self.move_to_7,
            ** style.STYLE_BUTTON,
        )
        boton_7.pack(expand=True, fill=tk.BOTH)

        boton_7.bind('<Enter>', on_enter)
        boton_7.bind('<Leave>', on_leave)

        # Octavo boton
        borde_8 = tk.LabelFrame(self, **style.STYLE_BUTTON_BORDER)
        borde_8.pack(side=tk.LEFT, expand=True,)

        boton_8 = tk.Button(
            borde_8,
            text="Shellsort\nRecursivo",
            command=self.move_to_8,
            ** style.STYLE_BUTTON,
        )
        boton_8.pack(expand=True, fill=tk.BOTH)

        boton_8.bind('<Enter>', on_enter)
        boton_8.bind('<Leave>', on_leave)


class Burbuja(tk.Frame):
    matriz = list()
    count = 0
    auxiliar_numeros_ingresados = ""

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
            text="Algoritmo Burbuja",
            # desempaquetado del diccionario STYLE
            **style.STYLE_TITTLE,
        ).pack(side=tk.TOP, fill=tk.X, expand=True, pady=30)

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


class Insercion(tk.Frame):
    matriz = list()
    count = 0
    auxiliar_numeros_ingresados = ""

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
        ordenamiento.inserccion(self.matriz)
        resultado = str(self.matriz)[1:len(str(self.matriz))-1]
        self.resultado.set(str(resultado).replace(",", ", "))

    def init_widgets(self):
        tk.Label(
            self,
            text="Algoritmo por Inserción",
            # desempaquetado del diccionario STYLE
            **style.STYLE_TITTLE,
        ).pack(side=tk.TOP, fill=tk.X, expand=True, pady=30)

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
            **style.STYLE_ENTRY
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


class Seleccion(tk.Frame):

    matriz = list()
    count = 0
    auxiliar_numeros_ingresados = ""

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
        ordenamiento.seleccion(self.matriz)
        resultado = str(self.matriz)[1:len(str(self.matriz))-1]
        self.resultado.set(str(resultado).replace(",", ", "))

    def init_widgets(self):
        tk.Label(
            self,
            text="Algoritmo por Selección",
            # desempaquetado del diccionario STYLE
            **style.STYLE_TITTLE,
        ).pack(side=tk.TOP, fill=tk.X, expand=True, pady=30)

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
            **style.STYLE_ENTRY
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


class Shellsort(tk.Frame):

    matriz = list()
    count = 0
    auxiliar_numeros_ingresados = ""

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
        ordenamiento.shellSort(self.matriz)
        resultado = str(self.matriz)[1:len(str(self.matriz))-1]
        self.resultado.set(str(resultado).replace(",", ", "))

    def init_widgets(self):
        tk.Label(
            self,
            text="Algoritmo Shellsort",
            # desempaquetado del diccionario STYLE
            **style.STYLE_TITTLE,
        ).pack(side=tk.TOP, fill=tk.X, expand=True, pady=30)

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
            **style.STYLE_ENTRY
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


class Mergesort(tk.Frame):

    matriz = list()
    count = 0
    auxiliar_numeros_ingresados = ""

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
        ordenamiento.mergeSort(self.matriz, 0, len(self.matriz)-1)
        resultado = str(self.matriz)[1:len(str(self.matriz))-1]
        self.resultado.set(str(resultado).replace(",", ", "))

    def init_widgets(self):
        tk.Label(
            self,
            text="Algoritmo Mergesort",
            # desempaquetado del diccionario STYLE
            **style.STYLE_TITTLE,
        ).pack(side=tk.TOP, fill=tk.X, expand=True, pady=30)

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
            **style.STYLE_ENTRY
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


class Quicksort(tk.Frame):

    matriz = list()
    count = 0
    auxiliar_numeros_ingresados = ""

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
        ordenamiento.quickSort(self.matriz)
        resultado = str(self.matriz)[1:len(str(self.matriz))-1]
        self.resultado.set(str(resultado).replace(",", ", "))

    def init_widgets(self):
        tk.Label(
            self,
            text="Algoritmo Quicksort",
            # desempaquetado del diccionario STYLE
            **style.STYLE_TITTLE,
        ).pack(side=tk.TOP, fill=tk.X, expand=True, pady=30)

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
            **style.STYLE_ENTRY
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


class Heapsort(tk.Frame):

    matriz = list()
    count = 0
    auxiliar_numeros_ingresados = ""

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
        self.matriz = ordenamiento.heapSort(self.matriz)
        resultado = str(self.matriz)[1:len(str(self.matriz))-1]
        self.resultado.set(str(resultado).replace(",", ", "))

    def init_widgets(self):
        tk.Label(
            self,
            text="Algoritmo Heapsort",
            # desempaquetado del diccionario STYLE
            **style.STYLE_TITTLE,
        ).pack(side=tk.TOP, fill=tk.X, expand=True, pady=30)

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
            **style.STYLE_ENTRY
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


class ShellsortRecursivo(tk.Frame):

    matriz = list()
    count = 0
    auxiliar_numeros_ingresados = ""

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
        ordenamiento.shellsort_recursivo(self.matriz)
        resultado = str(self.matriz)[1:len(str(self.matriz))-1]
        self.resultado.set(str(resultado).replace(",", ", "))

    def init_widgets(self):
        tk.Label(
            self,
            text="Algoritmo Shellsort Recursivo",
            # desempaquetado del diccionario STYLE
            **style.STYLE_TITTLE,
        ).pack(side=tk.TOP, fill=tk.X, expand=True, pady=30)

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
            **style.STYLE_ENTRY
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
