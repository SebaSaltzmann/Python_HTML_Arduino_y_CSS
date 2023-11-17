usuarios = {}

def menu():
    opcionesMenu= """
    =================================================
    =   BIENVENDOS - INICIAR SESIÓN O REGISTRARSE   =
    =================================================
    =  1. Registrar usuario                         =
    =  2. Iniciar sesión                            =
    =  3. Salir                                     =
    =================================================
    """
    print(opcionesMenu)

def registrar_usuario():
    nombreUsuario = input("Ingrese un nombre de usuario: ")
    if nombreUsuario in usuarios:
        print("El usuario ya existe. Intente con otro nombre de usuario.")
    else:
        contrasena = input("Ingrese una contraseña: ")
        usuarios[nombreUsuario] = contrasena
        print("Usuario registrado con éxito.")

def iniciar_sesion():
    nombreUsuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    if nombreUsuario in usuarios and usuarios[nombreUsuario] == contrasena:
        print("Inicio de sesión exitoso. ¡Bienvenido,", nombreUsuario, "!")
    else:
        print("Credenciales incorrectas. Intente nuevamente.")

while True:
    menu()

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        registrar_usuario()
    elif opcion == '2':
        iniciar_sesion()
    elif opcion == '4':
         print(usuarios)
    elif opcion == '3':
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
