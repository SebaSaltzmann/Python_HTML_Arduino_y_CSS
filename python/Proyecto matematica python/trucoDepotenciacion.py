funcionPrograma = """
    Esta función analiza las potencias de números terminados en 5
    elevados al cuadrado hasta un número dado n.
    """
print(funcionPrograma)

def menu ():
    menu1 = '''
    *********************************
    ***   1-Analisis de potencia  ***
    ***   2-salir                ***
    *********************************'''
    print(menu1)
    opcion=int(input("Ingrese la operacion a realizar: "))
    return opcion

def analizar_potencias_terminadas_en_5(n):
    resultados = {}
    for i in range(5, n + 1, 10): 
        resultado = i ** 2
        resultados[i] = resultado
        print(f"{i}^2 = {resultado}")
    return resultados

n_max = int(input("Ingrese el número máximo a analizar: "))
analizar_potencias_terminadas_en_5(n_max)
