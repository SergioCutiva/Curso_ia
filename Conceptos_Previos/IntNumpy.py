import numpy as np
import matplotlib.pyplot as plt
# Matriz de 2 filas y 4 columnas con ceros
a = np.zeros((2,4))
print(a)
# Matriz de 2 filas y 4 columnas con unos
b = np.ones((2,4))
print(b)

# Imprimir las dimensiones de la matriz
print(f"Dimensiones de la matriz a: {a.shape}")
print(f"Dimensiones de la matriz b: {b.shape}") 

# numero de dimensiones de la matriz
print(f"Número de dimensiones de la matriz a: {a.ndim}")
print(f"Número de dimensiones de la matriz b: {b.ndim}")

# Imprimir el tamaño de la matriz
print(f"Tamaño de la matriz a: {a.size}")
print(f"Tamaño de la matriz b: {b.size}")

# Array o matriz cuyos valores son todos el valor indicado como segundo parámetro de la función
c = np.full((2,3,4), 8)
print(c)
print(f"Número de dimensiones de la matriz c: {c.ndim}")

# Inicializa los valores del array con lo que haya en memoria
# El llenado del empty es aleatorio
#d = np.empty((2,3,9))
#print(d)

# Inicializacion del array usando uno de python
e = np.array([[1,2,3],[4,5,6]])
print(e)
 
# Creacion del array utilizando una funcion basada en rangos
# (minimo,maximo,numero de elementos del array)
f = np.linspace(0,6,10)
print(f)

# inicializacion del array con valores aleatorios
g = np.random.random((2,3,4))
print(g)

# Inicializacion del array con valores aleatorios con forme a una distribución normal
h = np.random.rand(2,4)
print(h)

# Histograma con valores aleatorios
g = np.random.rand(100)
print(g)

#plt.hist(g, bins=100, density=True)
#plt.title("Histograma de valores aleatorios")
#plt.xlabel("Valor")
#plt.ylabel("Frecuencia")
#plt.show()

# Histogramas con valores personalizados
h = np.array([1,2,3,2,2,2,4,5,6,7,8])
plt.hist(h, bins=15, density=True)
plt.title("Histograma de valores personalizados")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
#plt.show()

# Inicialización de un array usando una función
def func(x, y):
    return (x +2) *y
i = np.fromfunction(func, (3, 5), dtype=int)
print(i)