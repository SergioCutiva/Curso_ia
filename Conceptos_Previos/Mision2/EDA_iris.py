import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()

df = pd.DataFrame(data=iris.data,columns=iris.feature_names)
df['species']=iris.target
df['species']= df['species'].map(dict(zip(range(3),iris.target_names)))

#imprimimos las primeras  5 filas
print(df.head())
#Tipos de datos de las columnas
print(df.info())


#EStadisticas descriptivas
print(df.describe())
      
# Cuantar cuantas flores hay de cada clase
especies_count = df['species'].value_counts()
print(especies_count)

plt.bar(especies_count.index,especies_count.values,color='skyblue')
plt.xlabel('Especie')
plt.ylabel('Cantidad')
plt.title('Distribucion de especies')
plt.show()


df['species']= iris.target
#Crear la matriz de correlacion
correlacion_matriz = df.corr()
sns.heatmap(correlacion_matriz,annot=True,cmap='coolwarm')
plt.title('correlacion entre variables')
plt.show()