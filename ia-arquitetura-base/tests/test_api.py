import os
import joblib
from sklearn.dummy import DummyClassifier
from fastapi.testclient import TestClient

def setup_module(module):
    # Ensure test model path and create a simple dummy model
    test_model_path = 'tests/test_model.pkl'
    os.environ['MODEL_PATH'] = test_model_path
    # create dummy model that predicts class 1
    clf = DummyClassifier(strategy='most_frequent')
    X = [[0], [1], [2]]
    y = [1,1,1]
    clf.fit(X,y)
    joblib.dump({'model': clf, 'columns': ['x']}, test_model_path)

def teardown_module(module):
    try:
        os.remove('tests/test_model.pkl')
    except:
        pass

def test_predict_endpoint():
    # import app after MODEL_PATH env var is set
    import importlib
    app_module = importlib.import_module('app.main')
    client = TestClient(app_module.app)
    resp = client.post('/predict', json={'input': [0]})
    assert resp.status_code == 200
    data = resp.json()
    assert 'prediction' in data
    assert isinstance(data['prediction'], list)
