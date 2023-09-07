print("inicio")
#listas altura y volumen
listaV = []
listaH = []
listaMax = []
#crea funcion menu para dar a elegir opción
def menu():
    print('''
    Ingrese 1 para hacer un calculo
    Ingrese 2 para salir
    ''')

def valores():
    print(f"los valores son: {Altura}")
    print("altura son: ",listaH)
    print(f"la lista es: {listaV}")
    comparate = list(zip(listaV, listaH))
    print(f"los datos junto a sus respectivas alturas son: {comparate}")
#Bucle while para evitar errores al ingresar en el programa
while True: 
    try:
        #llama a la funcion menu
        menu()
        felection = int(input(f"Ingrese...")) #opc del menu
        while felection > 0 and felection < 3:
                if felection == 1:
                        #valores de una caja de carton
                        h=0 
                        rango = int(input("Ingrese cantidad de iteraciones: "))
                        ancho = int(input("El ancho para la plancha de carton: "))
                        largo = int(input("El largo para la plancha de carton: "))
                        #Se piden los datos iniciales como el rango ancho y largo
                        for h in range(rango):
                            print("calculo ", (h+1))
                            h += 1
                            anchoh = ancho - h              #Ancho - h
                            largoh = largo - h              #Largo - h
                            volumen = anchoh * largoh * h   #Se calcula el volumen
                            print(f"para el ancho: {ancho} - {h} es {anchoh}")
                            print(f"para el largo: {largo} - {h} es {largoh}")
                            print(f"para el area: {anchoh} * {largoh} * {h} = {volumen}")
                            #Se imprimen los valores, se almacenan: volumen y h en las listas
                            listaH.append(h)
                            listaV.append(volumen)
                            print("---------------------------")
                            #Esto restringe el programa a valores negativos
                            if anchoh and largoh and volumen < 0:
                                print("El codigo no puede llegar a valores negativos :/")
                                break   #Termina el ciclo si el valor llega a negativo
                        #Aca empieza a imprimir el volumen y altura
                        max_area = max(listaV)  #Se usa max() para el valor más alto
                        while True:             #Esto hace el calculo del index
                            for h in range(rango):
                                Altura = listaV.index(max_area) #Con la funcion index() se puede encontrar la ubicacion de un numero especifico
                                Altura +=1                      #de una lista, en este caso el maximo es max_area
                            break
                        for i in range(3):  #Esto solo separa codigo
                            print("...")
                        #El usuario decide si desea llamar a los valores
                        print("quiere llamar a los valores?, elija 1, o ingrese otro numero para saber el max y h")
                        valores = int(input("..."))
                        if valores == 1:    #Si se cumple valor == 1 se van a llamar a los datos    (1)
                            valores()
                        else:
                            print("...")   #Si se ingresa otro numero
                        for i in range(3):  #Esto solo separa codigo
                            print("...")
                        print(f"los datos son: [{max_area}] como el maximo volumen y [{Altura}] como la altura de esa caja")#Se imprime la caja
                        #list()     
                        #zip()
                        #index()
                        break   #Esto vuelve al primer while para llamar al menu y felection
                else:
                    print(f"cerrando...          [{felection}]")
                    break
        break
    except ValueError:  #exepcion de caracter en datos ingresados
        print("Dato no valiido, reinicio al menu()")
        print("---------------------------")
#probando por primera vez el GitHub el 13/05/2023
print("fin")