from fastapi import HTTPException, UploadFile
from PIL import Image, UnidentifiedImageError
from torchvision import transforms
from torchvision.transforms import InterpolationMode
from io import BytesIO
import torch

from torchvision.models import (MobileNet_V3_Large_Weights, mobilenet_v3_large)

from app.models.inference import InferenceResponse

WEIGHTS = MobileNet_V3_Large_Weights.IMAGENET1K_V2
model = mobilenet_v3_large(weights = WEIGHTS)
model.eval()
PREPROCESS = transforms.Compose(
    [
        transforms.Resize(232, interpolation=InterpolationMode.BILINEAR),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean = [0.485, 0.456, 0.406],
            std = [0.229, 0.224, 0.225]
        )
    ]
)
CATEGORIES = WEIGHTS.meta["categories"]

def predict_image(image_bytes: bytes) -> tuple[str, float]:
    try:
        with Image.open(BytesIO(image_bytes)) as image:
            image = image.convert("RGB")
            input_tensor = PREPROCESS(image)

    except (UnidentifiedImageError, OSError) as exc:
        raise InvalidImageError("This is not a valid image") from exc

    input_batch = input_tensor.unsqueeze(0)

    with torch.inference_mode(): output = model(input_batch)
    
    probabilities = torch.softmax(output[0], dim=0)

    confidence, class_index = probabilities.max(dim=0)

    prediction = CATEGORIES[class_index.item()]

    return prediction, confidence.item()