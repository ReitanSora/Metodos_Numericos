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
import model.usuario as usuario
import functions.events as event
import validation.validacion as val
from static import style


class Register(tk.Toplevel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(background=style.BG)
        self.title("Registro nuevo usuario")
        self.geometry("500x600")
        self.resizable(False, False)
        self.init_widgets()

    def vaciar_campos(self):
        self.texto_nombre.set("")
        self.texto_apellido.set("")
        self.texto_nickname.set("")
        self.texto_correo.set("")
        self.texto_clave.set("")
        self.texto_alerta_nombre.set("")
        self.texto_alerta_apellido.set("")
        self.texto_alerta_nickname.set("")
        self.texto_alerta_correo.set("")
        self.texto_alerta_clave.set("")

    # funcion para validar los datos ingresados por el usuario cuando escribe por teclado
    def validar_teclado(self, event):
        self.validar_email()
        self.validar_nickname_clave()
        self.validar_letras()

    # funcion para validar los datos ingresados por el usuario cuando presiona el boton registrar
    def validar(self):
        self.validar_letras()
        self.validar_email()
        self.validar_nickname_clave()
        if (self.validar_letras() == 1 and self.validar_email() is True and self.validar_nickname_clave() == 1):
            self.comprobar_usuario()

    def validar_email(self):
        estado = val.validate_email(self.texto_correo.get())
        self.texto_alerta_correo.set(
            "Correo con formato erroneo" if estado is False else "")
        return estado

    def validar_nickname_clave(self):
        estado_clave = val.validate_password(self.texto_clave.get())
        estado_nickname = val.validate_password(self.texto_nickname.get())
        self.texto_alerta_clave.set(
            "La clave debe tener de 4 a 25 carácteres" if estado_clave is False else "")
        self.texto_alerta_nickname.set(
            "Campo de hasta 25 carácteres" if estado_nickname is False else "")
        return estado_nickname * estado_clave

    def validar_letras(self):
        estado_nombre = val.validate_letters(self.texto_nombre.get())
        estado_apellido = val.validate_letters(self.texto_apellido.get())

        self.texto_alerta_nombre.set(
            "Campo de hasta 50 carácteres" if estado_nombre is False else "")
        self.texto_alerta_apellido.set(
            "Campo de hasta 50 carácteres" if estado_apellido is False else "")
        return estado_nombre * estado_apellido

    # funcion para comprobar si ya existe un usuario con el mismo nickname o correo
    def comprobar_usuario(self):
        posicion_nickname = usuario.buscar(self.texto_nickname.get(), 1)
        posicion_correo = usuario.buscar(self.texto_correo.get(), 2)

        if posicion_nickname is not None:
            self.texto_alerta_nickname.set(
                "Ya existe un usuario con este nickname")
        elif posicion_correo is not None:
            self.texto_alerta_correo.set(
                "Ya existe un usuario con este correo")
        else:
            self.registrar_usuario()

    # funcion para registrar un usuario en la base de datos
    def registrar_usuario(self):
        usuario.crear_tabla()
        usuario_ingreso = usuario.Usuario(self.texto_nombre.get(), self.texto_apellido.get(), self.texto_nickname.get(), self.texto_correo.get(),
                                          self.texto_clave.get())
        usuario.ingresar(usuario_ingreso)
        self.vaciar_campos()

    # funcion para inicializar los widgets de la ventana
    def init_widgets(self):

        # titulo del frame
        tk.Label(self,
                 text="Registro",
                 **style.STYLE_TITTLE
                 ).pack(side=tk.TOP, fill=tk.BOTH, pady=10)

        info_frame = tk.Frame(self, background=style.BG)
        info_frame.columnconfigure(0, weight=1)
        info_frame.columnconfigure(1, weight=1)
        info_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True,)

        # label nombre de usuario
        tk.Label(info_frame,
                 text="Nombre",
                 **style.STYLE_SUBTITTLE,
                 justify="center"
                 ).grid(row=0, column=0, pady=10, sticky=tk.N)

        # label apellido del usuario
        tk.Label(info_frame,
                 text="Apellido",
                 **style.STYLE_SUBTITTLE
                 ).grid(row=1, column=0, pady=10, sticky=tk.N)

        # label nickname
        tk.Label(info_frame,
                 text="Nickname",
                 **style.STYLE_SUBTITTLE
                 ).grid(row=2, column=0, pady=10, sticky=tk.N)

        # label correo electrocnico
        tk.Label(info_frame,
                 text="Correo",
                 **style.STYLE_SUBTITTLE
                 ).grid(row=3, column=0, pady=10, sticky=tk.N)

        # label clave
        tk.Label(info_frame,
                 text="Clave",
                 **style.STYLE_SUBTITTLE
                 ).grid(row=4, column=0, pady=10, sticky=tk.N)

        # entry nombre usuario
        borde_entry_1 = tk.LabelFrame(info_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_1.grid(row=0, column=1, pady=(10, 0), sticky=tk.EW)

        self.texto_nombre = tk.StringVar()
        entry_nombre = tk.Entry(borde_entry_1,
                                textvariable=self.texto_nombre,
                                **style.STYLE_ENTRY,
                                )
        entry_nombre.pack(side=tk.TOP, expand=True)

        canvas_linea_1 = tk.Canvas(
            borde_entry_1, **style.STYLE_CANVAS, width=250)
        canvas_linea_1.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_1.create_line(0, 0, 250, 0, **style.STYLE_CANVAS_LINE)

        # label alerta nombre
        self.texto_alerta_nombre = tk.StringVar()
        tk.Label(borde_entry_1,
                 textvariable=self.texto_alerta_nombre,
                 **style.STYLE_WARNING
                 ).pack()

        # entry apellido
        borde_entry_2 = tk.LabelFrame(info_frame,
                                      **style.STYLE_ENTRY_BORDER
                                      )
        borde_entry_2.grid(row=1, column=1, pady=(10, 0), sticky=tk.EW)

        self.texto_apellido = tk.StringVar()
        entry_apellido = tk.Entry(borde_entry_2,
                                  textvariable=self.texto_apellido,
                                  **style.STYLE_ENTRY
                                  )
        entry_apellido.pack(side=tk.TOP, expand=True)

        canvas_linea_2 = tk.Canvas(
            borde_entry_2, **style.STYLE_CANVAS, width=250)
        canvas_linea_2.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_2.create_line(
            0, 0, 250, 0, **style.STYLE_CANVAS_LINE)

        # label alerta apellido
        self.texto_alerta_apellido = tk.StringVar()
        tk.Label(borde_entry_2,
                 textvariable=self.texto_alerta_apellido,
                 **style.STYLE_WARNING
                 ).pack()

        # entry nickname
        borde_entry_3 = tk.LabelFrame(info_frame,
                                      **style.STYLE_ENTRY_BORDER
                                      )
        borde_entry_3.grid(row=2, column=1, pady=(10, 0), sticky=tk.EW)

        self.texto_nickname = tk.StringVar()
        entry_nickname = tk.Entry(borde_entry_3,
                                  textvariable=self.texto_nickname,
                                  **style.STYLE_ENTRY
                                  )
        entry_nickname.pack(side=tk.TOP, expand=True)

        canvas_linea_3 = tk.Canvas(
            borde_entry_3, **style.STYLE_CANVAS, width=250)
        canvas_linea_3.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_3.create_line(
            0, 0, 250, 0, **style.STYLE_CANVAS_LINE)

        # label alerta nickname
        self.texto_alerta_nickname = tk.StringVar()
        tk.Label(borde_entry_3,
                 textvariable=self.texto_alerta_nickname,
                 **style.STYLE_WARNING
                 ).pack()

        # entry correo
        borde_entry_4 = tk.LabelFrame(info_frame,
                                      **style.STYLE_ENTRY_BORDER
                                      )
        borde_entry_4.grid(row=3, column=1, pady=(10, 0), sticky=tk.EW)

        self.texto_correo = tk.StringVar()
        entry_correo = tk.Entry(borde_entry_4,
                                textvariable=self.texto_correo,
                                **style.STYLE_ENTRY
                                )
        entry_correo.pack(side=tk.TOP, expand=True)

        canvas_linea_4 = tk.Canvas(
            borde_entry_4, **style.STYLE_CANVAS, width=250)
        canvas_linea_4.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_4.create_line(
            0, 0, 250, 0, **style.STYLE_CANVAS_LINE)

        # label alerta correo
        self.texto_alerta_correo = tk.StringVar()
        tk.Label(borde_entry_4,
                 textvariable=self.texto_alerta_correo,
                 **style.STYLE_WARNING
                 ).pack()

        # entry clave
        borde_entry_5 = tk.LabelFrame(info_frame,
                                      **style.STYLE_ENTRY_BORDER
                                      )
        borde_entry_5.grid(row=4, column=1, pady=(10, 0), sticky=tk.EW)

        self.texto_clave = tk.StringVar()
        entry_clave = tk.Entry(borde_entry_5,
                               textvariable=self.texto_clave,
                               **style.STYLE_ENTRY,
                               )
        entry_clave.pack(side=tk.TOP, expand=True)

        canvas_linea_5 = tk.Canvas(
            borde_entry_5, **style.STYLE_CANVAS, width=250)
        canvas_linea_5.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_5.create_line(
            0, 0, 250, 0, **style.STYLE_CANVAS_LINE)

        # label alerta clave
        self.texto_alerta_clave = tk.StringVar()
        tk.Label(borde_entry_5,
                 textvariable=self.texto_alerta_clave,
                 **style.STYLE_WARNING
                 ).pack(side=tk.TOP, expand=True)

        # boton para registrarse
        borde_1 = tk.LabelFrame(self,
                                **style.STYLE_BUTTON_BORDER)
        borde_1.pack(side=tk.TOP, pady=(20, 0))

        self.boton_register = tk.Button(borde_1,
                                        text="Registrar",
                                        **style.STYLE_BUTTON,
                                        command=self.validar
                                        )
        self.boton_register.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.boton_register.bind('<Enter>', event.on_enter)
        self.boton_register.bind('<Leave>', event.on_leave)

        # boton para regresar
        borde_2 = tk.LabelFrame(self,
                                **style.STYLE_BUTTON_RETURN_BORDER)
        borde_2.pack(side=tk.TOP, pady=(20, 50))

        boton_regresar = tk.Button(borde_2,
                                   text="Regresar",
                                   **style.STYLE_BUTTON_RETURN,
                                   command=self.destroy
                                   )
        boton_regresar.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        boton_regresar.bind('<Enter>', event.on_enter_return)
        boton_regresar.bind('<Leave>', event.on_leave_return)

        entry_nombre.bind('<KeyRelease>', self.validar_teclado)
        entry_apellido.bind('<KeyRelease>', self.validar_teclado)
        entry_nickname.bind('<KeyRelease>', self.validar_teclado)
        entry_correo.bind('<KeyRelease>', self.validar_teclado)
        entry_clave.bind('<KeyRelease>', self.validar_teclado)
