import tkinter as tk

# Ventana tkinter
ventana = tk.Tk()
palabra = tk.StringVar(ventana)
entrada = tk.StringVar(ventana)


# Dimensiones: Ancho x Alto
ventana.geometry("300x600")
ventana.configure(background="black")
tk.Wm.wm_title(ventana,"Lord Of Dragons")

def cambiarpalabra():
    palabra.set("chau" + entrada.get())

tk.Button(
    ventana,
    text="arriba",
    font=("Courier", 14),
    bg="gold",
    fg="white",
    command= cambiarpalabra,
    relief="flat"
).pack(
    fill=tk.BOTH,
    expand=True,
)

tk.Label(
    ventana,
    text="soy una etiqueta",
    textvariable=palabra,
    fg="white",
    bg="black",
    justify="center"
).pack(
    fill=tk.BOTH,
    expand=True,
)

tk.Entry(
    fg="white",
    bg="black",
    justify="center",
    textvariable=entrada
).pack(
    fill=tk.BOTH,
    expand=True,
)

ventana.mainloop()