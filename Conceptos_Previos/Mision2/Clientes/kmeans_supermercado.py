import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D


# Cargar datos
df = pd.read_csv('clientes_supermercado.csv')
print(df)

# Redondear antes de convertir en int

df['Edad'] = df['Edad'].round().astype(int)
df['VisitasPorMes']=df['VisitasPorMes'].round().astype(int)
print(df)