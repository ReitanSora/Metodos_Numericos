'''
Tema: Métodos Numéricos
#Grupo #
#Integrantes:

•	Kevin Josue Amaguaña Rivadeneira
•	Priscila Veronica Chisag Pillajo
•	Andy Ricardo Galarza Morales
•	Stiven Anthony Pilca Sánchez

#Carrera: Ingeniería en Sistemas de la información
#Paralelo: SI4 - 002
'''

import tkinter as tk

class Menu(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)

        barra_menu = tk.Menu(parent)
        parent.config(menu=barra_menu)

        opcion_user = tk.Menu(barra_menu, tearoff=0)
        opcion_file = tk.Menu(barra_menu, tearoff=0)
        opcion_edit = tk.Menu(barra_menu, tearoff=0)
        opcion_help = tk.Menu(barra_menu, tearoff=0)

        barra_menu.add_cascade(label="File", menu=opcion_file)
        barra_menu.add_cascade(label="Edit", menu=opcion_edit)
        barra_menu.add_cascade(label="User", menu=opcion_user)
        barra_menu.add_cascade(label="Help", menu=opcion_help)

        opcion_file.add_command(label="Guardar Imágen", command=parent.screenshot)
        opcion_file.add_command(label="Nueva ventana", command=parent.new_window)
        opcion_file.add_separator()
        opcion_file.add_command(label="Salir" , command=parent.salir)

        opcion_edit.add_command(label="Copiar")
        opcion_edit.add_command(label="Cortar")

        opcion_user.add_command(label="Actualizar Información")
        opcion_user.add_command(label="Cambiar Clave")
        opcion_user.add_command(label="Cerrar Sesión")
        opcion_user.add_separator()
        opcion_user.add_command(label="Eliminar Cuenta")

        opcion_help.add_command(label="Manual de usuario")
        opcion_help.add_command(label="Manual técnico")
        opcion_help.add_command(label="Repositorio en Github", command=parent.github)
        opcion_help.add_separator()
        opcion_help.add_command(label="Versión 1.0")
