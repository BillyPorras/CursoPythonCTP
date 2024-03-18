# Impresión de información inicial
print('-----------------------')
print(' Programa de la Ley de Ohm')
print('-----------------------')
print(' devby: BPM')

def calcular_voltaje(corriente, resistencia):
  """
  Calcula el voltaje a partir de la corriente y la resistencia.

  Args:
    corriente (float): La corriente en amperios (A).
    resistencia (float): La resistencia en ohmios (O).

  Returns:
    float: El voltaje en voltios (V).
  """
  return corriente * resistencia

def calcular_resistencia(corriente, voltaje):
  """
  Calcula la resistencia a partir de la corriente y el voltaje.

  Args:
    corriente (float): La corriente en amperios (A).
    voltaje (float): El voltaje en voltios (V).

  Returns:
    float: La resistencia en ohmios (O).
  """
  return voltaje / corriente

def calcular_corriente(voltaje, resistencia):
  """
  Calcula la corriente a partir del voltaje y la resistencia.

  Args:
    voltaje (float): El voltaje en voltios (V).
    resistencia (float): La resistencia en ohmios (O).

  Returns:
    float: La corriente en amperios (A).
  """
  return voltaje / resistencia

def main():
  """
  Función principal del programa.
  """
  while True:
    # Solicitud de la opción al usuario
    opcion = input('Digite 1 para calcular el voltaje, 2 para calcular resistencia, 3 para calcular corriente, o "fin" para salir: ')

    # Validación de la opción
    if opcion.lower() == 'fin':
      break
    elif not opcion.isdigit() or int(opcion) not in range(1, 4):
      print('Opción no válida. Ingrese un número entre 1 y 3, o "fin" para salir.')
      continue

    # Cálculo de la variable seleccionada
    opcion = int(opcion)
    if opcion == 1:
      # Cálculo del voltaje
      corriente = float(input('Digite la corriente (amperios): '))
      resistencia = float(input('Digite la resistencia (ohmios): '))
      voltaje = calcular_voltaje(corriente, resistencia)
    elif opcion == 2:
      # Cálculo de la resistencia
      corriente = float(input('Digite la corriente (amperios): '))
      voltaje = float(input('Digite el voltaje (voltios): '))
      resistencia = calcular_resistencia(corriente, voltaje)
    elif opcion == 3:
      # Cálculo de la corriente
      voltaje = float(input('Digite el voltaje (voltios): '))
      resistencia = float(input('Digite la resistencia (ohmios): '))
      corriente = calcular_corriente(voltaje, resistencia)

    # Impresión de los resultados
    print('Resultados')
    print('El voltaje es:', "{:.3f}".format(voltaje), 'voltios')
    print('La corriente es:', "{:.3f}".format(corriente), 'amperios')
    print('La resistencia es:', "{:.3f}".format(resistencia), 'ohmios')

if __name__ == '__main__':
  main()
