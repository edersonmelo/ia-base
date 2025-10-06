from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os

MODEL_PATH = os.getenv('MODEL_PATH', 'models/model.pkl')

app = FastAPI(title='IA Arquitetura Base - Inference API')

class PredictRequest(BaseModel):
    input: list

@app.on_event('startup')
def load_model():
    global MODEL, COLUMNS
    data = joblib.load(MODEL_PATH)
    MODEL = data['model']
    COLUMNS = data.get('columns', None)

@app.post('/predict')
def predict(req: PredictRequest):
    x = np.array(req.input).reshape(1, -1)
    pred = MODEL.predict(x).tolist()
    return {'prediction': pred}
