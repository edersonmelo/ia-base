# Visão Computacional em Produção 🚀📸

Este projeto demonstra como colocar um modelo de **visão computacional** em produção utilizando **FastAPI**, com deploy local via `uvicorn` e uma estrutura de código limpa e didática.

---

## 📂 Estrutura do Projeto

```
visao-computacional-em-producao/
│
├── app/
│   ├── main.py               # API FastAPI com endpoint de predição
│   ├── model/
│   │   ├── model.pkl         # Modelo de exemplo serializado (ou simulado)
│   │   └── predict.py        # Função de predição (recebe imagem e retorna resultado)
│   └── utils/
│       └── image_utils.py    # Funções auxiliares de imagem
│
├── tests/                    # Testes básicos (opcional)
│
├── requirements.txt          # Dependências do projeto
├── README.md                 # Este arquivo
└── .gitignore
```

---

## 🛠️ Pré-requisitos

- Python 3.9+
- pip
- virtualenv (opcional, mas recomendado)

---

## ▶️ Como rodar localmente

### 1. Clone o repositório

```bash
git clone --filter=blob:none --no-checkout git@github.com:edersonmelo/ia-base.git
cd ia-base

# Ativa o modo sparse
git sparse-checkout init --cone

# Escolhe a pasta que quer baixar
git sparse-checkout set visao-computacional-em-producao

# Baixa só aquela pasta
git checkout main

cd visao-computacional-em-producao
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# .\venv\Scripts\activate  # Windows
```

### 3. Instale as dependências

```bash
python -m pip install --upgrade pip
python -m pip install --break-system-packages -r requirements.txt
```

Se aparecer erro relacionado a `python-multipart`, rode:
```bash
python -m pip install --break-system-packages python-multipart
```

### 4. Rode o servidor FastAPI com Uvicorn

```bash
uvicorn app.main:app --reload
```

Acesse em seu navegador:

- Swagger (interface interativa): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📤 Testando a API

No Swagger UI (`/docs`), envie uma imagem `.jpg` ou `.png` no endpoint `/predict`.

A resposta será uma predição simulada do modelo (ou real, se você acoplar um `.pkl` válido).

---

## 📦 Deploy com Docker (em breve)

Você poderá fazer deploy com Docker facilmente. Um `Dockerfile` e instruções serão incluídos na próxima versão.

---

## 📌 Possibilidades(Próximos passos)

- [ ] Adicionar testes automatizados
- [ ] Criar pipeline de CI/CD
- [ ] Publicar como imagem Docker
- [ ] Substituir modelo simulado por um modelo real (ex: CNN em PyTorch)

---

## 📄 Licença

MIT - sinta-se livre para adaptar, contribuir ou usar como base em outros projetos.

---

## 🤝 Contribuindo

Pull requests são bem-vindos! Para grandes mudanças, abra uma issue primeiro para discutir o que deseja modificar.

---

## 💡 Autor

Feito com foco em simplicidade e clareza por **Ederson Melo**.
