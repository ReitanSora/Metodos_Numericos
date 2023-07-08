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


BG = "#FFF"

COLOR_TITULO = "#000"
COLOR_SUBTITULO = "#666666"
COLOR_BLANCO = "#FFF"
COLOR_AQUA = "#257dca"
COLOR_AQUA_OSCURO = "#1D6AAD"
COLOR_MAGENTA = "#512BCF"
COLOR_MAGENTA_OSCURO = "#3b1f98"


BG_ENTRY = "#4C4C4C"
FG_ENTRY = "#4C4C4C"

BG_BUTTON_DES = "#FFF"
BG_BUTTON_EN = COLOR_MAGENTA
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
    "font": ("Corbel", 14, "bold"),
    "bg": BG,
    "fg": COLOR_SUBTITULO,
}

STYLE_WARNING = {
    "font": ("Corbel", 9, "bold"),
    "bg": BG,
    "fg": "red",
}

STYLE_ENTRY_BORDER = {
    "bg": BG,
    "relief": "flat",
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

STYLE_BUTTON_RETURN = {
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

STYLE_BUTTON_NAV= {
    "font": ("Corbel", 14, "bold"),
    "bg": COLOR_AQUA,
    "fg": "#FFF",
    "activeforeground": COLOR_AQUA,
    "activebackground": "#FFF",
    "relief": "sunken",
    "cursor": "hand2",
    "bd": 0,
    "width": 10,
    "height": 3,
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

STYLE_BUTTON_NAV_ENTER = {
    "bg": COLOR_AQUA_OSCURO,
    "fg": COLOR_BLANCO
}

STYLE_ENTRY = {
    "font": ("Corbel", 14),
    "bg": BG,
    "bd": 0,
    "fg": COLOR_TITULO,
    "selectbackground": COLOR_MAGENTA,
    "justify": "center"
}

STYLE_ENTRY_NUMBERS = {
    "font": ("Verdana", 13),
    "bg": BG_ENTRY,
    "width": "10",
    "fg": "#fff",
    "justify": "center"
}

STYLE_ENTRY_DES = {
    "font": ("Verdana", 14),
    "bg": BG,
    "fg": FG_ENTRY,
    "bd": 0,
    "cursor": "",
    "state": "readonly",
    "justify": "center"
}

STYLE_RADIO_BUTTON = {
    "font": ("Corbel", 14, "bold"),
    "bg": BG,
    "fg": COLOR_TITULO,
    "activebackground": BG,
    "activeforeground": "#000",
}

STYLE_CANVAS_LINE = {
    "bg": BG,
    "height": 3,
    "bd": 0,
    "relief": "flat",
    "highlightthickness": 0
}