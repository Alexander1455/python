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

def buscar_usuario(correos, lista_usuarios):
    for usuario in lista_usuarios:
        if usuario["correo"] == correos:
            return usuario
    return None

search_user = input("Ingrese el correo del usuario: ")

resultados = buscar_usuario(search_user, usuarios)

if resultados:
    print("Usuario encontrado")
    print(f"Nombre: {resultados['nombre']}")
    print(f"Edad : {resultados['edad']}")
    print(f"Correo: {resultados['correo']}")
else:
    print("No se encontro usuario con ese correo")
    
