# agenda
contacto = []

def agregar_contacto(nombre, telefono):
    contacto.append({"nombre": nombre, "telefono:": telefono})

def listar_contactos():
    print("\nLista de contacto: ")
    for c in contacto:
        print(f"{c['nombre']} - {c['telefono']}")


nombre = input("Ingresa el nombre: ")
telefono = input("Ingresar el telefono: ")
agregar_contacto(nombre, telefono)
print("contacto agregado")