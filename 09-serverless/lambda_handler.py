import json
import numpy as np
from io import BytesIO
from urllib import request
from PIL import Image
import onnxruntime as ort

session = ort.InferenceSession("hair_classifier_empty.onnx")
input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name


def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    return Image.open(stream)


def prepare_image(img, target_size=(128, 128)):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img


def preprocess(img):
    img = np.array(img) / 255.0          # scale to [0,1]
    img = img.transpose(2, 0, 1)         # HWC → CHW
    img = img.astype(np.float32)         # <<< IMPORTANT FIX
    img = np.expand_dims(img, 0)         # batch dimension
    return img


def lambda_handler(event, context=None):
    url = event["url"]

    img = download_image(url)
    img = prepare_image(img)
    x = preprocess(img)

    pred = session.run([output_name], {input_name: x})[0]
    pred_value = float(pred[0][0])

    return {"prediction": pred_value}
