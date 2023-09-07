print("inicio")
menu = """ 
############################################
### 1. convertir de Fahrenheit a Celcius ###
### 2. convertir de Celcius a Fahrenheit ###
### 3. salir                             ###    
############################################
"""
print(menu)
def Fahrenheit():
    gf = int(input("ingrese la temperatura deseada a convertir: "))
    gc = (gf - 32) / 1.8
    return (gc)

def celcius():
    gC = int(input("ingrese la temperatura deseada a convertir: "))
    gF = gC * 1.8 + 32
    return (gF)

while True:

    opcion = int(input("elija la opcion deseada: "))

    if opcion == 3:
        print("***fin del programa***")
        break
    elif opcion == 1:
        print(Fahrenheit())
    elif opcion == 2:
        print(celcius())
    

