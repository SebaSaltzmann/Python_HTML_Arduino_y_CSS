import time

def introduction():
    print("Bienvenido al desafío lógico de los interruptores.")
    time.sleep(2)
    print("\nTe encuentras frente a una habitación cerrada. Dentro de la habitación hay una bombilla.")
    time.sleep(2)
    print("Tienes tres interruptores frente a ti, solo uno de ellos enciende la bombilla.")
    time.sleep(2)
    print("Puedes encender y apagar los interruptores, pero solo puedes abrir la puerta de la habitación una vez.")
    print("¿Cuál interruptor enciende la bombilla? Piensa bien en tu estrategia antes de abrir la puerta.")
    time.sleep(2)

def get_input():
    print("\nOpciones:")
    print("1. Prender el interruptor 1.")
    print("2. Prender el interruptor 2.")
    print("3. Prender el interruptor 3.")
    print("4. Abrir la puerta de la habitación.")
    return input("\n¿Qué haces? Ingresa el número de tu acción: ")

def puzzle_solution():
    print("\n¡Es hora de abrir la puerta!")
    print("Abres la puerta y ves la bombilla.")
    time.sleep(2)
    print("\nSi la bombilla está encendida, significa que ese interruptor era el correcto.")
    print("Si está apagada pero caliente, fue encendida anteriormente.")
    print("Si está apagada y fría, ese interruptor no fue encendido.")
    time.sleep(3)
    print("\nPiensa en las combinaciones que has hecho.")

def play_game():
    introduction()
    
    switch1_on = False
    switch2_on = False
    switch3_on = False
    bulb_state = "off"
    bulb_heat = False

    while True:
        choice = get_input()

        if choice == '1':
            switch1_on = not switch1_on
            print("\nInterruptor 1 encendido." if switch1_on else "\nInterruptor 1 apagado.")
        
        elif choice == '2':
            switch2_on = not switch2_on
            print("\nInterruptor 2 encendido." if switch2_on else "\nInterruptor 2 apagado.")
        
        elif choice == '3':
            switch3_on = not switch3_on
            print("\nInterruptor 3 encendido." if switch3_on else "\nInterruptor 3 apagado.")
        
        elif choice == '4':
            if switch1_on:
                bulb_state = "on"
            elif switch2_on:
                bulb_heat = True
            break
        else:
            print("Opción inválida, por favor selecciona nuevamente.")

    puzzle_solution()

    final_choice = input("¿Qué interruptor enciende la bombilla? (1, 2 o 3): ")

    if (final_choice == '1' and bulb_state == "on") or (final_choice == '2' and bulb_heat) or (final_choice == '3' and bulb_state == "off" and not bulb_heat):
        print("\n¡Correcto! Has resuelto el enigma.")
    else:
        print("\nIncorrecto. Inténtalo de nuevo.")

play_game()
