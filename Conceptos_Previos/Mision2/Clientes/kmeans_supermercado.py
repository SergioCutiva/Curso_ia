import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D


#===========================
# 1. Carga de datos
#===========================
df = pd.read_csv('clientes_supermercado.csv')
print(df)

#==================================
# Redondear antes de convertir a int
#==================================

df['Edad'] = df['Edad'].round().astype(int)
df['VisitasPorMes']=df['VisitasPorMes'].round().astype(int)
print(df)
x = df[['Edad','GastoMensual','VisitasPorMes']]

#=======================================
# Metodo del codo
#=======================================
inertias=[]
k_range = range(1,10)
for k in k_range:
    kmeans=KMeans(n_clusters=k,random_state=42)
    kmeans.fit(x)
    inertias.append(kmeans.inertia_)

plt.figure(figsize=(6,4))
plt.plot(k_range,inertias,marker='o')
plt.xlabel('Numero de cluster')
plt.ylabel('Inercia')
plt.title('Metodo del codo Sergmentación de clientes')
plt.show()