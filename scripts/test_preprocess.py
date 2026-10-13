import sys

from app.preprocessing import preprocess_image

ruta = sys.argv[1]
with open(ruta, "rb") as f:        # "rb" = leer en modo binario: obtienes bytes, no texto
    contenido = f.read()

x = preprocess_image(contenido)
print("Forma:", x.shape)           # debe ser (1, 128, 128, 1)
print("Tipo:", x.dtype)            # debe ser float32
print("Mínimo:", x.min())          # debe ser >= -1
print("Máximo:", x.max())          # debe ser <= 1