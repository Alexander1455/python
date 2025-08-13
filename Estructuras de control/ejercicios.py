for i in range(1, 11):
    print(i)


suma = 0
while True:
    numero = int(input("Ingrese el numero o Fin para finalizar la suma: "))
    if numero.lower():
        break
    try:
        suma = numero + numero
    except ValueError:
        print("Por favor, ingrese un numero valido o fin.")
print(f"La suma total es:{suma}")

for i in range(0, 51, 2):
    if i % 2 == 0:
        print(i)

for y in range(0, 1):
    numero = int(input("ingrese el numero de la tabla: "))
    for i in range(1, 13):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
    
import random

while True:
    print("1. mostrar mensaje motivacional")
    print("2. Mostrar numero aleatorio")
    print("3. Salir")

    opcion = input("Escoge un numero (1-3): ")

    if opcion == "1":
        pass