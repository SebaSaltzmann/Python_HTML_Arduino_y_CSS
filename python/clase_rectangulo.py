class Rectangulo:

    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def calculararea(self):
        calcular_area = self.base * self.altura
        return calcular_area

    def calcularperimetro(self):
        calcular_perimetro = (self.base + self.altura) * 2
        return calcular_perimetro


objeto1 = Rectangulo(9,6)

print("la base de tu triangulo es: ", objeto1.base)
print("la altura de tu triangulo es: ", objeto1.altura)
print("el area del rectangulo es :", objeto1.calculararea())
print("el perimetro del rectangulo es :", objeto1.calcularperimetro())

objeto2 = Rectangulo(3,6)

areatotal = objeto1.calculararea() + objeto2.calculararea()
print (areatotal)

