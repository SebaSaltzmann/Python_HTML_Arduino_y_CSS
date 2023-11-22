

class Rectangulo:

    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def calculararea(self):
        self.calcular_area = self.base * self.altura
        return self.calcular_area

    def calcularperimetro(self):
        self.calcular_perimetro = (self.calcular_area + self.altura) ** 2
        return self.calcular_perimetro


objeto1 = Rectangulo(9,6)

print("la base de tu triangulo es: ", objeto1.base)
print("la altura de tu triangulo es: ", objeto1.altura)
print("el area del rectangulo es :", objeto1.calculararea())
print("el perimetro del rectangulo es :", objeto1.calcularperimetro())
