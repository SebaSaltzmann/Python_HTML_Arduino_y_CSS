import time

def intro():
    print("Bienvenido al Escape Room Virtual.")
    time.sleep(2)
    print("\nEstás atrapado en una habitación cerrada. Para escapar, debes resolver varios acertijos.")
    time.sleep(2)
    print("Hay una puerta cerrada con un código de cuatro dígitos, un escritorio, y una caja misteriosa.")
    time.sleep(2)
    print("Tendrás que usar la lógica para encontrar pistas y salir de la habitación.")
    time.sleep(2)

def solve_riddle():
    print("\nAcertijo: \n")
    print("Soy alto cuando soy joven, y bajo cuando soy viejo. ¿Qué soy?")
    answer = input("\nEscribe tu respuesta: ").lower()

    if answer == "vela" or answer == "una vela":
        print("\n¡Correcto! Encuentras una llave dentro de la vela.")
        return True
    else:
        print("\nIncorrecto. Piensa de nuevo.")
        return False

def open_desk():
    print("\nAbres el escritorio y encuentras un papel con el siguiente número: 7532.")
    time.sleep(2)
    print("Esto parece ser una pista para la caja o la puerta.")
    return "7532"

def open_box():
    print("\nLa caja está cerrada con un candado numérico de cuatro dígitos.")
    code = input("\nIngresa el código de cuatro dígitos: ")

    if code == "7532":
        print("\n¡El candado se abre! Dentro de la caja encuentras otra pista: 'El código de la puerta es el número al revés'.")
        return True
    else:
        print("\nEl código es incorrecto. Intenta de nuevo.")
        return False

def open_door():
    print("\nLlegas a la puerta. Necesitas un código de cuatro dígitos para abrirla.")
    code = input("\nIngresa el código de la puerta: ")

    if code == "2357":
        print("\n¡Correcto! La puerta se abre y logras escapar de la habitación. ¡Felicidades!")
        return True
    else:
        print("\nEl código es incorrecto. Sigues atrapado en la habitación.")
        return False

def play_game():
    intro()
    has_key = False
    desk_open = False
    box_open = False

    while True:
        print("\n¿Qué quieres hacer?")
        print("1. Inspeccionar la vela.")
        print("2. Abrir el escritorio.")
        print("3. Abrir la caja.")
        print("4. Abrir la puerta.")
        action = input("\nElige una opción (1-4): ")

        if action == '1':
            if solve_riddle():
                has_key = True
        elif action == '2':
            if not desk_open:
                desk_code = open_desk()
                desk_open = True
            else:
                print("\nYa has inspeccionado el escritorio.")
        elif action == '3':
            if has_key and not box_open:
                if open_box():
                    box_open = True
            elif not has_key:
                print("\nParece que necesitas una llave para abrir la caja.")
            else:
                print("\nYa has abierto la caja.")
        elif action == '4':
            if box_open:
                if open_door():
                    break
            else:
                print("\nParece que aún no tienes el código correcto para la puerta.")
        else:
            print("\nOpción no válida. Intenta de nuevo.")

play_game()
