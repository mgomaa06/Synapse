from fastapi import FastAPI, UploadFile
from PIL import Image

def main():
    print("Hello from synapse-mentorship-summer-2026!")

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    image = Image.open(file.file)
    width, height = image.size
    return {"filename": file.filename,
            "height": height,
            "width": width}

if __name__ == "__main__":
    main()