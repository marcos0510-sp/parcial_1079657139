import re

def tiene_longitud_valida(contraseña):
    return 8 <= len(contraseña) <= 20

def tiene_mayuscula(contraseña):
    return any(c.isupper() for c in contraseña)

def tiene_minuscula(contraseña):
    return any(c.islower() for c in contraseña)

def tiene_numero(contraseña):
    return any(c.isdigit() for c in contraseña)

def tiene_caracter_especial(contraseña):
    return any(not c.isalnum() for c in contraseña)

def validar_contraseña(contraseña):
    if not tiene_longitud_valida(contraseña):
        return False, "La contraseña debe tener entre 8 y 20 caracteres."
    if not tiene_mayuscula(contraseña):
        return False, "La contraseña debe tener al menos una mayúscula."
    if not tiene_minuscula(contraseña):
        return False, "La contraseña debe tener al menos una minúscula."
    if not tiene_numero(contraseña):
        return False, "La contraseña debe tener al menos un número."
    if not tiene_caracter_especial(contraseña):
        return False, "La contraseña debe tener al menos un carácter especial."
    return True, "Contraseña válida."

if __name__ == "__main__":
    while True:
        contraseña = input("Ingrese una contraseña: ")
        valida, mensaje = validar_contraseña(contraseña)
        if valida:
            print("Contraseña aceptada.")
            break
        else:
            print(mensaje)
