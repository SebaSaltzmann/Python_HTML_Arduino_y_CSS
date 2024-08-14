import math
print("inicio: datos a ingresar")

TCE = int(input("""
1_ Energia Cinetica
2_ Energia Potencial

--> """))

if TCE == 1:
    while True:
        opcion = int(input("""
    1_ Ec
    2_ m
    3_ v

    --> """))
        if opcion == 4:
            print("**Fin del programa**")
            break
        elif opcion == 1:
            m1 = float(input("ingrese la masa: "))
            v = float(input("ingrese la velocidad: "))
            Ec = 1/2 * m1 * v**2
            print(f"La energia cinetica Es: {Ec}")
        elif opcion == 2:
            Ec = float(input("ingrese la Energia cinetica: "))
            v = float(input("ingrese la velocidad: "))
            m2 = Ec * 2 / v**2
            print(f"la masa es igual a {m2}")
        elif opcion == 3:
            m3 = float(input("ingrese la masa: "))
            Ec = float(input("ingrese la Energia cinetica: "))
            velocidad = math.sqrt((2*Ec)/m3)
            print(f"La velocidad es igual a {velocidad}")
elif TCE == 2:
    while True:
        opcion = int(input("""
    1_ Ep
    2_ m
    3_ v

    --> """))

        if opcion == 1:
            m1 = float(input("ingrese la masa: "))
            h = float(input("ingrese la altura: "))
            g = 9,8
            Ep = m1 * g * h
            print(f"La energia potencial Es: {Ep}")
