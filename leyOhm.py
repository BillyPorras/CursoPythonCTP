print ('-----------------------')
print (' Programa de la Ley de Ohm')
print ('-----------------------')
print (' devby: BPM')

opcion = int(input('digite 1 para calcular el voltaje, 2 para calcular resistencia , 3 para calcular corrieente: '))

if opcion == 1:
    C = float(input('digite la corriente: '))
    R = float(input('digite la resistencia:: '))
    V= C * R
if opcion == 2:
    C = float(input('digite la corriente: '))
    V= float(input('digite la volteje:: '))
    R= V / C
if opcion == 3:
    V = float(input('digite el Voltaje: '))
    R = float(input('digite la Corriente: '))
    C =  V / R
    
print ('Resultados')
print (' el voltaje es: ', V, 'voltios')
print (' La  Corriente es: ',"{:.3f}".format(C), ' amperios')
print (' La  Resistencia  es: ', R, ' ohmios')
