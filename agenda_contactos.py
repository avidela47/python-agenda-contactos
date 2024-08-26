

def mostrar_menu():
    print("\nAgenda de Contactos:")
    print("1. Añadir contacto")
    print("2. Eliminaar contacto")
    print("3. Buscar contacto")
    print("4. Mostrar todos los contactos")
    print("5. Salir")
    print("\n")
    
def agregar_contacto(agenda):
    nombre = input("Ingresa el nombre del contacto: ")
    telefono = input("Ingresa el teléfono del contacto: ")
    email = input("Ingresa el email del contacto: ")
    agenda[nombre] = {"telefono": telefono, "email": email}
    print(f"Contacto '{nombre}' se agrego correctamente.!!!")
    
def eliminar_contacto(agenda):
    nombre = input("Ingresa el nombre del contacto a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto '{nombre}' eliminado correctamente.")
    else:
        print(f"Contacto '{nombre}' no encontrado en la agenda.")
        
def buscar_contacto(agenda):
    nombre = input("Ingresa el nombre del contacto a buscar: ")
    if nombre in agenda:
        contacto = agenda[nombre]
        print(f"Nombre: {nombre}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")
    else:
        print(f"Contacto '{nombre}' no encontrado en la agenda.")
        
def listar_contactos(agenda):
    if not agenda:
        print("La agenda está vacía.")
    else:
        print("\nContactos en la agenda:")
        for nombre,info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {info["telefono"]}")
            print(f"Email: {info["email"]}")
            print("-" * 20)
    
def agenda_contactos():
    agenda = {}
    
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            listar_contactos(agenda)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")
            
agenda_contactos()