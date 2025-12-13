# Homework 09 – Serverless

This repo contains my solution and reflection for [Module 9 – Serverless](https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/09-serverless) of the [Machine Learning Zoomcamp](https://courses.datatalks.club/ml-zoomcamp-2025/) by Datatalks Club led by [Alexey Grigorev](https://www.linkedin.com/in/agrigorev/). The module was about deploying deep learning models in the cloud, AWS Lambda specifically. It also touched on creating web APIs that can be used to interact with the deep learning models. In the homework, I deployed a deep learning image classification model (Straight vs Curly Hair) as a serverless service using AWS Lambda–compatible Docker images. The task focused on running inference with a pre-trained ONNX model, applying the correct image preprocessing pipeline, and packaging everything in a Lambda-ready container that can be tested locally and deployed to AWS.

---

## 🧩 What I Did

I inspected the ONNX model to identify the correct input and output node names, then implemented the same image preprocessing steps used during training (e.g. resizing to 200×200, RGB conversion, normalization with ImageNet mean and standard deviation, and channel reordering). I then wrote a Lambda handler in Python that downloads an image from a URL, preprocesses it, runs inference using ONNX Runtime, and returns the model output. I then extended a prebuilt Lambda-compatible Docker image that already contained the model, installed the required dependencies, and verified the service locally using the AWS Lambda Runtime Interface Emulator.

---

## 🧩 What I Learned

I learned how to deploy deep learning models in a serverless setting using container images instead of traditional ZIP-based Lambda deployments. I gained practical experience with ONNX Runtime for inference, strict data type handling (float32 vs float64), and Lambda-specific requirements such as handler definitions and container entry points. This homework also reinforced how important it is to exactly match training-time preprocessing during deployment to avoid incorrect predictions or runtime errors.

---

## 🧰 Tools and Libraries

- **ONNX Runtime** 
- **NumPy**
- **Pillow (PIL)**
- **Docker**
- **AWS Lambda Runtime Interface Emulator** (via local Docker run) 

---

## Final Thoughts

This module emphasized that modern machine learning is not complete without efficient and scalable deployment. Serverless platforms like AWS Lambda show how models can be exposed as lightweight and on-demand services without managing infrastructure.

---

