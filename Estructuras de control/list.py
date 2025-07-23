frutas = ["pera", "fresa", "mango", "manzana"]
print(frutas)

varios = [ True, "hola", 10, 12.2]
print(varios)

indice = [0, 1, 2, 3]
print(indice[0])
print(indice[1])
print(indice[2])
print(indice[3])

indice2 = indice[1:3]
print(indice2)

print(varios + frutas)
frutas[3] = "nuez"
print(frutas)

frutas.append("mandarina")
print(frutas)

print(len(frutas))

combinacion = [frutas, indice]
print(combinacion[0][2])
print(combinacion)