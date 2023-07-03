import re
import ast

def validate_email(correo: str) -> bool:
    EMAIL_REGEX = re.compile(
        r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[A-Za-z]*$")
    is_valid = False if not EMAIL_REGEX.match(correo) else True

    return is_valid


def validate_password(clave: str) -> bool:
    PASSWORD_REGEX = re.compile(r"^[a-zA-Z0-9ñÑáéíóúÁÉÍÓÚ.]{4,25}$")
    is_valid = False if not PASSWORD_REGEX.match(clave) else True
    return is_valid


def validate_letters(expresion: str) -> bool:
    EXPRESSION_REGEX = re.compile(r"^[a-zA-ZñÑáéíóúÁÉÍÓÚ.\s]{2,50}$")
    is_valid = False if not EXPRESSION_REGEX.match(expresion) else True
    return is_valid

# método para validar los números de cédula de los socios
def validate_number_decimal(numeros: str) -> bool:
    NUMBERS_REGEX = re.compile(r"^[0-9]{1,}$")
    is_valid = False if not NUMBERS_REGEX.match(numeros) else True
    return is_valid

# método para validar los números de cédula de los socios
def validate_number_binary(numeros: str) -> bool:
    NUMBERS_REGEX = re.compile(r"^[0-1]{1,}$")
    is_valid = False if not NUMBERS_REGEX.match(numeros) else True
    return is_valid

# método para validar los números de cédula de los socios
def validate_decimal(numeros: str) -> bool:
    is_valid = type(ast.literal_eval(numeros))
    if is_valid == float:
        return True
    else:
        return False