import sqlite3  

conexion = sqlite3.connect("ControlDatos.db")
cursor = conexion.cursor()    # Consulta SQL
consulta = 'SELECT  *  FROM salida LIMIT 2'
cursor.execute(consulta)
resultados = cursor.fetchall()
cursor.close()
conexion.close()
# Impresión de los resultados
for fila in resultados:
    print(fila)
