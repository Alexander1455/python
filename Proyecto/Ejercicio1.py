
usuarios =[]

while True:
    nombre = input("Ingrese su nombre:")
    edad = input("Ingrese su edad: ")
    correo = input("Ingrese su Correo: ")

    usuario = {
        "nombre": nombre,
        "edad": edad,
        "correo": correo
    }
    
    usuarios.append(usuario)

    continuar = input("Desea agregar un nuevo usuario? (si/no)").lower()
    if continuar != "si":
        break

print("\nUsuarios registrados:")
for i, u in enumerate(usuarios, 1):
    print(f"{i}. Nombre: {u['nombre']} | Edad: {u['edad']} | Correo: {u['correo']}")



