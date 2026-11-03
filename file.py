import sqlite3

def registrar_maquina(nombre, tipo):
    conexion = sqlite3.connect('industria.db')
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO maquinaria (nombre, tipo) VALUES (?, ?)", (nombre, tipo))
    conexion.commit()
    print(f"Maquina {nombre} registrada exitosamente.")