import re


def validate_email(correo: str) -> bool:
    EMAIL_REGEX = re.compile(
        r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[A-Za-z]*$")
    is_valid = False if not EMAIL_REGEX.match(correo) else True

    return is_valid


def validate_password(clave: str) -> bool:
    PASSWORD_REGEX = re.compile(r"^[a-zA-Z0-9.]{4,25}$")
    is_valid = False if not PASSWORD_REGEX.match(clave) else True
    return is_valid


def validate_letters(expresion: str) -> bool:
    EXPRESSION_REGEX = re.compile(r"^[a-zA-Z.]{2,50}$")
    is_valid = False if not EXPRESSION_REGEX.match(expresion) else False
    return is_valid