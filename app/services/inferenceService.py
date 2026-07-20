from fastapi import HTTPException, UploadFile
from PIL import Image, UnidentifiedImageError

from app.models.inference import InferenceResponse


def run_inference(file: UploadFile) -> InferenceResponse:
    image = Image.open(file.file)
    image = image.convert("RGB")

    # Replace these two lines with your real model logic.
    prediction = "placeholder"
    confidence = 0.0

    return InferenceResponse(
        filename=file.filename or "unknown",
        prediction=prediction,
        confidence=confidence,
    )