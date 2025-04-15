import sqlite3

# Conexión a la base de datos (o creación si no existe)
conexion = sqlite3.connect("mi_base.db")

# Crear un cursor para interactuar con la base de datos
cursor = conexion.cursor()

# Crear una tabla llamada 'usuarios'
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER,
    correo TEXT UNIQUE NOT NULL
)
''')

# Guardar los cambios y cerrar la conexión
conexion.commit()
conexion.close()

print("Base de datos y tabla creadas correctamente.")
