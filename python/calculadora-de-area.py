import math
try:
    menu = """
    *********** menu **************
    ***  calculo de areas       ***
    *** 1_ triangulo equilatero ***
    *** 2_ circulo              ***
    *** 3_ salir                ***
    *******************************
    """
    print(menu)
    var1 = int(input("--> "))
except ValueError: print("error vuelva a intentarlo") 

while var1==1 :
    try:
        valor1 = int(input("ingrese el valor de la base de su triangulo: "))
        lado = int(input("ingrese un lado de su triangulo equilatero: "))

        resultado = valor1 * lado / 2

        print(f"el resultado del area es: {resultado}")

        print(menu)
        var1 = int(input("--> "))
        
    except ValueError: print("error vuelva a intentarlo")

while var1==2:
    try:
        radio = float(input("ingrese el valor de su radio: "))
        resultado1 = math.pi * radio ** 2

        print(f"el resultado del area de su circulo es: {resultado1}")

        print(menu)
        var1 = int(input("--> "))
    except ValueError: print("error vuelva a intentarlo")        



print("*fin del programa*")