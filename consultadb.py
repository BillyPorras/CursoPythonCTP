import yaml
import sqlite3


def ejecutar_consulta(archivo_yaml):
  """
  Esta función carga la configuración desde un archivo YAML y ejecuta la consulta,
  imprimiendo el valor de cada variable durante el proceso.

  Args:
      archivo_yaml (str): Ruta del archivo YAML con la consulta y conexión.

  Returns:
      list: Lista de resultados de la consulta.
  """

  # Carga de la configuración desde el archivo YAML
  with open(archivo_yaml, "r") as archivo:
      configuracion = yaml.safe_load(archivo)
      print("configuracion:", configuracion)  # Print configuration dictionary

  # Extracción de la información de conexión
  ruta_db = configuracion["conexion"]["ruta_db"]
  print("ruta_db:", ruta_db)  # Print database path

  # Conexión a la base de datos
  conexion = sqlite3.connect(ruta_db)
  print("conexion:", conexion)  # Print connection object

  # Extracción de la consulta
  consulta = configuracion["consulta"][0]  # Assuming single line consulta
  print("consulta:", consulta)  # Print the consulta string

  # Creación de un cursor
  cursor = conexion.cursor()
  print("cursor:", cursor)  # Print cursor object

  # Ejecución de la consulta
  cursor.execute(consulta)
  print("Ejecutando consulta:", consulta)  # Print message about execution

  # Obtención de los resultados
  resultados = cursor.fetchall()
  print("resultados:", resultados)  # Print the list of results

  # Cierre del cursor y conexión
  cursor.close()
  print("Cursor cerrado")  # Print message about cursor closure
  conexion.close()
  print("Conexion cerrada")  # Print message about connection closure

  return resultados


if __name__ == "__main__":
  archivo_consulta = "consulta.yaml"  # Replace with your actual YAML file path
  resultados = ejecutar_consulta(archivo_consulta)

  # Impresión de los resultados (unchanged)
  for fila in resultados:
      print(fila)
