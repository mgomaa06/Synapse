from fastapi import FastAPI, UploadFile
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
    if file.content_type == "image/jpeg" or file.content_type == "image/png":
        image = Image.open(file.file)
        width, height = image.size
        return {"filename": file.filename,
                "height": height,
                "width": width}
    else:
        return "invalid file type"


if __name__ == "__main__":
    main()