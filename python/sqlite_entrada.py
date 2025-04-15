import sqlite3

# Conexión a la base de datos
conexion = sqlite3.connect("mi_base.db")
cursor = conexion.cursor()

# Insertar datos en la tabla
cursor.execute('''
INSERT INTO usuarios (nombre, edad, correo)
VALUES (?, ?, ?)
''', ("Juan Perez", 25, "juan.perez@email.com"))

# Guardar y cerrar
conexion.commit()
conexion.close()

print("Datos insertados correctamente.")
