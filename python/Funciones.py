import numpy as np
import matplotlib.pyplot as plt

# Definir valores de x
x = np.linspace(-3, 3, 400)  # Para funciones cuadrática y cúbica
x_pos = np.linspace(0, 3, 400)  # Para la raíz cuadrada (evitamos valores negativos)
x_rational = np.linspace(-3, 3, 400)
x_rational = x_rational[x_rational != 0]  # Evitamos división por cero

# Definir funciones
y1 = x**2
y2 = x**3
y3 = np.sqrt(x_pos)
y4 = 1 / x_rational

# Crear gráficos
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# f(x) = x^2
axs[0, 0].plot(x, y1, label=r'$f(x) = x^2$', color='b')
axs[0, 0].set_title('Función Cuadrática')
axs[0, 0].grid()

# f(x) = x^3
axs[0, 1].plot(x, y2, label=r'$f(x) = x^3$', color='g')
axs[0, 1].set_title('Función Cúbica')
axs[0, 1].grid()

# f(x) = sqrt(x)
axs[1, 0].plot(x_pos, y3, label=r'$f(x) = \sqrt{x}$', color='r')
axs[1, 0].set_title('Función Raíz Cuadrada')
axs[1, 0].grid()

# f(x) = 1/x
axs[1, 1].plot(x_rational, y4, label=r'$f(x) = \frac{1}{x}$', color='purple')
axs[1, 1].set_title('Función Racional')
axs[1, 1].axvline(0, color='k', linestyle='dashed')  # Asintota vertical
axs[1, 1].grid()

# Ajustes generales
for ax in axs.flat:
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

plt.tight_layout()
plt.show()
