# Uso rápido

- Treinar localmente:
  ```
  python train.py
  ```

- Rodar MLflow local (opcional):
  ```
  ./mlflow_run.sh
  ```

- Rodar API local:
  ```
  uvicorn app.main:app --reload --port 8000
  ```

- Fazer uma predição (exemplo usando curl):
  ```
  curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d @predict_example.json
  ```
