from fastapi import APIRouter, HTTPException, UploadFile

from app.models.inference import InferenceResponse
from app.services.inferenceService import predict_image

router = APIRouter()


@router.post("/uploadfile/", response_model=InferenceResponse)
async def create_upload_file(file: UploadFile) -> InferenceResponse:
    if file.content_type != "image/jpeg" and file.content_type != "image/png":
        raise HTTPException(status_code=400, detail= "invalid image file")
    
    image_bytes =await file.read()

    if len(image_bytes) == 0:
        raise HTTPException(status_code = 400, detail= "empty file")
    
    prediction, confidence = predict_image(image_bytes)

    return InferenceResponse(filename= file.filename, prediction = prediction, confidence = confidence)