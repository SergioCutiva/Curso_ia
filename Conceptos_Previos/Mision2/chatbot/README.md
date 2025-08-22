## Trabajo con linux en windows

cmd como admini
```
wsl --install
```

|Libreria    |Comando                  |
|------------|-------------------------|
|transformers|pip install tranosformes |
|torch       |pip install torch        |


pip install huggingface_hub[hf_xet]

```
codigo de ejemplo 1

from transformers import pipeline

#crear un pepeline de análisis de sentimiento
clasificador = pipeline ('sentiment-analysis')
clasificador2 = pipeline ('sentiment-analysis')
# análisar un sentencia
resultado= clasificador("Me encanta usar la librería trasnformers de hugging face!")
print(resultado)
resultado2=clasificador2("no me gusta trabajar los sabado")
print(resultado2)


```

