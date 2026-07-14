from fastapi import FastAPI, UploadFile, HTTPException
from PIL import Image
from pydantic import BaseModel

def main():
    print("Hello from synapse-mentorship-summer-2026!")

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

class InferenceResponse(BaseModel):
    filename: str
    prediction: str
    confidence: float

class ImageMetadata(BaseModel):
    filename: str
    height: int
    width: int

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile, response = ImageMetadata):
    if file.content_type != "image/jpeg" and file.content_type != "image/png":
        raise HTTPException(status_code=400, detail= "invalid image file")
    image = Image.open(file.file)
    width, height = image.size
    return {"filename": file.filename,
                "height": height,
                "width": width}


if __name__ == "__main__":
    main()