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


BG = "#FFF"

COLOR_TITULO = "#666666"
COLOR_SUBTITULO = "#666666"

BG_ENTRY = "#4C4C4C"
FG_ENTRY = "#4C4C4C"

BG_BUTTON_DES = "#FFF"
BG_BUTTON_EN = "#3b1f98"
FG_BUTTON_DES = "#3b1f98"
FG_BUTTON_EN = "#FFF"

BG_BUTTON_RETURN_DES = "#FFF"
BG_BUTTON_RETURN_EN = "#257dca"
FG_BUTTON_RETURN_DES = "#257dca"
FG_BUTTON_RETURN_EN = "#FFF"

STYLE_TITTLE = {
    "font": ("Corbel", 20, "bold"),
    "bg": BG,
    "fg": COLOR_TITULO
}

STYLE_SUBTITTLE = {
    "font": ("Corbel", 16, "bold"),
    "bg": BG,
    "fg": COLOR_TITULO,
}

STYLE_BUTTON_BORDER = {
    "bg": BG_BUTTON_EN,
    "relief": "flat",
    "bd": 3,
    "width": 12,
}

STYLE_BUTTON_RETURN_BORDER = {
    "bg": BG_BUTTON_RETURN_EN,
    "relief": "flat",
    "bd": 3,
    "width": 12,
}

STYLE_BUTTON = {
    "font": ("Corbel", 14, "bold"),
    "bg": BG_BUTTON_DES,
    "fg": FG_BUTTON_DES,
    "activeforeground": FG_BUTTON_DES,
    "activebackground": BG_BUTTON_DES,
    "relief": "sunken",
    "cursor": "hand2",
    "bd": 0,
    "width": 10,
    "padx": 20,
}

STYLE_BUTTON_RETURN= {
    "font": ("Corbel", 14, "bold"),
    "bg": BG_BUTTON_RETURN_DES,
    "fg": FG_BUTTON_RETURN_DES,
    "activeforeground": FG_BUTTON_RETURN_DES,
    "activebackground": BG_BUTTON_RETURN_DES,
    "relief": "sunken",
    "cursor": "hand2",
    "bd": 0,
    "width": 10,
    "padx": 20,
}

STYLE_BUTTON_ENTER = {
    "bg": BG_BUTTON_EN,
    "fg": FG_BUTTON_EN, 
}

STYLE_BUTTON_RETURN_ENTER = {
    "bg": BG_BUTTON_RETURN_EN,
    "fg": FG_BUTTON_RETURN_EN, 
}

STYLE_ENTRY = {
    "font": ("Verdana", 14),
    "bg": BG_ENTRY,
    "fg": "#fff",
    "bd": 1,
    "width": 20,
    "justify": "center"
}

STYLE_ENTRY_DES = {
    "font": ("Verdana", 14),
    "bg": BG_ENTRY,
    "fg": FG_ENTRY,
    "bd": 1,
    "width": 60,
    "cursor": "",
    "state": "readonly",
    "justify": "center"
}
