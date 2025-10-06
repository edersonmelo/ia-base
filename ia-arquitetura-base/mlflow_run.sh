#!/usr/bin/env bash
# Start a local MLflow server (file-store) on port 5000
mlflow server --backend-store-uri file:./mlruns --default-artifact-root ./mlruns/artifacts --host 0.0.0.0 --port 5000
