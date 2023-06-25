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
import model.usuario as usuario
import model.persona as persona
import functions.events as event
import validation.validation as val
from static import style


class Register(tk.Toplevel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(background=style.BG)
        self.title("Registro nuevo usuario")
        self.geometry("500x600")
        self.resizable(False, False)
        self.init_widgets()

    def comprobar_usuario(self):
        posicion_persona = persona.buscar_correo(self.texto_correo.get())
        posicion_usuario = usuario.buscar_nickname(self.texto_nickname.get())

        if posicion_usuario is not None:
            self.texto_alerta_nickname.set(
                "Ya existe un usuario con este nickaname")
        elif posicion_persona is not None:
            self.texto_alerta_correo.set(
                "Ya existe un usuario con este correo")
        else:
            self.registrar_usuario()

    def validar_email(self):
        estado = val.validate_email(self.texto_correo.get())
        texto = "Correo con formato erroneo" if estado is False else ""
        self.texto_alerta_correo.set(texto)
        return estado

    def validar_nickname_clave(self):
        estado_clave = val.validate_password(self.texto_clave.get())
        estado_nickname = val.validate_password(self.texto_nickname.get())
        self.texto_alerta_clave.set(
            "La clave debe tener de 4 a 25 carácteres") if estado_clave is False else self.texto_alerta_clave.set("")
        self.texto_alerta_nickname.set(
            "Campo obligatorio, hasta 25 carácteres") if estado_nickname is False else self.texto_alerta_nickname.set("")
        return estado_nickname * estado_clave

    def validar_letras(self):
        estado_nombre = val.validate_password(self.texto_nombre.get())
        estado_apellido = val.validate_password(self.texto_apellido.get())

        self.texto_alerta_nombre.set(
            "Campo obligatorio, hasta 50 carácteres") if estado_nombre is False else self.texto_alerta_nombre.set("")
        self.texto_alerta_apellido.set(
            "Campo obligatorio, hasta 50 carácteres") if estado_apellido is False else self.texto_alerta_apellido.set("")
        return estado_nombre * estado_apellido

    def validar(self):
        if self.validar_letras() == 1 and self.validar_email() is True and self.validar_nickname_clave() == 1:
            self.comprobar_usuario()

    def validar_teclado(self, event):
        self.validar_email()
        self.validar_nickname_clave()
        self.validar_letras()

    def registrar_usuario(self):
        usuario.crear_tabla()
        persona.crear_tabla()
        usuario_ingreso = usuario.Usuario(self.texto_nickname.get(),
                                          self.texto_clave.get())
        persona_ingreso = persona.Persona(self.texto_nombre.get(
        ), self.texto_apellido.get(), self.texto_correo.get())
        usuario.ingresar(usuario_ingreso)
        persona.ingresar(persona_ingreso)

    def init_widgets(self):

        # titulo del frame
        tk.Label(self,
                 text="Registro",
                 **style.STYLE_TITTLE
                 ).pack(side=tk.TOP, fill=tk.BOTH, pady="10")

        infoFrame = tk.Frame(self, background=style.BG)
        infoFrame.columnconfigure(0, weight=1)
        infoFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True,)

        # label nombre de usuario
        tk.Label(infoFrame,
                 text="Nombre",
                 **style.STYLE_SUBTITTLE,
                 justify="center"
                 ).grid(row=0, column=0)

        # label apellido del usuario
        tk.Label(infoFrame,
                 text="Apellido",
                 **style.STYLE_SUBTITTLE
                 ).grid(row=1, column=0)

        # label nickname
        tk.Label(infoFrame,
                 text="Nickname",
                 **style.STYLE_SUBTITTLE
                 ).grid(row=2, column=0)

        # label correo electrocnico
        tk.Label(infoFrame,
                 text="Correo",
                 **style.STYLE_SUBTITTLE
                 ).grid(row=3, column=0)

        # label clave
        tk.Label(infoFrame,
                 text="Clave",
                 **style.STYLE_SUBTITTLE
                 ).grid(row=4, column=0)

        # entry nombre usuario
        borde_entry_1 = tk.LabelFrame(infoFrame,
                                      **style.STYLE_ENTRY_BORDER
                                      )
        borde_entry_1.grid(row=0, column=1, pady=(10, 0), padx="20")

        self.texto_nombre = tk.StringVar()
        entry_nombre = tk.Entry(borde_entry_1,
                                textvariable=self.texto_nombre,
                                **style.STYLE_ENTRY,
                                )
        entry_nombre.pack()

        # label alerta nombre
        self.texto_alerta_nombre = tk.StringVar()
        tk.Label(borde_entry_1,
                 textvariable=self.texto_alerta_nombre,
                 **style.STYLE_WARNING
                 ).pack()

        # entry apellido
        borde_entry_2 = tk.LabelFrame(infoFrame,
                                      **style.STYLE_ENTRY_BORDER
                                      )
        borde_entry_2.grid(row=1, column=1, pady=(10, 0), padx="20")

        self.texto_apellido = tk.StringVar()
        entry_apellido = tk.Entry(borde_entry_2,
                                  textvariable=self.texto_apellido,
                                  **style.STYLE_ENTRY
                                  )
        entry_apellido.pack()

        # label alerta apellido
        self.texto_alerta_apellido = tk.StringVar()
        tk.Label(borde_entry_2,
                 textvariable=self.texto_alerta_apellido,
                 **style.STYLE_WARNING
                 ).pack()

        # entry nickname
        borde_entry_3 = tk.LabelFrame(infoFrame,
                                      **style.STYLE_ENTRY_BORDER
                                      )
        borde_entry_3.grid(row=2, column=1, pady=(10, 0), padx="20")

        self.texto_nickname = tk.StringVar()
        entry_nickname = tk.Entry(borde_entry_3,
                                  textvariable=self.texto_nickname,
                                  **style.STYLE_ENTRY
                                  )
        entry_nickname.pack()

        # label alerta nickname
        self.texto_alerta_nickname = tk.StringVar()
        tk.Label(borde_entry_3,
                 textvariable=self.texto_alerta_nickname,
                 **style.STYLE_WARNING
                 ).pack()

        # entry correo
        borde_entry_4 = tk.LabelFrame(infoFrame,
                                      **style.STYLE_ENTRY_BORDER
                                      )
        borde_entry_4.grid(row=3, column=1, pady=(10, 0), padx="20")

        self.texto_correo = tk.StringVar()
        entry_correo = tk.Entry(borde_entry_4,
                                textvariable=self.texto_correo,
                                **style.STYLE_ENTRY
                                )
        entry_correo.pack()

        # label alerta correo
        self.texto_alerta_correo = tk.StringVar()
        tk.Label(borde_entry_4,
                 textvariable=self.texto_alerta_correo,
                 **style.STYLE_WARNING
                 ).pack()

        # entry clave
        borde_entry_5 = tk.LabelFrame(infoFrame,
                                      **style.STYLE_ENTRY_BORDER
                                      )
        borde_entry_5.grid(row=4, column=1, pady=(10, 0), padx="20")

        self.texto_clave = tk.StringVar()
        entry_clave = tk.Entry(borde_entry_5,
                               textvariable=self.texto_clave,
                               **style.STYLE_ENTRY,
                               )
        entry_clave.pack()

        # label alerta clave
        self.texto_alerta_clave = tk.StringVar()
        tk.Label(borde_entry_5,
                 textvariable=self.texto_alerta_clave,
                 **style.STYLE_WARNING
                 ).pack()

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
        borde_2.pack(side=tk.TOP, pady=(20, 80))

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
