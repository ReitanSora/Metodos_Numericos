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
from tkinter import ttk
from tkinter import messagebox
import random as r
from static import style
# from modules.form_punto_flotante import PuntoFlotante
from functions import ordenamiento
import functions.events as event

# from PIL import ImageTk, Image


class Home(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BG, pady=50)
        self.controller = controller
        self.init_widgets()

    def move_to_errores(self):
        self.controller.show_frame(MenuTabErrores)

    def move_to_sistemas(self):
        self.controller.show_frame()

    def move_to_flotante(self):
        self.controller.show_frame(PuntoFlotante)

    def move_to_bolzano(self):
        self.controller.show_frame(Shellsort)

    def move_to_biseccion(self):
        self.controller.show_frame(Mergesort)

    def move_to_6(self):
        self.controller.show_frame(Quicksort)

    def init_widgets(self):

        tk.Label(
            self,
            text="Bienvenido al programa de\nMétodos Numéricos",
            # desempaquetado del diccionario STYLE
            **style.STYLE_TITTLE,
        ).pack(side=tk.TOP, fill=tk.BOTH, pady=0)

        optionsFrame = tk.Frame(self, background=style.BG)
        optionsFrame.columnconfigure(0, weight=1)
        optionsFrame.columnconfigure(1, weight=1)
        optionsFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady="30")

        # Primer boton
        borde_1 = tk.LabelFrame(optionsFrame, **style.STYLE_BUTTON_BORDER)
        borde_1.grid(row=0, column=0, pady="20")

        boton_1 = tk.Button(
            borde_1,
            text="Errores",
            command=self.move_to_errores,
            ** style.STYLE_BUTTON,
        )
        boton_1.pack(expand=True, fill=tk.BOTH)

        boton_1.bind('<Enter>', event.on_enter)
        boton_1.bind('<Leave>', event.on_leave)

        # Segundo boton
        borde_2 = tk.LabelFrame(optionsFrame, **style.STYLE_BUTTON_BORDER)
        borde_2.grid(row=0, column=1, pady="20")

        boton_2 = tk.Button(
            borde_2,
            text="Sistemas de\nNumeración",
            command=self.move_to_sistemas,
            ** style.STYLE_BUTTON,
        )
        boton_2.pack(expand=True, fill=tk.BOTH)

        boton_2.bind('<Enter>', event.on_enter)
        boton_2.bind('<Leave>', event.on_leave)

        # Tercer boton

        borde_3 = tk.LabelFrame(optionsFrame, **style.STYLE_BUTTON_BORDER)
        borde_3.grid(row=1, column=0, pady="20")

        boton_3 = tk.Button(
            borde_3,
            text="Punto\nFlotante",
            command=self.move_to_flotante,
            ** style.STYLE_BUTTON,
        )
        boton_3.pack(expand=True, fill=tk.BOTH)

        boton_3.bind('<Enter>', event.on_enter)
        boton_3.bind('<Leave>', event.on_leave)

        # Cuanto boton
        borde_4 = tk.LabelFrame(optionsFrame, **style.STYLE_BUTTON_BORDER)
        borde_4.grid(row=1, column=1, pady="20")

        boton_4 = tk.Button(
            borde_4,
            text="Teorema de\nBolzano",
            command=self.move_to_bolzano,
            ** style.STYLE_BUTTON,
        )
        boton_4.pack(expand=True, fill=tk.BOTH)

        boton_4.bind('<Enter>', event.on_enter)
        boton_4.bind('<Leave>', event.on_leave)

        # Quinta opcion
        borde_5 = tk.LabelFrame(optionsFrame, **style.STYLE_BUTTON_BORDER)
        borde_5.grid(row=2, column=0, pady="20")

        boton_5 = tk.Button(
            borde_5,
            text="Teorema de\nBisección",
            command=self.move_to_biseccion,
            ** style.STYLE_BUTTON,
        )
        boton_5.pack(expand=True, fill=tk.BOTH)

        boton_5.bind('<Enter>', event.on_enter)
        boton_5.bind('<Leave>', event.on_leave)

        # Sexta opcion
        borde_6 = tk.LabelFrame(optionsFrame, **style.STYLE_BUTTON_BORDER)
        borde_6.grid(row=2, column=1, pady="20")

        boton_6 = tk.Button(
            borde_6,
            text="Quicksort",
            command=self.move_to_6,
            ** style.STYLE_BUTTON,
        )
        boton_6.pack(expand=True, fill=tk.BOTH)

        boton_6.bind('<Enter>', event.on_enter)
        boton_6.bind('<Leave>', event.on_leave)


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

        boton_1.bind('<Enter>', event.on_enter)
        boton_1.bind('<Leave>', event.on_leave)

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

        boton_2.bind('<Enter>', event.on_enter)
        boton_2.bind('<Leave>', event.on_leave)

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

        boton_3.bind('<Enter>', event.on_enter)
        boton_3.bind('<Leave>', event.on_leave)

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

        boton_4.bind('<Enter>', event.on_enter)
        boton_4.bind('<Leave>', event.on_leave)

        # Quinto boton, boton para regresar al menu principal
        borde_5 = tk.LabelFrame(self, **style.STYLE_BUTTON_BORDER)
        borde_5.pack(side=tk.LEFT, expand=True, padx=50)

        boton_5 = tk.Button(
            borde_5,
            text="Regresar",
            command=Home.move_to_home
            ** style.STYLE_BUTTON
        )
        boton_5.pack(expand=True, fill=tk.BOTH)

        boton_5.bind('<Enter>', event.on_enter)
        boton_5.bind('<Leave>', event.on_leave)


