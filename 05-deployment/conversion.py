import pickle
from fastapi import FastAPI
import uvicorn

with open("pipeline_v1.bin", "rb") as f_in:
    pipeline = pickle.load(f_in)

print("Pipeline loaded successfully!")


app = FastAPI(title="Conversion Prediction")

@app.post("/predict")
def predict(client: dict):
    y_pred = pipeline.predict_proba([client])[0, 1]
    prediction = pipeline.predict([client])[0]
    
    return {
        "conversion_probability": float(y_pred),
        "will_convert": bool(prediction)
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)
