import tkinter as tk
from pynput import keyboard, mouse
import threading

# --- GUI SETUP ---
root = tk.Tk()
root.title("Monitor de Teclado y Mouse")
root.geometry("600x400")
root.attributes("-topmost", True)

# Marcos para teclado y mouse
keyboard_frame = tk.LabelFrame(root, text="Teclado", padx=10, pady=10)
keyboard_frame.pack(padx=10, pady=10, fill="x")

mouse_frame = tk.LabelFrame(root, text="Mouse", padx=10, pady=10)
mouse_frame.pack(padx=10, pady=10, fill="x")

# Diccionario de botones del teclado
key_buttons = {}

# Teclas simplificadas
keys = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', 'Space']
]

# Crear teclado visual
def crear_teclado():
    for fila in keys:
        fila_frame = tk.Frame(keyboard_frame)
        fila_frame.pack()
        for k in fila:
            btn = tk.Label(fila_frame, text=k, width=6, height=2, relief="raised", bg="white")
            btn.pack(side=tk.LEFT, padx=2, pady=2)
            key_buttons[k.lower()] = btn
crear_teclado()

# --- Mouse Visual Setup ---
left_btn = tk.Label(mouse_frame, text="Clic Izquierdo", width=20, relief="raised", bg="white")
left_btn.pack(pady=5)

midle_btn = tk.Label(mouse_frame, text="Botón central", width=20, relief="raised", bg="white")
midle_btn.pack(pady=5)

right_btn = tk.Label(mouse_frame, text="Clic Derecho", width=20, relief="raised", bg="white")
right_btn.pack(pady=5)

pos_label = tk.Label(mouse_frame, text="Posición: (0, 0)", width=40)
pos_label.pack(pady=10)

# --- Funciones de resaltado ---
def resaltar_tecla(k):
    k = k.lower()
    if k in key_buttons:
        btn = key_buttons[k]
        btn.config(bg="lightgreen")
        root.after(300, lambda: btn.config(bg="white"))

def resaltar_mouse(btn_widget):
    btn_widget.config(bg="lightblue")
    root.after(200, lambda: btn_widget.config(bg="white"))

# --- Listeners ---
def teclado_listener():
    def on_press(key):
        try:
            k = key.char if hasattr(key, 'char') and key.char else str(key)
        except:
            k = str(key)
        k = k.replace("'", "").replace("Key.", "")
        print(f"Tecla: {k}")
        resaltar_tecla(k)
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def mouse_listener():
    def on_click(x, y, button, pressed):
        if pressed:
            if button == mouse.Button.left:
                print("Clic izquierdo")
                resaltar_mouse(left_btn)
            elif button == mouse.Button.right:
                print("Clic derecho")
                resaltar_mouse(right_btn)
            else:
                print("Botón central")
                resaltar_mouse(midle_btn)
    def on_move(x, y):
        pos_label.config(text=f"Posición: ({x}, {y})")

    with mouse.Listener(on_click=on_click, on_move=on_move) as listener:
        listener.join()

# --- Iniciar listeners en hilos ---
threading.Thread(target=teclado_listener, daemon=True).start()
threading.Thread(target=mouse_listener, daemon=True).start()

# --- Iniciar GUI ---
root.mainloop()