class MenuTabErrores (tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BG)
        self.controller = controller

        errores = ttk.Notebook(self)
        errores.pack(expand=True, fill=tk.BOTH)

        errores.columnconfigure(0, weight=1)
        errores.rowconfigure(0, weight=1)

        
        subventana1= PropErrores(self, controller)
        subventana2 = PuntoFlotante(self, controller)

        errores.add(subventana1, text="Propagación")
        errores.add(subventana2, text="Propagación")

        # for F in (PropErrores, PuntoFlotante):
        #     frame = F(errores, self)
        #     self.frames[F] = frame

        #     # configuracion de filas, columnas y rellenado del frame
        #     frame.grid(row=0, column=0, sticky=tk.NSEW)
        # self.show_frame( errores ,PropErrores)

    # def show_frame(self, container, frame):
        
    #     container.add(frame, text="Propagación Errores")

        # para poner una pantalla encima de la otra
        

        # tab1 = tk.Frame(errores, width=400, height=400, bg="#000")
        # tab2 = tk.Frame(errores, width=400, height=400, bg="#fff")

        # tab1.pack(fill=tk.BOTH, expand=True)
        # tab2.pack(fill=tk.BOTH, expand=True)

        # errores.add(tab1, text="negro")
        # errores.add(tab2, text="blanco")
        # self.init_widgets()


    
    def init_widgets(self):
        pass

    

class PropErrores(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BG)
        self.controller = controller
        self.init_widgets()

    def move_to_home(self):
        self.controller.show_frame(Home)

    def init_widgets(self):
        tk.Label(self,
                 text="Propagación de Errores",
                 **style.STYLE_TITTLE,
                 ).pack(side=tk.TOP, fill=tk.BOTH, pady=30)

        inputFrame = tk.Frame(self, background=style.BG)
        inputFrame.columnconfigure(0, weight=1)
        inputFrame.pack(side=tk.TOP, fill=tk.BOTH)

        # label ecuacion
        tk.Label(inputFrame,
                 text="Ecuación",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=0)

        # label exponente
        tk.Label(inputFrame,
                 text="Exponente",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=1, column=0)

        # label respuesta
        tk.Label(inputFrame,
                 text="Respuesta",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=2, column=0)

        # entry desactivado formula
        self.formula = tk.StringVar()
        tk.Entry(inputFrame,
                 textvariable=self.formula,
                 **style.STYLE_ENTRY_DES,
                 ).grid(row=0, column=1, pady="10", padx="20")

        # entry desactivado respuesta
        self.respuesta = tk.StringVar()
        tk.Entry(inputFrame,
                 textvariable=self.respuesta,
                 **style.STYLE_ENTRY_DES,
                 ).grid(row=2, column=1, pady="10", padx="20")

        # entry desactivado exponente
        self.exponente = tk.StringVar()
        tk.Entry(inputFrame,
                 textvariable=self.exponente,
                 **style.STYLE_ENTRY,
                 ).grid(row=1, column=1, pady="10", padx="20")

        # boton para calcular
        borde_1 = tk.LabelFrame(inputFrame,
                                **style.STYLE_BUTTON_BORDER)
        borde_1.grid(row=0, rowspan=3, column=2, pady="30", padx="20")

        boton_calculo = tk.Button(borde_1,
                                  text="Calcular",
                                  **style.STYLE_BUTTON,
                                  )
        boton_calculo.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        boton_calculo.bind('<Enter>', event.on_enter)
        boton_calculo.bind('<Leave>', event.on_leave)

        outputFrame = tk.Frame(self, background="#666666")
        outputFrame.pack(side=tk.TOP, fill=tk.BOTH,
                         expand=True, padx="10", pady="10")

        # boton para regresar
        borde_2 = tk.LabelFrame(self,
                                **style.STYLE_BUTTON_RETURN_BORDER)
        borde_2.pack(side=tk.TOP, padx="10", pady="10")

        boton_return = tk.Button(borde_2,
                                 text="Regresar",
                                 **style.STYLE_BUTTON_RETURN,
                                 command=self.move_to_home
                                 )
        boton_return.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        boton_return.bind('<Enter>', event.on_enter_return)
        boton_return.bind('<Leave>', event.on_leave_return)


