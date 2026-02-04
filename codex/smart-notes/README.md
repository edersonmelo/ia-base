# Smart Notes (CLI)

Projeto simples de linha de comando para criar e gerenciar notas com persistência em JSON.

## O que faz
- Criar notas (`add <title> <content>`)
- Listar notas (`list`)
- Concluir notas (`complete <id>`)
- Remover notas (`delete <id>`)

## Como usar
```bash
python app.py add "Titulo" "Conteudo"
python app.py list
python app.py complete 1
python app.py delete 1
```

## Estrutura principal
- `app.py`: Interface CLI e ponto de entrada.
- `domain/`: Entidades do domínio.
- `services/`: Regras de negócio e orquestração.
- `persistence/`: Persistência em JSON.
- `tests/`: Testes unitários.

## Persistência
As notas são salvas em `storage.json` no diretório atual do projeto.
