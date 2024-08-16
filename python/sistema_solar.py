import numpy as np
import matplotlib.pyplot as plt

G = 6.67430e-11


class CuerpoCeleste:
    def __init__(self, nombre, masa, posicion, velocidad):
        self.nombre = nombre
        self.masa = masa
        self.posicion = np.array(posicion, dtype='float64')
        self.velocidad = np.array(velocidad, dtype='float64')
        self.aceleracion = np.zeros(2, dtype='float64')

    def actualizar_aceleracion(self, otros_cuerpos):
        self.aceleracion = np.zeros(2, dtype='float64')
        for cuerpo in otros_cuerpos:
            if cuerpo is not self:
                r_vec = cuerpo.posicion - self.posicion
                r_mag = np.linalg.norm(r_vec)
                self.aceleracion += G * cuerpo.masa * r_vec / r_mag**3

    def actualizar_velocidad(self, dt):
        self.velocidad += self.aceleracion * dt

    def actualizar_posicion(self, dt):
        self.posicion += self.velocidad * dt


sol = CuerpoCeleste("Sol", 1.989e30, [0, 0], [0, 0])
tierra = CuerpoCeleste("Tierra", 5.972e24, [1.496e11, 0], [0, 29780])


cuerpos = [sol, tierra]


dt = 60 * 60  # 1 hora
num_pasos = 1000

posiciones_tierra = []

for _ in range(num_pasos):
    for cuerpo in cuerpos:
        cuerpo.actualizar_aceleracion(cuerpos)
    
    for cuerpo in cuerpos:
        cuerpo.actualizar_velocidad(dt)
        cuerpo.actualizar_posicion(dt)
    
    posiciones_tierra.append(tierra.posicion.copy())


posiciones_tierra = np.array(posiciones_tierra)


plt.plot(posiciones_tierra[:, 0], posiciones_tierra[:, 1], label='Tierra')
plt.scatter([sol.posicion[0]], [sol.posicion[1]], color='orange', label='Sol')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
