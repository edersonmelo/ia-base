# ia-arquitetura-base

[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI--lightgrey)](https://fastapi.tiangolo.com/)
[![MLflow](https://img.shields.io/badge/MLflow--lightgrey)](https://mlflow.org/)
[![Build Status](https://img.shields.io/badge/build-ia--arquitetura--base%20(main)-brightgreen)](https://github.com/your-org/ia-arquitetura-base/actions)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**Author:** Ederson Melo

Repository base para **IA/ML em produção**.
Inclui:
- treinamento com scikit-learn e logging em MLflow
- API simples com FastAPI para inferência
- Dockerfile para conteinerizar a API
- workflow GitHub Actions (CI) com lint, testes e build Docker

**Exemplo:** classificação (breast cancer) com scikit-learn.

## Como usar (rápido)
1. Instale dependências:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Rodar treinamento:
   ```bash
   python train.py --mlflow-uri http://localhost:5000
   ```
   Isso treina um modelo, registra no MLflow e salva `models/model.pkl`.

3. Rodar API local:
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```
   Endpoint: `POST /predict` com JSON `{"input": [ ... features ... ]}`

4. Docker:
   ```bash
   docker build -t ia-arquitetura-base:latest .
   docker run -p 8000:80 ia-arquitetura-base:latest
   ```

## Estrutura
- `train.py` — script de treino e registro MLflow
- `app/` — FastAPI para inferência
- `models/` — local para salvar o modelo treinado
- `requirements.txt`, `Dockerfile`, `README.md`
- `.github/workflows/ci.yml` — workflow CI

## GitHub Actions / CI
O workflow presente neste repositório usa **Python 3.11**, roda lint (`flake8`), testes (`pytest`) e builda a imagem Docker.
Para habilitar push automático para Docker Hub configure os *Secrets*:
- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

## Versão Premium disponível!
Template completo com MLflow, FastAPI e Docker.
👉 Me chama para acesso ou mentoria personalizada.

## Autor
Ederson Melo
