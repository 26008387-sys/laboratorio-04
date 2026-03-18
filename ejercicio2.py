texto_original = input("Ingrese el texto a transformar: ")
# 1. Pasar a mayusculas (permitido usar funcion de Python)
texto_mayus = texto_original.upper()
texto_final = ""
for caracter in texto_mayus:
    if caracter == "A":
        texto_final += "4"
    elif caracter == "E":
        texto_final += "3"
    elif caracter == "I":
        texto_final += "1"
    elif caracter == "O":
        texto_final += "0"
    else:
        # Si no es ninguna de las letras anteriores, se queda igual
        texto_final += caracter
# 2. Mostrar el resultado
print("Texto transformado:")
print(texto_final)
