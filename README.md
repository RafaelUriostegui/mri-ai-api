# mri-ai-api

REST API (FastAPI) that serves a CNN classifying brain MRI slices as
Alzheimer's disease (AD) or healthy control (HC).

> ⚠️ Educational project, not a clinical tool. Test accuracy ~75%.

## Requirements

- Python 3.11 (TensorFlow does not support Python 3.14 yet)

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run

```powershell
python -m uvicorn app.main:app --reload
```

Interactive docs at `http://127.0.0.1:8000/docs`.

## Endpoints

| Method | Route | Description |
|---|---|---|
| GET | `/health` | Service status check |
| POST | `/predict` | Upload an MRI image, get the predicted class and probabilities |

Example response from `/health`:

```json
{"status": "ok"}
```

Example response from `/predict`:

```json
{
  "label": "HC",
  "probabilities": {
    "HC": 0.7461723685264587,
    "AD": 0.2538275718688965
  }
}
```

## Notes

- Images are converted to 128×128 grayscale and normalized to [-1, 1] before inference, matching the training pipeline.
- Data: [Falah/Alzheimer_MRI](https://huggingface.co/datasets/Falah/Alzheimer_MRI) (Hugging Face).
- Model trained in a course lab.

## Next steps

- Input validation with clear error responses
- Automated tests (pytest)
- Docker
- Public demo
