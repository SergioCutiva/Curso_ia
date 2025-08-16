from transformers import pipeline

# Crear un pepline de analisis de sentimiento
clasificador = pipeline('sentiment-analysis')
# analizar una sentencia
resultado = clasificador('Me encanta usar la libreria transformers de python')
print(resultado)
resultado2 = clasificador('Estoy triste y no me gusta trabajar el sabado')
print(resultado2)
resultado3=clasificador('eres feo')
print(resultado3)
resultado4=clasificador('eres bonito')
print(resultado4)
resultado5 = clasificador('Me encanta usar la libreria transformes de python')
print(resultado5)
resultado6= clasificador('Me chimba conocerte')
print(resultado6)

clasificador2 = pipeline('sentimient-analysis')
