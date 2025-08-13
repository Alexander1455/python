def operaciones(a , b):
    suma = a + b
    resta = a - b
    multipliacion = a * b
    division = a / b
    return suma, resta, multipliacion, division

suma, resta, multiplicacion, division = operaciones(16, 23)

print(suma)
print(resta)
print(multiplicacion)
print(division)

