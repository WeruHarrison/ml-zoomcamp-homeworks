FROM agrigorev/model-2025-hairstyle:v1

RUN pip install --no-cache-dir numpy pillow onnxruntime

COPY lambda_handler.py ./

CMD ["lambda_handler.lambda_handler"]
