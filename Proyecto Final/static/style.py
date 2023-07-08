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

# 342E37
# 1D1E2C
# 12263A
# 210B2C
# 39393a
# 262626
# 453750
# 110B11
# 1A1423
# 335a85
# 334985
#292D3E
BG = "#292D3E"
BG_LIGH_MODE = "#DBE4EE"

COLOR_TITULO = "#FEFFEA"
COLOR_TITULO_LIGHT_MODE = "#000"
COLOR_SUBTITULO = "#FEFFEA"
COLOR_SUBTITULO_LIGHT_MODE = "#C2C2C2"

COLOR_BLANCO = "#FFF"
COLOR_NEGRO = "#000"
COLOR_GRIS = "#C2C2C2"
COLOR_AQUA = "#257dca"
COLOR_AQUA_OSCURO = "#1D6AAD"
COLOR_MAGENTA_NORMAL = "#512BCF"
COLOR_MAGENTA_CLARO = "#8A67FF"
COLOR_MAGENTA_OSCURO = "#3b1f98"
COLOR_CIAN = "#FF6B6B"

BG_ENTRY = "#4C4C4C"
FG_ENTRY = "#4C4C4C"

BG_BUTTON_DES = "#FFF"
BG_BUTTON_EN = COLOR_MAGENTA_NORMAL
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
    "fg": COLOR_GRIS,
}

STYLE_ENTRY_BORDER = {
    "font": ("Corbel", 14, "bold"),
    "bg": BG,
    "fg": COLOR_GRIS,
    "bd":0,
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

STYLE_BUTTON_NAV = {
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
    "fg": COLOR_TITULO,
    "bd": 0,
    "selectbackground": COLOR_BLANCO,
    "selectforeground": COLOR_MAGENTA_NORMAL,
    "justify": "center"
}

STYLE_ENTRY_DES = {
    "font": ("Verdana", 14),
    "bg": BG,
    "fg": COLOR_BLANCO,
    "bd": 0,
    "selectbackground": COLOR_BLANCO,
    "selectforeground": COLOR_MAGENTA_NORMAL,
    "readonlybackground": BG,
    "cursor": "",
    "state": "readonly",
    "justify": "center"
}

STYLE_RADIO_BUTTON = {
    "font": ("Corbel", 14, "bold"),
    "bg": BG,
    "fg": COLOR_BLANCO,
    "activebackground": BG,
    "activeforeground": COLOR_MAGENTA_CLARO,
    "selectcolor": BG,
    "border": "0",
    "anchor": "center",
    "borderwidth": "0",
    "relief": "flat"
}

STYLE_CANVAS = {
    "bg": BG,
    "height": 3,
    "bd": 0,
    "relief": "flat",
    "highlightthickness": 0
}

STYLE_CANVAS_LINE = {
    "width": "3",
    "fill": COLOR_MAGENTA_CLARO
}
