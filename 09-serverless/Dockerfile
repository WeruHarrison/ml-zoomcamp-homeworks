FROM agrigorev/model-2025-hairstyle:v1

# Install Python libs
RUN pip install numpy pillow onnxruntime

# Copy inference code
COPY lambda_handler.py .

CMD ["lambda_handler.lambda_handler"]
