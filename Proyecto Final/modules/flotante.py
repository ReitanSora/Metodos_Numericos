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

    def clean(self):
        self.texto_alerta_ndecimal.set("")
        self.texto_alerta_edecimal.set("")
        self.texto_alerta_exponente.set("")

    def validar_campo_unico(self):
        if self.decimal_normal.get() != "" and self.decimal_exponente.get() == "":
            self.validar_calculo_normal()
        elif self.decimal_normal.get() == "" and self.decimal_exponente.get() != "":
            self.validar_calculo_exponente()
        else:
            self.texto_alerta_ndecimal.set("Solo un dato")
            self.texto_alerta_edecimal.set("Solo un dato")

    def validar_calculo_normal(self):
        if validacion.validate_number_float(self.decimal_normal.get()) is True:
            self.texto_alerta_ndecimal.set("")
            self.calcular(float(self.decimal_normal.get()))
        else:
            self.texto_alerta_ndecimal.set("Números del 0-9 y .")

    def validar_calculo_exponente(self):
        if validacion.validate_number_float(self.decimal_exponente.get()) is True:
            if validacion.validate_number_float(self.exponente.get()) is True:
                self.texto_alerta_edecimal.set("")
                print(float(self.exponente.get()))
                self.calcular(
                    pow(float(self.decimal_exponente.get()), float(self.exponente.get())))
            else:
                self.texto_alerta_exponente.set("Exponente erroneo")
        else:
            self.texto_alerta_edecimal.set("Números del 0-9 y .")

    def calcular(self, valor: float):
        self.clean()
        try:
            (valor_signo, valor_exponente, valor_mantisa, valor_hexa,
             valor_normalizado) = flotante.ingreso_decimal(valor, self.precision.get())
            self.resultado_signo.set(valor_signo)
            self.resultado_exponente.set(valor_exponente)
            self.resultado_mantisa.set(valor_mantisa)
            self.resultado_hexadecimal.set(valor_hexa)
            self.resultado_normalizado.set(valor_normalizado)
        except ValueError:
            self.texto_alerta_edecimal.set("Imposible representar")

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
                 text=" ^ ",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=1, column=2, pady=20, sticky=tk.N)

        # entry numero decimal normal
        borde_entry_1 = tk.LabelFrame(input_frame,
                                      **style.STYLE_ENTRY_BORDER,
                                      )
        borde_entry_1.grid(row=0, column=1, columnspan=3,
                           pady=(20, 0), sticky=tk.EW)

        self.decimal_normal = tk.StringVar()
        tk.Entry(borde_entry_1,
                 textvariable=self.decimal_normal,
                 **style.STYLE_ENTRY,
                 ).pack(side=tk.TOP, fill=tk.X, expand=True)
        
        canvas_linea_1 = tk.Canvas(
            borde_entry_1, **style.STYLE_CANVAS, width=500)
        canvas_linea_1.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_1.create_line(0, 0, 500, 0, **style.STYLE_CANVAS_LINE)

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
        borde_entry_2.grid(row=1, column=1, pady=(20, 0), sticky=tk.EW)

        self.decimal_exponente = tk.StringVar()
        tk.Entry(borde_entry_2,
                 textvariable=self.decimal_exponente,
                 **style.STYLE_ENTRY,
                 ).pack(side=tk.TOP, fill=tk.X, expand=True)
        
        canvas_linea_2 = tk.Canvas(
            borde_entry_2, **style.STYLE_CANVAS, width=250)
        canvas_linea_2.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_2.create_line(0, 0, 250, 0, **style.STYLE_CANVAS_LINE)

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
        borde_entry_3.grid(row=1, column=3, pady=(20, 0), sticky=tk.EW)

        self.exponente = tk.StringVar()
        tk.Entry(borde_entry_3,
                 textvariable=self.exponente,
                 **style.STYLE_ENTRY,
                 ).pack(side=tk.TOP, fill=tk.X, expand=True)
        
        canvas_linea_3 = tk.Canvas(
            borde_entry_3, **style.STYLE_CANVAS, width=250)
        canvas_linea_3.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_3.create_line(0, 0, 250, 0, **style.STYLE_CANVAS_LINE)

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
                                  command=self.validar_campo_unico
                                  )
        boton_calculo.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        boton_calculo.bind('<Enter>', event.on_enter)
        boton_calculo.bind('<Leave>', event.on_leave)

        PRESICION = {
            "Simple": 1,
            "Doble": 2
        }

        borde_seleccion = tk.LabelFrame(
            input_frame, **style.STYLE_ENTRY_BORDER)
        borde_seleccion.grid(row=0, column=4)

        self.precision = tk.IntVar(value=1)
        for (keys, values) in PRESICION.items():
            tk.Radiobutton(borde_seleccion,
                           text=keys,
                           variable=self.precision,
                           value=values,
                           **style.STYLE_RADIO_BUTTON,
                           ).pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        output_frame = tk.Frame(self, background=style.BG)
        output_frame.columnconfigure(0, weight=1)
        output_frame.columnconfigure(1, weight=1)
        output_frame.columnconfigure(2, weight=1)
        output_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True,)

        # label signo
        tk.Label(output_frame,
                 text="Signo",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=0)

        # label exponente
        tk.Label(output_frame,
                 text="Exponente",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=1, column=0)

        # label mantisa
        tk.Label(output_frame,
                 text="Mantisa",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=2, column=0)

        # label hexadecimal
        tk.Label(output_frame,
                 text="Representación\nHexadecimal",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=3, column=0)
        
        # label binario normalizado
        tk.Label(output_frame,
                 text="Normalizado a\nHexadecimal",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=4, column=0)

        # entry desactivado signo
        borde_entry_4 = tk.LabelFrame(output_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_4.grid(row=0, column=1, pady="20", padx=(0, 20), sticky=tk.EW)

        self.resultado_signo = tk.StringVar()
        tk.Entry(borde_entry_4,
                 textvariable=self.resultado_signo,
                 **style.STYLE_ENTRY_DES,
                 ).pack(side=tk.TOP, fill=tk.X, expand=True)
        
        canvas_linea_4 = tk.Canvas(
            borde_entry_4, **style.STYLE_CANVAS, width=500)
        canvas_linea_4.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_4.create_line(0, 0, 500, 0, **style.STYLE_CANVAS_LINE)

        # entry desactivado exponente
        borde_entry_5 = tk.LabelFrame(output_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_5.grid(row=1, column=1, pady="20", padx=(0, 20), sticky=tk.EW)

        self.resultado_exponente = tk.StringVar()
        tk.Entry(borde_entry_5,
                 textvariable=self.resultado_exponente,
                 **style.STYLE_ENTRY_DES,
                 ).pack(side=tk.TOP, fill=tk.X, expand=True)
        
        canvas_linea_5 = tk.Canvas(
            borde_entry_5, **style.STYLE_CANVAS, width=500)
        canvas_linea_5.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_5.create_line(0, 0, 500, 0, **style.STYLE_CANVAS_LINE)

        # entry desactivado mantisa
        borde_entry_6 = tk.LabelFrame(output_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_6.grid(row=2, column=1, pady="20", padx=(0, 20), sticky=tk.EW)

        self.resultado_mantisa = tk.StringVar()
        tk.Entry(borde_entry_6,
                 textvariable=self.resultado_mantisa,
                 **style.STYLE_ENTRY_DES,
                 ).pack(side=tk.TOP, fill=tk.X, expand=True)
        
        canvas_linea_6 = tk.Canvas(
            borde_entry_6, **style.STYLE_CANVAS, width=500)
        canvas_linea_6.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_6.create_line(0, 0, 500, 0, **style.STYLE_CANVAS_LINE)

        # entry desactivado hexadecimal
        borde_entry_7 = tk.LabelFrame(output_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_7.grid(row=3, column=1, pady="20", padx=(0, 20), sticky=tk.EW)

        self.resultado_hexadecimal = tk.StringVar()
        tk.Entry(borde_entry_7,
                 textvariable=self.resultado_hexadecimal,
                 **style.STYLE_ENTRY_DES,
                 ).pack(side=tk.TOP, fill=tk.X, expand=True)
        
        canvas_linea_7 = tk.Canvas(
            borde_entry_7, **style.STYLE_CANVAS, width=500)
        canvas_linea_7.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_7.create_line(0, 0, 500, 0, **style.STYLE_CANVAS_LINE)
        
        # entry desactivado binario normalizado
        borde_entry_8 = tk.LabelFrame(output_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_8.grid(row=4, column=1, pady="20", padx=(0, 20), sticky=tk.EW)

        self.resultado_normalizado = tk.StringVar()
        tk.Entry(borde_entry_8,
                 textvariable=self.resultado_normalizado,
                 **style.STYLE_ENTRY_DES,
                 ).pack(side=tk.TOP, fill=tk.X, expand=True)
        
        canvas_linea_8 = tk.Canvas(
            borde_entry_8, **style.STYLE_CANVAS, width=500)
        canvas_linea_8.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_8.create_line(0, 0, 500, 0, **style.STYLE_CANVAS_LINE)
