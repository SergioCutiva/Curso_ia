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

# Accesos a los elementos de un array
array_uni = np.array([1,3,5,7,9,11])
print("shape:", array_uni.shape)
print("array_uni:", array_uni)

# Acceso al quinto elemento
print("Quinto elemento:", array_uni[4])

# Accediendo a los elementos 0,3 y 5 del array
print("Elementos 0, 3 y 5:", array_uni[[0, 3, 5]])

# Array multidimensional
array_multi = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Array multidimensional:\n", array_multi)

# Accediendo al cuarto elemento del array multidimensional
print("Cuarto elemento del array multidimensional:", array_multi[1, 0])
# Accediendo a la segunda fila del array multidimensional
print("Segunda fila del array multidimensional:", array_multi[1, :])
# Accediendo al tercer elemento de las dos primeras filas
print("Tercer elemento de las dos primeras filas:\n", array_multi[0:2, 2])
# Modificación de un array
# Creaar un array unidimensional inicializando un rango de elementos del 0 al 27
array1 = np.arange(24)
print("Array original:", array1)
print("Shape del array original:", array1.shape)

# Camnbiar las dimensiones del array y sus longitudes
array2 = array1.reshape(6,4)
print("Array modificado:\n", array2)
print("Shape del array modificado:", array2.shape)

