from fastapi import FastAPI
from joblib import load
import numpy as np

app = FastAPI()


@app.get("/")
async def root():
 return {"greeting":"Hello Medium reader!"}

@app.get("/predict")
async def predict(total_rooms: int):
    model = load("model.joblib")
    prediction = model.predict(np.array(total_rooms).reshape(1,-1))[0]
    return {"prediction": prediction}