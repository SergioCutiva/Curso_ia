import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # pip install seaborn

titanic = pd.read_csv('titanic.csv')

# Imprimir las primeras 5 filas
print(titanic.head())


"""
1.Generar un dataframe con los datos del fichero titanic.csv
2.Hacer el tratamiento de los nulos
3.Mostrar por pantalla las dimensiones del dataframe,el numero de datos que contiene,
los nombres de sus columnas y filas, los tipos de datos de las columnas,
las 10 primeras filas y las 10 ultimas filas
4.Mostrar por pantalla los datos del pasajero con identificador 148
5.Mostrar por pantalla las filas pares del dataframe
6.Mostrar por pantalla el nombre de las personas que iban en primera clase 
ordenadas alfabeticamente
7.Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase
8.Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase
9.Añadir una nueva columna boleana para saber si el pasajero era menor de edad o no
10.Mostrar por pantalla el porcentaje de mayores y menores de edad que sobrevivieron
en cada clase
11.Mostrar por pantalla el porcentaje de mayores de edad que sobrevivieron en cada clase
"""

# Imprimo las columnas
print(titanic.columns)

# Imprimimos la suma de nulos por columna
print(titanic.isnull().sum())

#Tratamiento de nulos
#1. Rellenar los valores de la edad(Age) con la media
if 'Age' in titanic.columns:
    titanic['Age'].fillna(titanic['Age'].mean(),inplace=True)

#2. Como la columna cabin tiene muchos nulos, validamos si tiene mas de la mitad de los calores nulo y si es verdad elimnar la columna
if 'Cabin' in titanic.columns and titanic['Cabin'].isnull().sum()/len(titanic)>0.5:
    #Borramos la columna
    titanic.drop('Cabin',axis=1,inplace=True)

#3. Rellenar puerto de embarque (embarked) con la moda 
if 'Embarked' in titanic.columns:
    titanic['Embarked'].fillna(titanic['Embarked'].mode()[0],inplace=True)

# Imprimimos nuevamente la suma de nulos por columna
print(titanic.isnull().sum())

# Histograma de las edades
plt.figure(figsize=(8,5))
sns.histplot(titanic['Age'],bins=30,color='skyblue')
plt.title("Frecuencia de la edad de los pasajeros")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.show()

# Diagram de cajas de la edad por la clase
plt.figure(figsize=(8,5))
sns.boxplot(x='Pclass', y='Age',data=titanic,palette='Set2')
plt.title("Distribucion de la edad por clase")
plt.xlabel("Clase")
plt.ylabel("Edad")
plt.show()

# Diagrama de correlación seleccionado solo las columnas numericas
df_numerico = titanic.select_dtypes(include='number')
correlacion_matriz = df_numerico.corr()
plt.figure(figsize=(8,5))
sns.heatmap(correlacion_matriz,annot=True,cmap='coolwarm')
plt.title("Distribucion de la edad por clase")
plt.xlabel("Clase")
plt.ylabel("Edad")
plt.show()

# Diagrama de sectires de fallecidos y sobrevivientes
plt.figure()
titanic.Survived.value_counts().plot(kind='pie',labels=['Muertos','Sobrevivientes'],title='Diagrama de torta de % de vivos y muertos',autopct='%1.1f%%')
plt.show()

# Diagrama de barras con el numero de personada de cada clase
plt.figure()
titanic.Pclass.value_counts().plot(kind='bar',title='Numero de personas por clase')
plt.show()

print('Dimensiones:', titanic.shape)
print('Numero de elementos:',titanic.size)
print('Nombre de filas:',titanic.index)
print('Numero de elementos:',titanic.dtypes)
print('Primeras 10 filas:',titanic.head(10))
print('Ultimas 10 filas:',titanic.tail(10))

# Pasajero 148
print(titanic.query('PassengerId == 148'))