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
import functions.events as event
import functions.funcion_flotante_2 as flotante
from static import style
from validation import validacion


class PuntoFlotante(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BG)
        self.controller = controller
        self.init_widgets()

    def move_to_home(self):
        self.vaciar_campos()
        self.controller.move_to_home()

    def vaciar_campos(self):
        self.decimal_normal.set("")
        self.decimal_exponente.set("")
        self.exponente.set("")
        self.resultado_signo.set("")
        self.resultado_exponente.set("")
        self.resultado_mantisa.set("")
        self.resultado_hexadecimal.set("")
        self.texto_alerta_ndecimal.set("")
        self.texto_alerta_edecimal.set("")
        self.texto_alerta_exponente.set("")

    def validar_campo_unico_1 (self):
        if self.decimal_normal != "" and self.decimal_exponente == "":
            self.validar_calculo_normal()
        elif self.decimal_normal == "" and self.decimal_exponente != "":
            self.validar_calculo_exponente()
        else:
            self.texto_alerta_ndecimal.set("Solo debe completar uno de los dos campos")
            self.texto_alerta_edecimal.set("Solo debe completar uno de los dos campos")

    def validar_calculo_normal(self):
        if validacion.validate_float(self.decimal_normal.get()) is True:
            self.texto_alerta_ndecimal.set("")
            self.calcular_normal()
        else:
            self.texto_alerta_ndecimal.set("Ingrese números del 0-9")

    def validar_calculo_exponente(self):
        if validacion.validate_float(self.decimal_exponente.get()) is True:
            self.texto_alerta_edecimal.set("")
            self.calcular_exponente()
        else:
            self.texto_alerta_edecimal.set("Ingrese números del 0-9")

    def calcular_normal(self):
        pass

    def calcular_exponente(self):
        pass

    def init_widgets(self):

        # label del título
        tk.Label(self,
                 text="Punto Flotante",
                 **style.STYLE_TITTLE,
                 ).pack(side=tk.TOP, fill=tk.BOTH, pady=30)

        input_frame = tk.Frame(self, background=style.BG)
        input_frame.columnconfigure(0, weight=1)
        input_frame.columnconfigure(1, weight=1)
        input_frame.columnconfigure(2, weight=1)
        input_frame.columnconfigure(3, weight=1)
        input_frame.columnconfigure(4, weight=1)
        input_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True,)

        # label numero decimal
        tk.Label(input_frame,
                 text="Número decimal",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=0, pady=20, padx=10, sticky=tk.N)

        # label numero decimal 2
        tk.Label(input_frame,
                 text="Número decimal\ncon exponente",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=1, column=0, pady=20, sticky=tk.N)

        # label exponente
        tk.Label(input_frame,
                 text="x 10 ^ ",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=1, column=2, pady=20, sticky=tk.N)

        # entry numero decimal normal
        borde_entry_1 = tk.LabelFrame(input_frame,
                                      **style.STYLE_ENTRY_BORDER,
                                      )
        borde_entry_1.grid(row=0, column=1, columnspan=3, pady=(20,0), sticky=tk.EW)

        self.decimal_normal = tk.StringVar()
        tk.Entry(borde_entry_1,
                 textvariable=self.decimal_normal,
                 **style.STYLE_ENTRY_NUMBERS,
                 ).pack(fill=tk.BOTH, expand=True)

        # label alerta decimal normal
        self.texto_alerta_ndecimal = tk.StringVar()
        tk.Label(borde_entry_1,
                 textvariable=self.texto_alerta_ndecimal,
                 **style.STYLE_WARNING
                 ).pack()

        # entry numero decimal con exponente
        borde_entry_2 = tk.LabelFrame(input_frame,
                                      **style.STYLE_ENTRY_BORDER
                                      )
        borde_entry_2.grid(row=1, column=1, pady=(20,0), sticky=tk.EW)

        self.decimal_exponente = tk.StringVar()
        tk.Entry(borde_entry_2,
                 textvariable=self.decimal_exponente,
                 **style.STYLE_ENTRY_NUMBERS,
                 ).pack(fill=tk.BOTH, expand=True)

        # label alerta decimal exponente
        self.texto_alerta_edecimal = tk.StringVar()
        tk.Label(borde_entry_2,
                 textvariable=self.texto_alerta_edecimal,
                 **style.STYLE_WARNING
                 ).pack()

        # entry exponente
        borde_entry_3 = tk.LabelFrame(input_frame,
                                      **style.STYLE_ENTRY_BORDER
                                      )
        borde_entry_3.grid(row=1, column=3, pady=(20,0))

        self.exponente = tk.StringVar()
        tk.Entry(borde_entry_3,
                 textvariable=self.exponente,
                 **style.STYLE_ENTRY_NUMBERS,
                 ).pack(fill=tk.BOTH, expand=True)

        # label alerta decimal exponente
        self.texto_alerta_exponente = tk.StringVar()
        tk.Label(borde_entry_3,
                 textvariable=self.texto_alerta_exponente,
                 **style.STYLE_WARNING
                 ).pack()

        # boton para calcular
        borde_1 = tk.LabelFrame(input_frame,
                                **style.STYLE_BUTTON_BORDER)
        borde_1.grid(row=0, rowspan=2, column=4, pady="30", padx="20")

        boton_calculo = tk.Button(borde_1,
                                  text="Calcular",
                                  **style.STYLE_BUTTON,
                                  )
        boton_calculo.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        boton_calculo.bind('<Enter>', event.on_enter)
        boton_calculo.bind('<Leave>', event.on_leave)

        outputFrame = tk.Frame(self, background=style.BG)
        outputFrame.columnconfigure(0, weight=1)
        outputFrame.columnconfigure(1, weight=1)
        outputFrame.columnconfigure(2, weight=1)
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
                 ).grid(row=0, column=1, pady="20", padx=(0, 20), sticky=tk.EW)

        # entry desactivado exponente
        self.resultado_exponente = tk.StringVar()
        tk.Entry(outputFrame,
                 textvariable=self.resultado_exponente,
                 **style.STYLE_ENTRY_DES,
                 ).grid(row=1, column=1, pady="20", padx=(0, 20), sticky=tk.EW)

        # entry desactivado mantisa
        self.resultado_mantisa = tk.StringVar()
        tk.Entry(outputFrame,
                 textvariable=self.resultado_mantisa,
                 **style.STYLE_ENTRY_DES,
                 ).grid(row=2, column=1, pady="20", padx=(0, 20), sticky=tk.EW)

        # entry desactivado hexadecimal
        self.resultado_hexadecimal = tk.StringVar()
        tk.Entry(outputFrame,
                 textvariable=self.resultado_hexadecimal,
                 **style.STYLE_ENTRY_DES,
                 ).grid(row=3, column=1, pady="20", padx=(0, 20), sticky=tk.EW)

        # boton para regresar
        borde_2 = tk.LabelFrame(self,
                                **style.STYLE_BUTTON_RETURN_BORDER)
        borde_2.pack(side=tk.BOTTOM, pady=(0, 20))

        boton_return = tk.Button(borde_2,
                                 text="Regresar",
                                 **style.STYLE_BUTTON_RETURN,
                                 command=self.move_to_home
                                 )
        boton_return.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        boton_return.bind('<Enter>', event.on_enter_return)
        boton_return.bind('<Leave>', event.on_leave_return)
