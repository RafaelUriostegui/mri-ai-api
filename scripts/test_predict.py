from pathlib import Path

from app.model import predict
from app.preprocessing import preprocess_image

for ruta in sorted(Path("samples").glob("*.png")):   # glob busca archivos que coincidan con el patrón
    x = preprocess_image(ruta.read_bytes())          # read_bytes() lee el archivo como bytes
    resultado = predict(x)
    print(f"{ruta.name:20} → {resultado}")           # :20 rellena el nombre a 20 caracteres para alinear