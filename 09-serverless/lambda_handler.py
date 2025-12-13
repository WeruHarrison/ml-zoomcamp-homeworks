import numpy as np
from PIL import Image
from io import BytesIO
from urllib import request
import onnxruntime as ort

# ImageNet normalization (from HW08)
MEAN = np.array([0.485, 0.456, 0.406])
STD = np.array([0.229, 0.224, 0.225])

# Load ONNX model ONCE (cold start)
session = ort.InferenceSession(
    "hair_classifier_empty.onnx",
    providers=["CPUExecutionProvider"]
)

input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name


def preprocess_image(url):
    with request.urlopen(url) as resp:
        img = Image.open(BytesIO(resp.read()))

    if img.mode != "RGB":
        img = img.convert("RGB")

    img = img.resize((200, 200), Image.NEAREST)

    x = np.array(img).astype(np.float32) / 255.0
    x = (x - MEAN) / STD
    x = np.transpose(x, (2, 0, 1))
    x = np.expand_dims(x, axis=0)
    x = x.astype(np.float32)

    return x



def lambda_handler(event, context):
    url = event["url"]
    x = preprocess_image(url)
    pred = session.run([output_name], {input_name: x})[0]
    return float(pred[0][0])
