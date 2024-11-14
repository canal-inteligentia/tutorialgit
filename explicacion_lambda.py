'''
EXPLICACIÓN LAMBDA
'''

numeros = [1,2,3,4,5,6,7,8,9,10]

desordenados = [(1,'a','Primero'),(5,'c','Segundo'), (19,'b','Tercero'), (192,'d','Cuarto')]
valores_ordenados = list(sorted(desordenados,key=lambda x:x[0]))
print(valores_ordenados)

añadir = lambda x,y: x + y

print(añadir(1,1))


'''cuadrados = list(map(cuadrado,numeros))
print(cuadrados)

cuadrados = list(map(lambda x : x**2,numeros))
print(cuadrados)'''

pares = list(filter(lambda  x : x%2 == 0,numeros))
print(pares)
