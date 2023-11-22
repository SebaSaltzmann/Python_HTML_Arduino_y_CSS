class Espada:
    cuerpo = 1

    def __init__(self,daño):
        self.daño = daño

class Personaje:
    cuerpo = 1
    
    def __init__(self,raza,fuerza,velocidad,agilidad,sigilo,vida):
        self.raza = raza
        self.fuerza = fuerza
        self.velocidad = velocidad
        self.agilidad = agilidad
        self.sigilo = sigilo
        self.vida = vida

        #daño = fuerza + obj1

    def movimiento(self):
        v = self.velocidad = self.velocidad
        if v < 0:
            v = 0
            self.velocidad = v
    

    def equipar_espada(self, espada):
        self.espada = espada

    def atacar_dragon(self, dragon):
        if hasattr(self, 'espada'):
            dañio_total = self.fuerza + self.espada
            dragon.vida -= dañio_total
        else:
            print("No tienes una espada equipada.")

obj1 = Personaje("Elfo",150,200,800,400,800)
obj2 = Personaje("Dragon",300,200,100,100,1000)
obj3 = Espada(500)















