# Introducción Pandas
```
python 3.13.5
```
# Creación de objeto Serie
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
s = pd.Series([2,4,6,8,10])
print(s)
# Creación de un objeto Serie inicializando con un diccionario de python
altura = {"Santiago":180,"Marcelo":172,"Luis":174,"Alejandra":160}
s = pd.Series(altura)
print(s)
"""
Creación de un objeto series inicializandolo con algunos elementos
de un diccionario de python
"""
altura = {"Santiago":180,"Marcelo":172,"Luis":174,"Alejandra":160}
s = pd.Series(altura, index=["Marcelo","Luis"])
print(s)

# Creación de un objeto Serires inicializando con un escalar
s = pd.Series(34,["test1","test2","test3"])
print(s)
```