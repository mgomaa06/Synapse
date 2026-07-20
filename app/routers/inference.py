from fastapi import APIRouter, HTTPException, UploadFile

from app.models.inference import InferenceResponse
from app.services.inferenceService import run_inference

router = APIRouter()


@router.post("/uploadfile/", response_model=InferenceResponse)
async def create_upload_file(file: UploadFile) -> InferenceResponse:
    if file.content_type != "image/jpeg" and file.content_type != "image/png":
        raise HTTPException(status_code=400, detail= "invalid image file")
    if file.size == 0:
        raise HTTPException(status_code = 400, detail= "empty file")

    return run_inference(file)