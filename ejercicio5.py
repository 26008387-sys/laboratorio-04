palabra = input("Ingrese palabra: ")
letra_buscada = input("Letra a buscar:cafe ")
resultado = ""
for letra in palabra:
    if letra == letra_buscada:
        resultado += letra + " "
    else:
        resultado += "_ "
print("Resultado busqueda:", resultado.strip())
