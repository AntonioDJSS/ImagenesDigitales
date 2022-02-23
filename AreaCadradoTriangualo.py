#Variables
entero = 45
flotante = 10.2
cadena = 'Jesus'
boleano = True

#Conversion de datos
entero = int(flotante)
print(entero)
flotante = float(entero)
print(entero)
Cadena2 = str(45)
print(Cadena2)

hola = type(Cadena2)
print(hola)

print('Esto es una cadena')
print('Hola mundo')
print(entero)
print(flotante)
print(cadena)
print(boleano)

#Operadores Aritmeticos
# + - * / % **

print(2 + 2)
print(3 - 5)
print(3 * 3)
print(4 % 3)
print(3 ** 3)

suma = 3 + 3
print(suma)

entradaTeclado = input('Hola bb')
print(entradaTeclado)
#---------------------------------------------------------------------------------------------------------------------------------------------------
#Realice un programa que calcule el area de un triangulo y el area de un cuadrado.

print('¿Que quieres calcular?')
dato = int(input('\nArea de un triangulo (Selecciona 1)\nArea del cuadrado: (Selecciona 2): '))

def calculadoraTriangulo(base, altura, areaTriangulo):
  base = float(input('\nInserta la base de tu triangulo: '))
  altura = float(input('Inserta la altura de tu triangulo: '))
  areaTriangulo = (base * altura) / 2
  print('La base de tu triangulo es: {}'.format(areaTriangulo))    
  return

def calculadoraCuadrado(baseCuadrado, multi):
  baseCuadrado = int(input('\nInserta un lado de tu cuadrado: '))
  multi  = (baseCuadrado * baseCuadrado)
  print('El area de tu triangulo es: {}'.format(multi)) 
  return

if dato == 1:
  print(calculadoraTriangulo(base, altura, areaTriangulo))
elif dato == 2:
  print(calculadoraCuadrado(baseCuadrado, multi))
else:
  print('\nInsertaste mal el dato')


