import keras
import numpy as np 

MODEL_PATH = "models/model_cnn.keras"
CLASS_NAMES = ["HC", "AD"]

model = keras.models.load_model(MODEL_PATH, compile=False)  # compile=False evita que se intente compilar el modelo al cargarlo

def predict(x: np.ndarray) -> dict:
    """Recibe el tensor preprocesado y la etiqueta y las probabilidades"""
    logits = model(x, training=False)
    probs = np.asarray(keras.ops.softmax(logits))[0]
    idx = np.argmax(probs)
    label = CLASS_NAMES[idx]
    probabilities = {n: float(p) for n, p in zip(CLASS_NAMES, probs)}

    return {"label": label, "probabilities": probabilities}