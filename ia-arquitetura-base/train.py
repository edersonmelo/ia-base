import argparse
import os
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import mlflow
import joblib
import pandas as pd

def train(mlflow_uri=None):
    if mlflow_uri:
        mlflow.set_tracking_uri(mlflow_uri)
    mlflow.set_experiment('ia-arquitetura-base-experiment')

    data = load_breast_cancer(as_frame=True)
    X = data.data
    y = data.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    with mlflow.start_run():
        model = LogisticRegression(max_iter=1000)
        model.fit(X_train, y_train)

        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)

        mlflow.log_metric('accuracy', float(acc))
        mlflow.sklearn.log_model(model, 'model')

        os.makedirs('models', exist_ok=True)
        joblib.dump({'model': model, 'columns': list(X.columns)}, 'models/model.pkl')

        print('Accuracy:', acc)
        print(classification_report(y_test, preds))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mlflow-uri', type=str, default=None, help='URI do MLflow tracking server (opcional)')
    args = parser.parse_args()
    train(args.mlflow_uri)
