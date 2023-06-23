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

from static import style

# eventos para efecto de hover en botones
def on_enter(e):
    e.widget.config(**style.STYLE_BUTTON_ENTER)


def on_leave(e):
    e.widget.config(**style.STYLE_BUTTON)


def on_enter_return(e):
    e.widget.config(**style.STYLE_BUTTON_RETURN_ENTER)


def on_leave_return(e):
    e.widget.config(**style.STYLE_BUTTON_RETURN)
