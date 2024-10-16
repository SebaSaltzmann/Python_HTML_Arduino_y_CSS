print("Este es un programa que cuenta palabras, cantidad de letras en cada palabra, promedio de longitud de cada palabra y cantidad de oraciones")
parrafo = input("ingrese su texto --> ")

palabras = parrafo.split()
Cantidad_de_palabras = len(palabras)

letras = len(parrafo.replace(" ",""))

print(f"Cantidad de palabras: {Cantidad_de_palabras}")
print(f"Cantidad de letras: {letras}")
