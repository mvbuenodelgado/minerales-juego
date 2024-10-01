import os
import random
from PIL import Image
import matplotlib.pyplot as plt

# Función para seleccionar y mostrar una imagen aleatoria desde el directorio actual
def mostrar_imagen_aleatoria(directorio):
    imagenes = [archivo for archivo in os.listdir(directorio) if archivo.endswith(('.png', '.jpg', '.jpeg'))]
    imagen_aleatoria = random.choice(imagenes)
    
    # Mostrar la imagen
    ruta_imagen = os.path.join(directorio, imagen_aleatoria)
    imagen = Image.open(ruta_imagen)
    plt.imshow(imagen)
    plt.axis('off')
    plt.show()

    return imagen_aleatoria

# Función principal del juego
def juego_minerales(directorio):
    imagen_aleatoria = mostrar_imagen_aleatoria(directorio)
    respuesta = input("¿Cuál es el nombre del mineral? (Recuerda escribirlo todo en minúsculas) ")
    nombre_correcto = os.path.splitext(imagen_aleatoria)[0]

    if respuesta.lower() == nombre_correcto.lower():
        print("¡Correcto!")
    else:
        print(f"Incorrecto. El nombre correcto es: {nombre_correcto}")

# Solicitar al usuario la ruta del directorio
directorio = input("Introduce la ruta del directorio donde están las imágenes: ")

# Ejecutar el juego
juego_minerales(directorio)
