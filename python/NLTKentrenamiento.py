import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import random

# Frases de ejemplo para entrenamiento
training_data = [
    ("hola, ¿cómo estás?", "saludo"),
    ("buenos días", "saludo"),
    ("chau, que andes bien", "despedida"),
    ("nos vemos luego", "despedida"),
    ("¿qué hora es?", "pregunta"),
    ("¿dónde estás?", "pregunta"),
]

stop_words = set(stopwords.words('spanish'))

def tokenize_and_filter(sentence):
    words = word_tokenize(sentence.lower())
    return {word: True for word in words if word.isalpha() and word not in stop_words}

# Procesar datos
features = [(tokenize_and_filter(text), label) for (text, label) in training_data]

# Entrenar modelo
classifier = nltk.NaiveBayesClassifier.train(features)

# Probar con nueva frase
def responder(frase):
    features = tokenize_and_filter(frase)
    etiqueta = classifier.classify(features)
    
    if etiqueta == "saludo":
        return "¡Hola! ¿En qué puedo ayudarte?"
    elif etiqueta == "despedida":
        return "¡Hasta luego! Que tengas un buen día."
    elif etiqueta == "pregunta":
        return "Buena pregunta, déjame pensarlo..."
    else:
        return "No entendí eso, ¿podés reformularlo?"

# Ejemplo de uso
while True:
    entrada = input("Usuario: ")
    if entrada.lower() == "salir":
        break
    respuesta = responder(entrada)
    print("AI:", respuesta)
