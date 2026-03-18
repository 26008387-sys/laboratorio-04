# Definimos el PIN correcto (puedes cambiarlo aquí)
PIN_CORRECTO = "2024"
intentos = 0
max_intentos = 4
while intentos < max_intentos:
    pin_ingresado = input(f"Intento {intentos + 1}: Ingrese su PIN de 4 digitos: ")
    # 1. Verificar que tenga 4 dígitos
    if len(pin_ingresado) == 4 and pin_ingresado.isdigit():
        # 2. Verificar si es el correcto
        if pin_ingresado == PIN_CORRECTO:
            print("El PIN fue correcto. Acceso concedido.")
            break
        else:
            print("PIN incorrecto. Intente de nuevo.")
            intentos += 1
    else:
        print("Error: El PIN debe ser un numero de exactamente 4 digitos.")
        intentos += 1
# Mensaje final si se agotan los intentos
if intentos == max_intentos:
    print("Se le acabaron los intentos, vuelva mas tarde")
