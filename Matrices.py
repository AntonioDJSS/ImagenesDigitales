import numpy as np
#Arreglo unidimensional
a = np.array([1,2,3,4,5,7])
print("\n",'Arreglo Unidimensional')
print(a,'a')
#Arreglo bidimensional
b = np.array([(1,7,8,9),(6,7,8,9)])
print("\n",'Arreglo Bidimensional')
print(b,'b')
#arreglo
unos = np.ones((3,2))
ceros = np.zeros((3,2))
print("\n",'Arreglo')
print(unos)
print("\n",ceros)
arregloOchos = np.full((3,2),8)
print("\n",arregloOchos)
c = np.array([(3,4,7,8),(7,9,3,2)])
print(c,"c")
#Operacion con matrices
print("\n",'SUMA')
print(b+c)
print("\n",'RESTA')
print(b-c)
print("\n",'MULTIPLICACION')
print(b*c)

#Matriz Identidad
identidad = np.identity(3)
print("\n",'Matriz Identidad')
print(identidad)

print('\nMINIMO\n', b.min())
print('MAXIMO\n',b.max())
print('SUMATORIA\n',b.sum())
print('\nDesviacion Estandar\n',np.std(b)) 
