
from ultralytics import YOLO
import cv2

# Carrega o modelo YOLOv8 pré-treinado
model = YOLO("yolov8n.pt")

def predict(image_path):
    results = model(image_path)
    return results[0].boxes.xyxy
