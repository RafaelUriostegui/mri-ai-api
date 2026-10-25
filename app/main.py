from fastapi import FastAPI, UploadFile
from app.model import predict
from app.preprocessing import preprocess_image

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
async def predicting(archivo: UploadFile):
    contenido = await archivo.read()
    x = preprocess_image(contenido)
    resultado = predict(x)
    return resultado