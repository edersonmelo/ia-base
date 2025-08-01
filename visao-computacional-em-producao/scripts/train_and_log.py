
import mlflow
import time

def train_dummy_model():
    with mlflow.start_run():
        accuracy = 0.85  # Simulado
        mlflow.log_param("model_type", "yolov8")
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_artifact("model/predict.py")
        time.sleep(1)
