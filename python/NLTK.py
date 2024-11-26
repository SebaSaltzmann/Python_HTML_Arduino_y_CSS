# Instala NLTK si no lo tienes instalado
# pip install nltk

import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

# Descargar recursos necesarios de NLTK
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

# Texto de ejemplo
texto = """
El Procesamiento del Lenguaje Natural (NLP) es una rama de la inteligencia artificial 
que ayuda a las computadoras a comprender, interpretar y manipular el lenguaje humano.
"""

# Tokenización: dividir el texto en palabras
tokens = word_tokenize(texto)
print("Tokens:", tokens)

# Etiquetado gramatical (Part of Speech Tagging)
tags = nltk.pos_tag(tokens)
print("\nEtiquetado gramatical:", tags)

# Remover palabras vacías (stopwords)
stop_words = set(stopwords.words('spanish'))
tokens_sin_stopwords = [word for word in tokens if word.lower() not in stop_words]

print("\nTokens sin palabras vacías:", tokens_sin_stopwords)

# Análisis de frecuencia de palabras
frecuencia = FreqDist(tokens_sin_stopwords)
print("\nPalabras más frecuentes:")
for palabra, frecuencia in frecuencia.most_common(5):
    print(f"{palabra}: {frecuencia}")

# Generar un gráfico de frecuencia (opcional)
frecuencia.plot(5, title="Palabras más frecuentes (sin stopwords)")
