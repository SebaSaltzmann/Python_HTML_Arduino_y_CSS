import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Button, Slider

# Constantes optimizadas
G = 6.67430e-11
AU = 1.496e11
DIAS_POR_AÑO = 365.25

class CuerpoCeleste:
    def __init__(self, nombre, masa, posicion, velocidad, color, tamaño):
        self.nombre = nombre
        self.masa = masa
        self.color = color
        self.tamaño = tamaño
        
        # Usar dtype=np.float32 en lugar de float64 para mejor rendimiento
        self.posicion = np.array(posicion, dtype=np.float32)
        self.velocidad = np.array(velocidad, dtype=np.float32)
        self.aceleracion = np.zeros(3, dtype=np.float32)
        
        # Buffer circular más pequeño
        self.max_orbita = 50  # Reducido para mejor rendimiento
        self._buffer_orbita = np.zeros((self.max_orbita, 3), dtype=np.float32)
        self._indice_orbita = 0
        
        # Historial reducido
        self.historial_velocidades = []
        self.max_historial = 50  # Limitar el historial
        
        # Datos orbitales
        self.distancia_al_sol = 0
        self.velocidad_orbital = 0
        self.energia_cinetica = 0
        self.energia_potencial = 0

    def calcular_fuerzas(self, otros_cuerpos):
        self.aceleracion.fill(0)  # Más eficiente que crear nuevo array
        for otro in otros_cuerpos:
            if otro is not self:
                r = otro.posicion - self.posicion
                distancia = np.linalg.norm(r)
                if distancia > 0:
                    self.aceleracion += G * otro.masa * r / (distancia ** 3)

        if self.nombre != "Sol":
            self.distancia_al_sol = np.linalg.norm(self.posicion)
            self.velocidad_orbital = np.linalg.norm(self.velocidad)

    def mover(self, dt):
        self.velocidad += self.aceleracion * dt
        self.posicion += self.velocidad * dt
        
        # Actualizar buffer circular
        self._buffer_orbita[self._indice_orbita] = self.posicion
        self._indice_orbita = (self._indice_orbita + 1) % self.max_orbita
        
        # Actualizar historial con límite
        if len(self.historial_velocidades) >= self.max_historial:
            self.historial_velocidades.pop(0)
        self.historial_velocidades.append(self.velocidad_orbital)

    def calcular_energias(self, otros_cuerpos):
        v = np.linalg.norm(self.velocidad)
        self.energia_cinetica = 0.5 * self.masa * v**2
        self.energia_potencial = 0
        for otro in otros_cuerpos:
            if otro is not self:
                r = np.linalg.norm(otro.posicion - self.posicion)
                if r > 0:
                    self.energia_potencial -= G * self.masa * otro.masa / r

# Sistema solar reducido para mejor rendimiento
cuerpos = [
    CuerpoCeleste("Sol", 1.989e30, [0, 0, 0], [0, 0, 0], 'yellow', 20),
    CuerpoCeleste("Tierra", 5.972e24, [AU, 0, 0], [0, 29780, 0], 'blue', 12),
    CuerpoCeleste("Marte", 6.39e23, [1.524*AU, 0, 0], [0, 24070, 0], 'red', 10)
]

# Configuración de visualización optimizada
plt.style.use('dark_background')
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Variables de control
zoom_factor = 1.0
rotation_angle = 0
dt = 60 * 60 * 24  # 1 día
paused = False
update_info = 0  # Contador para actualizar información

def actualizar_vista():
    limite = 2 * AU * zoom_factor
    ax.set_xlim([-limite, limite])
    ax.set_ylim([-limite, limite])
    ax.set_zlim([-limite/2, limite/2])

def actualizar(frame):
    global update_info
    if not paused:
        ax.clear()
        
        # Actualizar sistema
        for cuerpo in cuerpos:
            cuerpo.calcular_fuerzas(cuerpos)
        for cuerpo in cuerpos:
            cuerpo.mover(dt)
        
        # Actualizar energías cada 5 frames para mejor rendimiento
        if update_info % 5 == 0:
            for cuerpo in cuerpos:
                cuerpo.calcular_energias(cuerpos)
        update_info += 1
        
        # Dibujar sistema optimizado
        for cuerpo in cuerpos:
            # Dibujar órbita con menos puntos
            orbita_valida = cuerpo._buffer_orbita[~np.all(cuerpo._buffer_orbita == 0, axis=1)]
            if len(orbita_valida) > 1:
                ax.plot(orbita_valida[:, 0], orbita_valida[:, 1], orbita_valida[:, 2],
                       color=cuerpo.color, alpha=0.3, linewidth=1)
            
            # Dibujar planeta
            ax.scatter(cuerpo.posicion[0], cuerpo.posicion[1], cuerpo.posicion[2],
                      color=cuerpo.color, s=cuerpo.tamaño*2, label=cuerpo.nombre,
                      picker=True)
        
        # Configuración básica de vista
        ax.set_title('Sistema Solar')
        ax.legend(loc='upper right', fontsize='small')
        actualizar_vista()
        ax.view_init(elev=20, azim=rotation_angle)

# Eventos simplificados
def zoom(event):
    global zoom_factor
    if event.inaxes == ax:
        zoom_factor *= 0.9 if event.button == 'up' else 1.1
        actualizar_vista()

def toggle_pausa(event):
    global paused
    paused = not paused

# Configurar interactividad básica
fig.canvas.mpl_connect('scroll_event', zoom)
fig.canvas.mpl_connect('button_press_event', lambda event: toggle_pausa(event) if event.dblclick else None)

# Animación optimizada
ani = animation.FuncAnimation(fig, actualizar, 
                            interval=50,  # Intervalo más largo para mejor rendimiento
                            cache_frame_data=False,
                            blit=False)  # blit=False para evitar problemas de memoria

plt.show()