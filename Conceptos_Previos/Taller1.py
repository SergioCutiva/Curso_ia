import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dataset ficticio
datos_estudiantes = {
    "peso": pd.Series([55, 68, 74, 60, 72], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "altura": pd.Series([162, 175, 168, 180, 170], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "promedio": pd.Series([4.5, 3.8, 4.2, 2.9, 3.5], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "edad": pd.Series([17, 18, 17, 19, 18], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"])
}

df = pd.DataFrame(datos_estudiantes)
print(df)

#Crear una Serie con los nombres y alturas de los estudiantes

alturas_estudiantes = pd.Series([162, 175, 168, 180, 170], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"])

# Pregunta: ¿Cuál es la altura de Daniela?

df_Daniela = df.loc["Daniela", "altura"]
print(f"La altura de Daniela es: {df_Daniela} cm")

df_Daniela2 = pd.DataFrame(datos_estudiantes,columns=["altura"], index=["Daniela"])
print(df_Daniela2)

# Accede al promedio de calificación de Carlos de 3 formas diferentes
df_Carlos = df.loc["Carlos", "promedio"]
print(f"El promedio de Carlos es: {df_Carlos}")

df_Carlos2 = pd.DataFrame(datos_estudiantes, columns=["promedio"], index=["Carlos"])
print(df_Carlos2)

df_Carlos3 = df.iloc[1, 2]  # Carlos es el segundo estudiante, promedio es la tercera columna
print(f"El promedio de Carlos es: {df_Carlos3}")

df_Carlos4 = df["promedio"]["Carlos"]
print(f"El promedio de Carlos es: {df_Carlos4}")

df_Carlos5 = df.query("index == 'Carlos'")["promedio"]
print(f"El promedio de Carlos es: {df_Carlos5}")

# Filtra a los estudiantes con promedio mayor o igual a 4.0
estudiantes_buenos = df[df["promedio"] >= 4.0]
print("Estudiantes con promedio mayor o igual a 4.0:")
print(estudiantes_buenos)

estudiantes_buenos2 = df.query("promedio >= 4.0")
print(estudiantes_buenos2)

# Pregunta: ¿Cuántos estudiantes tienen un buen promedio?
cantidad_buenos = estudiantes_buenos.shape[0]
print(f"Cantidad de estudiantes con buen promedio: {cantidad_buenos}")

cantidad_buenos2 = df.query("promedio >= 4.0").shape[0]
print(f"Cantidad de estudiantes con buen promedio: {cantidad_buenos2}")

#Agrega una nueva columna que indique si el estudiante es mayor de edad

df["mayor_de_edad"] = df["edad"] >= 18
print("DataFrame con la nueva columna 'mayor_de_edad':")    
print(df)

# Agrega una columna con el año de nacimiento (suponiendo que estamos en 2025)
df["año_nacimiento"] = 2025 - df["edad"]
print("DataFrame con la nueva columna 'año_nacimiento':")
print(df)

# Visualiza los promedios de los estudiantes en un gráfico
df["promedio"].plot(kind="bar", title="Promedio de estudiantes")
plt.xlabel("Estudiante")
plt.ylabel("Nota promedio")
#plt.show()

# Filtra a los estudiantes con altura entre 165 y 175 cm

estudiantes_altos = df[(df["altura"] >= 165) & (df["altura"] <= 175)]
print("Estudiantes con altura entre 165 y 175 cm:")
print(estudiantes_altos)

estudiantes_altos2 = df.query("altura >= 165 and altura <= 175")
print(estudiantes_altos2)

# Copia el DataFrame y elimina la columna "peso"
df_copia = df.copy()
del df_copia["peso"]
print("DataFrame copia sin la columna 'peso':")
print(df_copia)

# Crea un nuevo DataFrame con solo 3 columnas: nombre, edad y año de nacimiento
df_nuevo = df[["edad", "año_nacimiento"]].copy()
#df_nuevo.index = df.index  # Mantener los mismos índices
print("Nuevo DataFrame con solo 'edad' y 'año_nacimiento':")
print(df_nuevo)


