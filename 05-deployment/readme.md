# Homework 05 - Deployment

This repo contains my solution and reflection for **Module 5 – Deployment** of the [Machine Learning Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/05-deployment) by Datatalks Club led by Alexey Grigorev.

The goal of the homework was to learn how to deploy machine learning models so they can be used to make predictions from different machines or applications without rerunning the entire training code each time.

---

## 🧰 Tools & Library
- Flask  
- FastAPI  
- Pipenv and uv  
- Docker  
- Pickle (for saving and loading models)

---

## 🧩 What I Did
I revisited the prediction model created in the previous modules and extended it to a deployable version. The main objective was to make the model accessible through a web API instead of manually running notebook every time the user wants to make predictions.

I started by training and saving the model as a serialized file using `Pickle.` Saving the model this way ensures that it could be loaded later for inference without retraining.

Next, I learned how to create API endpoints using both Flask and FastAPI. These endpoints accept input data from external systems and return predictions in a browser setting. However, I realized it was not as easy as it seams.

There are several deployment methods used to manade dependencies to make the model run in different environments and machines:
- **Pipenv and uv:** Used to create isolated environments that manage dependencies safely.  
- **Docker:** Used to package the entire service (model + dependencies + runtime) into a single container image to all deployment to servers or the cloud.
---

## Final Thoughts
This module highlighted that a good model must be usable in production. Deployment bridges the gap between model development and real-world application. I learned how packaging tools like Docker and dependency managers like Pipenv and uv ensure consistency and scalability across environments. I also realized that API-based model serving is the backbone of real-time predictive systems. The biggest takeaway was understanding that deployment is the step that transforms a model from a Jupyter notebook experiment into a practical tool used by organizations to make data-driven decisions.
