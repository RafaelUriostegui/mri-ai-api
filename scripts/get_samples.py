from pathlib import Path

from datasets import load_dataset

HC_LABEL = 2        # en el dataset original, 2 = "Non Demented" (ver celda 8 del notebook)
N_POR_CLASE = 3     # cuántas imágenes guardar de cada clase

carpeta = Path("samples")          # Path representa una ruta y funciona igual en Windows y Linux
carpeta.mkdir(exist_ok=True)       # crea la carpeta; exist_ok=True evita error si ya existe

ds = load_dataset("Falah/Alzheimer_MRI", split="test")   # solo el split de test

conteo = {"hc": 0, "ad": 0}

for item in ds:
    clase = "hc" if item["label"] == HC_LABEL else "ad"   # mismo mapeo binario que el notebook

    if conteo[clase] >= N_POR_CLASE:
        continue                   # ya tenemos suficientes de esta clase: salta a la siguiente imagen

    conteo[clase] += 1
    nombre = f"{clase}_{conteo[clase]}_orig{item['label']}.png"
    item["image"].save(carpeta / nombre)                  # el operador / une rutas con Path

    if all(n >= N_POR_CLASE for n in conteo.values()):
        break                      # ya tenemos todas: sale del ciclo

print("Guardadas:", conteo)