
from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io

app = FastAPI()

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read()))
    # Aqui entraria o modelo carregado e inferência real
    return {"message": "Imagem recebida", "size": image.size}
