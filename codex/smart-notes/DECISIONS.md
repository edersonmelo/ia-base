# Decisões e Trade-offs

## 1. Persistência em JSON
- **Decisão**: Usar `storage.json` como armazenamento local.
- **Trade-off**: Simples e fácil de entender, mas não é ideal para concorrência ou grandes volumes.

## 2. Arquitetura em camadas
- **Decisão**: Separar CLI, serviço, domínio e persistência.
- **Trade-off**: Mais arquivos e estrutura, porém facilita testes e manutenção.

## 3. IDs gerados por tamanho da lista
- **Decisão**: `id = len(notes) + 1` para manter compatibilidade com o comportamento anterior.
- **Trade-off**: Possibilidade de reutilização de IDs após remoção, mas evita mudança de comportamento externo.

## 4. Interface de repositório
- **Decisão**: Criar `NotesRepository` para isolar o serviço da infraestrutura.
- **Trade-off**: Pequena camada extra, mas torna o serviço testável e desacoplado.
