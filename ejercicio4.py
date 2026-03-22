while True:
    password = input("Ingrese su password: ")

    # 1. Validar longitud (por lo menos 8 caracteres)
    cumple_longitud = len(password) >= 8
    conteo_vocales = 0
    conteo_digitos = 0
    vocales = "aeiouAEIOU"
    for caracter in password:

        if caracter in vocales:
            conteo_vocales += 1
        if caracter.isdigit():
            conteo_digitos += 1
    if cumple_longitud and conteo_vocales > 1 and conteo_digitos > 1:
        print("Strong password")
        break  # Termina el programa
    else:
        print("Weak password")
