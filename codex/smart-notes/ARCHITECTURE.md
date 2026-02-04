# Arquitetura

Este projeto usa uma arquitetura em camadas simples para manter o código organizado e fácil de evoluir.

## Camadas
1. **Interface (CLI)**  
   Responsável por ler argumentos e imprimir respostas. Não contém regras de negócio.

2. **Serviço (Application/Use Cases)**  
   Orquestra casos de uso como criar, listar, concluir e remover notas.

3. **Domínio**  
   Define a entidade `Note` e seus dados essenciais.

4. **Persistência (Infra)**  
   Implementa o repositório concreto (JSON) e lida com I/O.

## Fluxo
CLI → Service → Repository → JSON

## Benefícios
- Separação clara de responsabilidades.
- Facilita testes unitários (serviço usa mocks de persistência).
- Permite trocar a persistência sem alterar regras de negócio.
