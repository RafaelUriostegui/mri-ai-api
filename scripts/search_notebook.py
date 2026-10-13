import json   # librería estándar de Python para leer JSON
import sys    # da acceso a los argumentos que escribes en la terminal

# Palabras que buscamos y por qué:
PALABRAS = [
    "names",        # nombres de clases (p. ej. features["label"].names)
    "label",        # cómo se definen o convierten las etiquetas
    "map",          # remapeos tipo {"AD": 0, "HC": 1}
    "255",          # normalización de píxeles
    "resize",       # redimensionado a 128x128
    "convert",      # conversión a escala de grises (p. ej. .convert("L"))
    "compile",      # configuración de entrenamiento
    "from_logits",  # confirma que la salida son logits
    "save",         # dónde se guardó el modelo
]

ruta = sys.argv[1]   # sys.argv es la lista de lo que escribiste después de "python";
                     # [0] es el nombre del script, [1] es lo primero que le pasas

with open(ruta, encoding="utf-8") as f:   # abre el archivo y lo cierra solo al terminar
    notebook = json.load(f)               # convierte el texto JSON en diccionarios y listas de Python

for numero, celda in enumerate(notebook["cells"], start=1):   # enumerate te da el índice y el elemento
    if celda["cell_type"] != "code":
        continue                          # salta las celdas de texto
    for linea in celda["source"]:
        if any(p in linea for p in PALABRAS):              # ¿la línea contiene alguna palabra?
            print(f"[celda {numero}] {linea.rstrip()}")    # rstrip() quita el salto de línea final