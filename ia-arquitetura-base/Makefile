.PHONY: train run-api build-docker

train:
	python train.py

run-api:
	uvicorn app.main:app --reload --port 8000

build-docker:
	docker build -t ia-arquitetura-base:latest .
