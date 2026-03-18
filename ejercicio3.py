import random

# 1. Inicialización de variables
bateria = 100
iteraciones = 0
print(f"Estado inicial: {bateria}%")
print("-" * 30)
# 2. Ciclo de descarga
while bateria > 0:
    iteraciones += 1
    descarga = random.randint(4, 12)
    bateria -= descarga
    if bateria < 0:
        bateria = 0
    print(f"Iteracion {iteraciones}: Se descargo {descarga}%. Queda {bateria}% de carga.")
# 3. Resultado final
print("-" * 30)
print(f"La bateria se agoto por completo.")
print(f"Tomó un total de {iteraciones} iteraciones descargarla.")
