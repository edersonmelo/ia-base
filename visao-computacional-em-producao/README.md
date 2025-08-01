# Visão Computacional em Produção 🚀📸

Este projeto demonstra como colocar um modelo de **visão computacional** em produção utilizando **FastAPI**, com deploy local via `uvicorn` e uma estrutura de código limpa e didática.

---

## 📂 Estrutura do Projeto

visao-computacional-em-producao/
│
├── app/
│ ├── main.py # API FastAPI com endpoint de predição
│ ├── model/
│ │ ├── model.pkl # Modelo de exemplo serializado (ou simulado)
│ │ └── predict.py # Função de predição (recebe imagem e retorna resultado)
│ └── utils/
│ └── image_utils.py # Funções auxiliares de imagem
│
├── tests/ # Testes básicos (opcional)
│
├── requirements.txt # Dependências do projeto
├── README.md # Este arquivo
└── .gitignore


---

## 🛠️ Pré-requisitos

- Python 3.9+
- pip
- virtualenv (opcional, mas recomendado)

---

## ▶️ Como rodar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/visao-computacional-em-producao.git
cd visao-computacional-em-producao

### 2. Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
# .\venv\Scripts\activate  # Windows


### 3. Instale as dependências
python -m pip install --upgrade pip
python -m pip install --break-system-packages -r requirements.txt

### 4. Rode o servidor FastAPI com Uvicorn
uvicorn app.main:app --reload



### Acesse em seu navegador:
Swagger (interface interativa): http://127.0.0.1:8000/docs
Redoc: http://127.0.0.1:8000/redoc


### Testando a API
No Swagger UI (/docs), envie uma imagem .jpg ou .png no endpoint /predict.
A resposta será uma predição simulada do modelo (ou real, se você acoplar um .pkl válido).
