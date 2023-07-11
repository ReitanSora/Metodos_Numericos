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
import os
from PIL import ImageTk, Image
from static import style


class Home(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BG)
        self.controller = controller
        self.init_widgets()

    def addImg(self, ruta):

        return self.render

    def init_widgets(self):
        ruta_img = os.path.abspath("./resources/math.png")

        self.container = tk.Canvas(
            self, background=style.BG, bd=0, relief="flat", highlightthickness=0)
        self.container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20)


        container_frame = tk.Frame(self.container, background=style.BG)
        container_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.container.create_window((0, 0), window=container_frame)

        # label titulo bienvenida
        tk.Label(
            container_frame,
            text="Bienvenido al programa de Métodos Numéricos",
            **style.STYLE_TITTLE,
        ).pack(side=tk.TOP, fill=tk.X, pady=(20, 30))

        # label titulo bienvenida
        tk.Label(
            container_frame,
            text="Este programa ha sido diseñado en base a los temas y ejercicios vistos en clase, la finalidad de esta herramienta es meramente educativa. Esperamos que este aplicativo sea de utlidad para quien lo necesite, no olvides visitar el repositorio que se encuentra en Github, puedes acceder de forma directa a través de la opción que se encuentra en la pestaña 'Help'",
            **style.STYLE_TEXT,
        ).pack(side=tk.TOP, fill=tk.X, pady=(0, 20))

        # imagen de decoracion para la pantalla inicial
        imagen = Image.open(ruta_img)
        imagen = imagen.resize((200,200), Image.Resampling.BILINEAR)
        self.render = ImageTk.PhotoImage(imagen)

        img = tk.Label(container_frame,
                       image=self.render,
                       **style.STYLE_TEXT
                       )
        img.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=20)

        info_frame = tk.Frame(container_frame, background=style.BG)
        info_frame.columnconfigure(0, weight=1)
        info_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=20)

        tk.Label(info_frame,
                 text="Temas incluidos:\n\n     • Cálculo de error absoluto y relativo\n     • Cálculo de propagación de errores con gráfica\n     • Conversiones de sistemas de numeración\n     • Representación de un número en punto flotante con estándar IEEE 754\n     • Aplicación práctica del Teorema de Bolzano con gráfica\n     • Aplicación práctica del Método de Bisección con gráfica",
                 **style.STYLE_TEXT,
                 ).grid(row=0, column=0, sticky=tk.NW, pady=(0,20))

        tk.Label(info_frame,
                 text="Librerías usadas:\n\n     • tkinter\n     • pyautogui\n     • webbrowser\n     • os\n     • sqlite3\n     • re\n     • math\n     • numpy\n     • matplotlib",
                 **style.STYLE_TEXT,
                 ).grid(row=1, column=0, sticky=tk.NW)

        self.scroll = tk.Scrollbar(self,
                                   border=0,
                                   orient="vertical",
                                   command=self.container.yview,
                                   )
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.container.configure(yscrollcommand=self.scroll.set)
        self.container.bind('<Configure>', lambda e: self.container.configure(
            scrollregion=self.container.bbox(tk.ALL)))