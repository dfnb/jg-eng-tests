# Padrões técnicos

## Versões de referência

- Backend: C# e .NET 10.
- Frontend: TypeScript preferencialmente; JavaScript apenas quando a competência avaliada justificar.
- Frameworks de frontend: React ou Angular, escolhidos por exercício e fixados por lockfile.
- Banco relacional padrão: PostgreSQL.
- Cache e coordenação, quando necessários: Redis.
- Infraestrutura local: Docker Compose.

Versões exatas serão fixadas por exercício em arquivos de SDK, manifesto e lockfile. Atualizações serão feitas de forma consciente; um exercício publicado não deve mudar de comportamento por uma atualização flutuante.

## Backend

Cada projeto .NET deve incluir `global.json`, nullable reference types, analyzers, formatação reproduzível e testes separados do código de produção. Dependências externas devem ser substituíveis por doubles ou serviços locais controlados.

APIs devem oferecer health check quando dependem de banco, cache ou broker. Migrations e dados de exemplo fazem parte do setup e precisam ser idempotentes.

## Frontend

Projetos usam TypeScript em modo estrito, lint, formatter, lockfile e testes de unidade/componente. Exercícios de interface incluem critérios de acessibilidade e estados de carregamento, vazio, sucesso e erro quando aplicáveis.

Testes end-to-end devem selecionar elementos por papel, rótulo ou identificador estável, não por classes cosméticas.

## Comandos uniformes

Todo `exercise/` expõe os comandos conceituais abaixo, mesmo que sua implementação varie por plataforma:

- `setup`: valida ferramentas, instala dependências e prepara dados;
- `start`: inicia a aplicação e dependências;
- `test`: executa a suíte pública;
- `lint`: executa verificações estáticas;
- `reset-data`: restaura fixtures, quando houver persistência;
- `stop`: encerra dependências locais, quando aplicável.

No início da coleção, esses comandos serão disponibilizados por scripts POSIX e documentados com o comando nativo equivalente (`dotnet`, `npm`, `docker compose`).

## Reprodutibilidade

- imagens Docker recebem tags fixas;
- pacotes são travados por lockfile;
- relógio, UUIDs e aleatoriedade são injetáveis quando afetam testes;
- portas podem ser configuradas para evitar colisões;
- dados de teste não dependem de internet;
- nenhum exercício exige conta externa;
- setup novo e reset devem produzir o mesmo estado observável.

## Tempo e recursos

Meta para ambiente já provisionado:

- suíte pública: até 60 segundos;
- avaliador privado: até 3 minutos;
- exercício inteiro: até 2 GB de RAM em execução normal;
- download inicial: minimizado por imagens e pacotes compartilhados entre exercícios.

Exceções precisam ser justificadas no `EVALUATION.md`.

## Compatibilidade

O ambiente principal será Linux x86-64 com Docker. Scripts não devem depender de configuração pessoal. Caminhos usam nomes portáveis e não assumem ferramentas globais além das declaradas no README.