class PuntoFlotante(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BG)
        self.controller = controller
        self.init_widgets()

    def move_to_home(self):
        self.controller.show_frame(Home)

    def init_widgets(self):
        tk.Label(self,
                 text="Punto Flotante",
                 **style.STYLE_TITTLE,
                 ).pack(side=tk.TOP, fill=tk.BOTH, pady=30)

        inputFrame = tk.Frame(self, background=style.BG)
        inputFrame.columnconfigure(0, weight=1)
        inputFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True,)

        # label numero decimal
        tk.Label(inputFrame,
                 text="Número decimal",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=0)

        # label numero decimal con exponente
        tk.Label(inputFrame,
                 text="Número decimal\ncon exponente",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=1, column=0)

        # entry numero decimal normal
        self.decimal_normal = tk.StringVar()
        tk.Entry(inputFrame,
                 textvariable=self.decimal_normal,
                 **style.STYLE_ENTRY,
                 ).grid(row=0, column=1, pady="20", padx="20")

        # entry numero decimal con exponente
        self.decimal_exponente = tk.StringVar()
        tk.Entry(inputFrame,
                 textvariable=self.decimal_exponente,
                 **style.STYLE_ENTRY,
                 ).grid(row=1, column=1, pady="20", padx="20")

        # boton para calcular
        borde_1 = tk.LabelFrame(inputFrame,
                                **style.STYLE_BUTTON_BORDER)
        borde_1.grid(row=0, rowspan=2, column=2, pady="30", padx="20")

        boton_calculo = tk.Button(borde_1,
                                  text="Calcular",
                                  **style.STYLE_BUTTON,
                                  )
        boton_calculo.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        boton_calculo.bind('<Enter>', event.on_enter)
        boton_calculo.bind('<Leave>', event.on_leave)

        outputFrame = tk.Frame(self, background=style.BG)
        outputFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True,)

        # label signo
        tk.Label(outputFrame,
                 text="Signo",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=0)

        # label exponente
        tk.Label(outputFrame,
                 text="Exponente",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=1, column=0)

        # label mantisa
        tk.Label(outputFrame,
                 text="Mantisa",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=2, column=0)

        # label hexadecimal
        tk.Label(outputFrame,
                 text="Representación\nHexadecimal",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=3, column=0)

        # entry desactivado signo
        self.resultado_signo = tk.StringVar()
        tk.Entry(outputFrame,
                 textvariable=self.resultado_signo,
                 **style.STYLE_ENTRY_DES,
                 ).grid(row=0, column=1, pady="20", padx="20")

        # entry desactivado exponente
        self.resultado_exponente = tk.StringVar()
        tk.Entry(outputFrame,
                 textvariable=self.resultado_exponente,
                 **style.STYLE_ENTRY_DES,
                 ).grid(row=1, column=1, pady="20", padx="20")

        # entry desactivado mantisa
        self.resultado_mantisa = tk.StringVar()
        tk.Entry(outputFrame,
                 textvariable=self.resultado_mantisa,
                 **style.STYLE_ENTRY_DES,
                 ).grid(row=2, column=1, pady="20", padx="20")

        # entry desactivado hexadecimal
        self.resultado_hexadecimal = tk.StringVar()
        tk.Entry(outputFrame,
                 textvariable=self.resultado_hexadecimal,
                 **style.STYLE_ENTRY_DES,
                 ).grid(row=3, column=1, pady="20", padx="20")

        # boton para regresar
        borde_2 = tk.LabelFrame(outputFrame,
                                **style.STYLE_BUTTON_RETURN_BORDER)
        borde_2.grid(row=4, rowspan=2, column=1, pady="30")

        boton_return = tk.Button(borde_2,
                                 text="Regresar",
                                 **style.STYLE_BUTTON_RETURN,
                                 command=self.move_to_home
                                 )
        boton_return.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        boton_return.bind('<Enter>', event.on_enter_return)
        boton_return.bind('<Leave>', event.on_leave_return)


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
