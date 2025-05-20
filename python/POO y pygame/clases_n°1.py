class Auto:
    ruedas = 4
    motor = 1

    def __init__(self,color,aceleracion,marca) :
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0
        self.marca = marca

    def aceleracionF(self):
        self.velocidad=self.velocidad + self.aceleracion

    def freno(self):
        v = self.velocidad = self.aceleracion
        if v < 0:
            v = 0
            self.velocidad = v

print("Auto 1")
obj1 = Auto("gris", 10, "ford")
print("color del auto: ", obj1.color)
print("velociadad del auto: ", obj1.velocidad)
print("aceleracion del auto: ", obj1.aceleracion)
print("marca del auto", obj1.marca)

print("Auto 2")
obj2 = Auto("azul", 17, "BMW")
print("color del auto: ", obj2.color)
print("velociadad del auto: ", obj2.velocidad)
print("aceleracion del auto: ", obj2.aceleracion)
print("marca del auto", obj2.marca)
