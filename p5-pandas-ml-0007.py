import numpy as np
import pandas as pd
# Alexandro Aguilar NC 0007
## datos matriz 4 x 3
datos_alumno = [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
# poner nombre a las columnas
# y almacenar la tabla en la variable df (DataFrame)
print("---- Datos a partir de una matriz de 4 x 3 ----")
df = pd.DataFrame(datos_alumno,columns=['ci', 'marcas', 'paquete'])
print(df)
# datos a partir de un diccionario
print("---- Datos a partir de un diccionario ----")
alumno_diccionario = {
    "nombre": ["Caleb", "Yahir", "Lia", "Meredith", "Abril", "Anaely"],
    "califa": [70, 30, 90, 80, 100, 100],
    "Edad": [15, 16, 15, 15, 16, 16]
}
estudiantes = pd.DataFrame(alumno_diccionario)
print(estudiantes)
print("Alexandro Aguilar NC 0007")

