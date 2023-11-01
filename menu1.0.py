def Limpiar_pantalla():
    from os import system
    system("cls")

def menu():
    print("Bienvenidos a nuestra plataforma.\n¿Qué desea realizar?: ")
    print("1- Entrar a la ibrería")
    print("2- Salir de la librería")

    option_str = input("Ingrese la opción deseada: ")
    option = int(option_str)

    if option == 1:
        print("Estamos en la librería.\nQué desea realizar: ")
        print("1- Agregar un libro")
        print("2- Ver listado de libros")
        print("3- Modificar un libro")
        print("4- Borrar un libro")
        print("5- Salir")


        search_option_str = input("Ingrese la opción de búsqueda: ")
        search_option = int(search_option_str)

        if search_option == 1:
            titulo = input("Ingrese el título del libro: ")
            print("Ha agregado el libro:", titulo)

        elif search_option == 2:
            
            print("Este es el listado de libros")
            
        elif search_option == 3:
            Modificar = input("Qué quiere modificar?: ")
            print("Ha modificado:", Modificar)

        elif search_option == 4:
            Borrar = input("Cuál quiere borrar?: ")
            print("Ha borrado:", Borrar)

        elif search_option == 5:
            print("Ha salido de la plataforma. Hasta luego")
        else:
            print("Opción de búsqueda no válida")

    elif option == 2:
        print("Ha salido de la plataforma. Hasta luego")
    else:
        print("Esa no es una opción válida")

menu()

