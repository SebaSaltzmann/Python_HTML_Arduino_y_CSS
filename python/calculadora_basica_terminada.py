import math
print("inicio")
#variables
print("""INGRESE UNA OPCION:

1-OPERACIONES BASICAS
2-FUNCION CUADRATICA

""")
OB = int(input("-->"))

def menu ():
    menu1 = '''
    ****************************
    ***   1-suma:            *** 
    ***   2-resta:           ***
    ***   3-division:        ***
    ***   4-multiplicacion:  ***
    ***   5-salir:           ***
    ****************************'''
    print(menu1)
    opcion1=int(input("Ingrese la operacion a realizar: "))
    return opcion1

#operaciones basicas
def suma(a,b):
    return a+b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
   if b == 0:
       print("no se puede puede dividir por 0, ingrese el segundo numero")
   else:
        return a/b
   
#funcion cuadrática
def ceros(a,b,c):
    return -b+-b**2-4*a*c/2*a

if OB == 1:
    while True:

        opcion2 = menu()
        
        if opcion2 == 5:
            print("**fin del progrma**")
            break
        else:
            num1 = float(input("ingrese el primer numero: "))
            num2 = float(input("ingrese el segundo numero: "))
            if opcion2==1:
                print(suma(num1, num2))
            elif opcion2==2:
                print(resta(num1,num2))
            elif opcion2==3:
                print(division(num1,num2))
            elif opcion2==4:
                print(multiplicacion(num1,num2))
elif OB == 2:

    while True:

        print("1_Calculo ceros")
        print("2_Salir")

        OP = int(input("ingrese una opción: "))


        if OP == 1:
            num1 = float(input("ingrese el primer numero: "))
            num2 = float(input("ingrese el segundo numero: "))
            num3 = float(input("ingrese el segundo numero: "))

            print(ceros(num1,num2,num3))
        else:
            print("**fin del progrma**")
            break