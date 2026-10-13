import io

from PIL import Image
import numpy as np

IMG_SIZE = 128


def preprocess_image(image_bytes: bytes) -> np.ndarray:
    """Convierte los bytes de la imagen en el tensor que espera el modelo: (1, 128, 128, 1) acotada de [-1, 1]"""
    img = Image.open(io.BytesIO(image_bytes))
    img = img.convert("L").resize((IMG_SIZE, IMG_SIZE)) #Se lleva a escala de grises y se redimensiona a 128x128

    x = np.asarray(img, dtype="float32")/255 # normalización de píxeles a [0, 1]
    x = (x*2) - 1 # normalización de píxeles a [-1, 1]

    x = x.reshape((1, IMG_SIZE, IMG_SIZE, 1))  # reshape to (1, 128, 128, 1)

    return x
