# Catálogo de exercícios

## Leitura do catálogo

Este documento cobre o núcleo 01–30. A expansão está detalhada no [catálogo dos exercícios 31–100](EXERCISES_31_100.md). Cada critério é ligado a um teste privado específico no `EVALUATION.md` do exercício.

- **M**: mínimo obrigatório.
- **I**: resultado intermediário que demonstra robustez.
- **D**: resultado desejado que demonstra acabamento profissional.

Todos os critérios são binários. Duração é uma estimativa para um estudante que já conhece a linguagem, mas ainda está desenvolvendo experiência profissional.

## Visão geral

| ID | Exercício | Tipo principal | Stack | Nível | Duração |
| ---: | --- | --- | --- | --- | ---: |
| 01 | Desconto de fidelidade | Feature | .NET 10, ASP.NET Core | iniciante | 90 min |
| 02 | Reserva de estoque | Correção de bug | .NET 10, armazenamento local | intermediário | 120 min |
| 03 | Relatório de vendas | Queries/dados | .NET 10, LINQ | intermediário | 120 min |
| 04 | Importação de catálogo | Manipulação de dados | .NET 10, CSV | iniciante | 90 min |
| 05 | Canais de notificação | Design patterns | .NET 10 | intermediário | 120 min |
| 06 | Checkout modular | Arquitetura/refatoração | .NET 10 | intermediário | 150 min |
| 07 | Checkout acessível | Interface | React, TypeScript | iniciante | 120 min |
| 08 | Busca fora de ordem | Correção de bug | React, TypeScript | intermediário | 90 min |
| 09 | Dashboard lento | Performance | Angular, TypeScript | intermediário | 120 min |
| 10 | Formulário por esquema | Feature | Angular, TypeScript | intermediário | 150 min |
| 11 | Edição otimista | Estado/integração | React, TypeScript | intermediário | 120 min |
| 12 | Agendamento e fuso horário | Correção de bug | .NET 10 | iniciante | 90 min |
| 13 | Totais monetários | Correção de bug | .NET 10 | iniciante | 75 min |
| 14 | Motor de preços legado | Refatoração | .NET 10 | intermediário | 150 min |
| 15 | Suíte de testes instável | Qualidade | .NET 10, test doubles | intermediário | 90 min |
| 16 | Contrato de paginação | Correção de regressão | .NET 10 | intermediário | 120 min |
| 17 | Catálogo N+1 | Performance/queries | .NET 10, repositório instrumentado | intermediário | 120 min |
| 18 | Exportação sem memória | Performance/dados | .NET 10 | intermediário | 120 min |
| 19 | API com starvation | Assincronismo | .NET 10 | avançado | 150 min |
| 20 | Cupons concorrentes | Concorrência | .NET 10, estado compartilhado | avançado | 150 min |
| 21 | Consumidor idempotente | Concorrência distribuída | .NET 10, inbox local | avançado | 180 min |
| 22 | Pedidos de outro cliente | Segurança | .NET 10 | intermediário | 90 min |
| 23 | Busca vulnerável | Segurança/queries | .NET 10, SQL | iniciante | 75 min |
| 24 | Upload de documentos | Segurança | .NET 10 | intermediário | 120 min |
| 25 | Recebimento de webhooks | Integração | .NET 10 | intermediário | 120 min |
| 26 | Pagamento resiliente | Integração/resiliência | .NET 10 | avançado | 150 min |
| 27 | Serviço de encurtamento | Projeto do zero | .NET 10 | intermediário | 240 min |
| 28 | Scripts de desenvolvimento | Automação | Bash, PowerShell, .NET 10 | iniciante | 90 min |
| 29 | Ambiente local reproduzível | Infra de desenvolvimento | Docker Compose | intermediário | 120 min |
| 30 | Pipeline de integração | CI e integração | .NET 10, TypeScript | intermediário | 120 min |

## Trilha 1 — Backend e dados

### 01 — Desconto de fidelidade

Uma API de pedidos funcional precisa aceitar uma nova regra de desconto por nível do cliente. O repositório já traz domínio, persistência em memória, endpoints, fixtures e scripts. O estudante implementa apenas a feature sem quebrar cálculo de impostos ou clientes existentes.

- **Tecnologias:** C#, .NET 10, runner de testes local.
- **Armadilha:** aplicar desconto depois do imposto ou confiar no nível enviado pelo cliente em vez do cadastro.
- **Critérios:** [M] níveis elegíveis recebem o percentual correto; [M] clientes não elegíveis mantêm o total; [M] imposto é calculado sobre a base definida no contrato; [I] valores de borda e arredondamento passam; [D] há testes do estudante para ao menos três níveis.

### 02 — Reserva de estoque

Uma reserva cancelada continua reduzindo o saldo disponível em determinada sequência. Há endpoint, banco, migrations e cenário reproduzível. O estudante localiza e corrige a transição de estado.

- **Tecnologias:** C#, .NET 10, repositório local concorrente.
- **Armadilha:** corrigir somente a resposta da API sem restaurar a quantidade persistida, ou permitir cancelamento duplo.
- **Critérios:** [M] cancelamento devolve o estoque exatamente uma vez; [M] reserva ativa continua consumindo saldo; [M] repetição do cancelamento é idempotente; [I] transação é revertida quando a atualização falha; [D] um teste de regressão reproduz a sequência original.

### 03 — Relatório de vendas

Implementar uma consulta que agrega receita e quantidade por produto e período sobre uma base já populada. O contrato define paginação e ordenação, mas não dita SQL ou LINQ.

- **Tecnologias:** C#, .NET 10, LINQ.
- **Armadilha:** somar pedidos cancelados, carregar todas as linhas em memória ou paginar antes de agregar.
- **Critérios:** [M] totais excluem estados inválidos; [M] limites do período obedecem ao contrato; [M] ordenação e paginação são estáveis; [I] a agregação ocorre no banco em uma consulta limitada; [D] plano de execução não contém varredura evitável com o índice fornecido.

### 04 — Importação de catálogo

Adicionar a importação de um CSV fornecido por parceiros. O projeto já contém armazenamento, exemplos e serviço de validação; a entrega deve processar registros válidos e relatar erros por linha.

- **Tecnologias:** C#, .NET 10, CSV.
- **Armadilha:** quebrar com campos entre aspas, aceitar SKU duplicado ou deixar uma importação parcial sem que o contrato permita.
- **Critérios:** [M] CSV válido cria/atualiza os itens esperados; [M] aspas, separadores e UTF-8 são tratados; [M] erros retornam linha e código estável; [I] política de atomicidade é respeitada; [D] arquivo grande é processado sem leitura integral em memória.

### 05 — Canais de notificação

O sistema envia e-mail diretamente e precisa incorporar SMS e push, escolhidos por preferência do usuário. Adaptadores fake já simulam os provedores.

- **Tecnologias:** C#, .NET 10, dependency injection.
- **Armadilha:** criar condicionais espalhadas, instanciar SDKs no domínio ou falhar todos os canais quando um provedor cai.
- **Critérios:** [M] cada preferência aciona somente os canais configurados; [M] um novo canal pode ser registrado sem alterar o orquestrador; [M] payloads obedecem aos contratos; [I] falhas são isoladas segundo a política dada; [D] testes usam doubles por interface e cobrem composição de canais.

### 06 — Checkout modular

Refatorar um serviço de checkout que mistura validação, preço, estoque, pagamento e persistência. O comportamento deve permanecer idêntico e novos limites precisam permitir substituição de integrações.

- **Tecnologias:** C#, .NET 10, arquitetura em camadas.
- **Armadilha:** reescrever regras junto da refatoração, criar abstrações vazias ou deixar transações inconsistentes.
- **Critérios:** [M] toda a suíte de caracterização continua passando; [M] pagamento e estoque podem ser substituídos em testes; [M] regras de domínio não dependem de infraestrutura; [I] falha de pagamento não confirma pedido; [D] dependências entre projetos respeitam o grafo arquitetural verificado.

## Trilha 2 — Frontend

### 07 — Checkout acessível

Construir uma tela responsiva a partir de uma especificação visual local e de uma API já pronta. Deve incluir resumo, endereço, pagamento simulado e estados operacionais.

- **Tecnologias:** React, TypeScript, testes nativos do Node.
- **Armadilha:** reproduzir apenas a imagem feliz, sem teclado, rótulos, erro ou layout móvel.
- **Critérios:** [M] fluxo válido envia o payload correto; [M] erros de campo são associados aos controles; [M] tela é operável por teclado; [I] loading, erro e retry são exibidos; [D] layout passa em viewports móvel e desktop e não tem violações críticas de acessibilidade.

### 08 — Busca fora de ordem

Em uma busca incremental, uma resposta antiga às vezes substitui o resultado mais recente. A API fake controla latência para tornar a corrida determinística.

- **Tecnologias:** React, TypeScript, hooks, Vitest.
- **Armadilha:** apenas aumentar debounce ou comparar texto visual, sem cancelar/ignorar requisições obsoletas.
- **Critérios:** [M] somente a resposta da consulta mais recente é exibida; [M] limpar a busca limpa resultados; [M] desmontagem não causa atualização tardia; [I] requisições redundantes são limitadas; [D] teste do estudante cobre respostas em ordem invertida.

### 09 — Dashboard lento

Um dashboard Angular congela ao filtrar milhares de registros. Fixtures, medidor e comportamento esperado estão prontos; o estudante deve reduzir trabalho de renderização sem remover recursos.

- **Tecnologias:** Angular, TypeScript, RxJS, harness determinístico.
- **Armadilha:** esconder linhas, introduzir mutação incompatível com detecção de mudanças ou otimizar apenas o carregamento inicial.
- **Critérios:** [M] filtro e ordenação permanecem corretos; [M] o número de nós renderizados fica dentro do orçamento; [M] seleção sobrevive à atualização; [I] ciclos de cálculo ficam abaixo do contador definido; [D] navegação por teclado funciona na lista otimizada.

### 10 — Formulário por esquema

Adicionar um formulário de cadastro montado a partir de um esquema recebido da API. Tipos de campo e validações suportadas são delimitados pelo contrato.

- **Tecnologias:** Angular, TypeScript, reactive forms.
- **Armadilha:** codificar os campos do fixture, perder tipagem ou aplicar validação somente no submit.
- **Critérios:** [M] campos suportados são renderizados dinamicamente; [M] obrigatoriedade e limites controlam validade; [M] payload preserva tipos; [I] esquema inválido gera estado de erro seguro; [D] componentes de campo são extensíveis e possuem testes isolados.

### 11 — Edição otimista

Uma lista de tarefas deve permitir edição otimista com confirmação, falha e conflito de versão simulados pela API.

- **Tecnologias:** React, TypeScript, cache otimista local.
- **Armadilha:** sobrescrever edição mais nova no rollback ou ignorar conflito HTTP 409.
- **Critérios:** [M] edição aparece antes da resposta; [M] falha restaura o estado correto; [M] conflito apresenta ação de recarregar/reaplicar; [I] mutações simultâneas no mesmo item não corrompem o cache; [D] feedback é anunciado de forma acessível.

## Trilha 3 — Bugs e qualidade

### 12 — Agendamento e fuso horário

Reservas próximas da mudança de data aparecem no dia errado para usuários fora de UTC. Relógio fake, zonas e casos reproduzíveis já estão no projeto.

- **Tecnologias:** C#, .NET 10, DateTimeOffset.
- **Armadilha:** aplicar o offset duas vezes, usar fuso da máquina ou corrigir apenas a serialização.
- **Critérios:** [M] instante persistido é preservado; [M] exibição usa a zona do usuário; [M] limites de dia são calculados na zona correta; [I] horários ambíguos/inválidos seguem a política; [D] teste de regressão independe da zona da máquina.

### 13 — Totais monetários

O total da fatura diverge por centavos quando há quantidade fracionária, desconto e imposto. O estudante deve identificar a política monetária descrita pelo negócio.

- **Tecnologias:** C#, .NET 10, runner de testes local.
- **Armadilha:** trocar `double` por `decimal` sem corrigir os pontos e a ordem de arredondamento.
- **Critérios:** [M] exemplos oficiais fecham no centavo; [M] nenhuma operação monetária usa ponto flutuante binário; [M] arredondamento ocorre nos limites definidos; [I] valores negativos/estornos mantêm simetria; [D] política está centralizada e coberta por propriedades de invariância.

### 14 — Motor de preços legado

Refatorar um método longo de regras promocionais antes da inclusão futura de campanhas. Testes de caracterização e tabela de regras preservam o comportamento.

- **Tecnologias:** C#, .NET 10, runner de testes local.
- **Armadilha:** alterar precedência de promoções ou transformar cada linha em uma abstração sem benefício.
- **Critérios:** [M] resultados de caracterização permanecem idênticos; [M] regras podem ser testadas isoladamente; [M] ordem de aplicação é explícita; [I] complexidade ciclomática fica abaixo do limite; [D] uma regra fixture pode ser adicionada sem modificar regras existentes.

### 15 — Suíte de testes instável

Uma suíte falha intermitentemente por relógio real, aleatoriedade compartilhada e estado estático. Logs de execuções anteriores orientam a investigação.

- **Tecnologias:** C#, .NET 10, test doubles.
- **Armadilha:** desabilitar paralelismo global, adicionar retry ou aumentar espera.
- **Critérios:** [M] suíte passa repetidamente com sementes variadas; [M] testes não dependem do relógio real; [M] estado não vaza entre casos; [I] paralelismo permanece habilitado; [D] o tempo total não cresce além do orçamento.

### 16 — Contrato de paginação

Uma mudança no backend fez a tela repetir e omitir itens entre páginas quando registros compartilham a mesma data. Backend e frontend já executam juntos.

- **Tecnologias:** C#, .NET 10, paginação por cursor.
- **Armadilha:** remover itens duplicados no cliente em vez de tornar a ordenação estável ou quebrar compatibilidade do cursor.
- **Critérios:** [M] todos os itens aparecem exatamente uma vez; [M] ordenação é determinística em empates; [M] cursor inválido tem resposta contratual; [I] inserções entre páginas obedecem à semântica definida; [D] teste de integração cobre o contrato ponta a ponta.

## Trilha 4 — Performance e concorrência

### 17 — Catálogo N+1

Uma listagem de produtos faz centenas de consultas para montar categorias e disponibilidade. Um contador de comandos torna o problema mensurável.

- **Tecnologias:** C#, .NET 10, repositório instrumentado.
- **Armadilha:** trocar por uma consulta cartesiana enorme ou usar cache global incorreto.
- **Critérios:** [M] resposta mantém todos os campos e valores; [M] quantidade de consultas fica abaixo do limite; [M] paginação ocorre no banco; [I] volume transferido respeita o orçamento; [D] teste de regressão afirma o limite de consultas.

### 18 — Exportação sem memória

Uma exportação CSV esgota memória com um conjunto grande. Gerador de dados e medição de pico já são fornecidos.

- **Tecnologias:** C#, .NET 10, ASP.NET Core streaming.
- **Armadilha:** paginar e ainda acumular todas as strings, ou retornar antes de propagar cancelamento.
- **Critérios:** [M] arquivo possui todas as linhas na ordem correta; [M] pico de memória fica abaixo do orçamento; [M] caracteres e escaping são válidos; [I] cancelamento interrompe leitura e resposta; [D] o cliente recebe o primeiro bloco antes da consulta terminar por completo.

### 19 — API com starvation

Sob carga, um endpoint que combina chamadas HTTP e processamento bloqueia o pool de threads. Servidor fake e cenário de carga local acompanham o projeto.

- **Tecnologias:** C#, .NET 10, async/await, HttpClient.
- **Armadilha:** envolver I/O em `Task.Run`, aumentar threads ou remover limites de concorrência.
- **Critérios:** [M] não há bloqueio síncrono no caminho de I/O; [M] throughput mínimo é atingido sob carga controlada; [M] cancelamento da requisição chega às dependências; [I] concorrência do trecho CPU-bound é limitada; [D] métricas confirmam ausência de crescimento sustentado da fila.

### 20 — Cupons concorrentes

Um cupom de uso único pode ser resgatado duas vezes por requisições simultâneas. O harness dispara concorrência real contra PostgreSQL.

- **Tecnologias:** C#, .NET 10, estado compartilhado concorrente.
- **Armadilha:** `lock` local que falha com duas instâncias ou checagem seguida de escrita sem proteção no banco.
- **Critérios:** [M] exatamente um resgate é confirmado; [M] saldo e auditoria permanecem consistentes; [M] solução funciona com duas instâncias da API; [I] conflitos retornam resultado de negócio estável; [D] estratégia lida com retry sem duplicar efeitos.

### 21 — Consumidor idempotente

Mensagens podem ser entregues novamente e o consumidor atual duplica faturas. Broker e produtor local simulam duplicação, falha e redelivery.

- **Tecnologias:** C#, .NET 10, inbox e persistência local simulada.
- **Armadilha:** deduplicar apenas em memória, confirmar mensagem antes do commit ou confundir ordem com idempotência.
- **Critérios:** [M] uma chave gera um único efeito persistido; [M] redelivery após falha não perde a mensagem; [M] duas instâncias mantêm a garantia; [I] registro de idempotência e efeito são atômicos; [D] mensagens inválidas seguem para tratamento sem bloquear a fila.

## Trilha 5 — Segurança e integração

### 22 — Pedidos de outro cliente

Usuários autenticados conseguem consultar ou alterar um pedido pertencente a outra conta ao trocar o ID. Autenticação fake permite testar identidades sem serviço externo.

- **Tecnologias:** C#, .NET 10, autorização por recurso.
- **Armadilha:** esconder o botão no frontend, validar apenas um endpoint ou confiar em `customerId` do payload.
- **Critérios:** [M] leitura cruzada é negada; [M] alteração e cancelamento cruzados são negados; [M] dono mantém acesso esperado; [I] respostas não revelam existência além da política; [D] autorização é centralizada e todos os endpoints de pedido passam por ela.

### 23 — Busca vulnerável

Um endpoint monta SQL a partir de filtro e ordenação enviados pelo cliente. O desafio é eliminar injeção preservando filtros permitidos.

- **Tecnologias:** C#, .NET 10, construção segura de SQL.
- **Armadilha:** parametrizar valores, mas continuar interpolando coluna/direção sem allowlist.
- **Critérios:** [M] valores maliciosos não alteram a consulta; [M] ordenação aceita somente campos/direções permitidos; [M] buscas legítimas continuam funcionando; [I] entrada inválida retorna erro estável sem detalhes do banco; [D] analisador não encontra construção SQL insegura no caminho avaliado.

### 24 — Upload de documentos

Fortalecer um endpoint de upload usado para comprovantes. O armazenamento local fake e arquivos de teste cobrem conteúdo, tamanho e nomes.

- **Tecnologias:** C#, .NET 10, streams e filesystem.
- **Armadilha:** confiar apenas na extensão/MIME declarado, usar nome do usuário no caminho ou carregar arquivo inteiro antes de limitar tamanho.
- **Critérios:** [M] path traversal não escapa do diretório; [M] tamanho é limitado durante leitura; [M] tipos não permitidos são rejeitados por conteúdo/política; [I] nomes armazenados não colidem nem expõem entrada; [D] falhas removem arquivos parciais e geram auditoria sem dados sensíveis.

### 25 — Recebimento de webhooks

Integrar eventos de um parceiro a partir de uma especificação local. É necessário verificar assinatura, lidar com repetição e responder dentro do prazo.

- **Tecnologias:** C#, .NET 10, HMAC, armazenamento idempotente local.
- **Armadilha:** verificar assinatura depois de desserializar/normalizar o corpo ou executar todo o processamento antes da resposta.
- **Critérios:** [M] assinatura válida sobre bytes brutos é aceita; [M] assinatura inválida é rejeitada; [M] evento repetido não duplica efeitos; [I] resposta rápida desacopla processamento; [D] segredo pode ser rotacionado conforme a política fixture.

### 26 — Pagamento resiliente

Um cliente de pagamentos deve suportar timeout, falhas transitórias e resultado incerto. O provedor simulado registra cada tentativa.

- **Tecnologias:** C#, .NET 10, async/await, provedor local controlável.
- **Armadilha:** repetir POST sem chave idempotente, retry em erro permanente ou multiplicar timeouts em cascata.
- **Critérios:** [M] timeout é aplicado e propagado; [M] somente falhas transitórias elegíveis são repetidas; [M] tentativas usam a mesma chave idempotente; [I] backoff respeita política e cancelamento; [D] circuit breaker abre e se recupera no cenário controlado.

## Trilha 6 — DevEx, scripts e infraestrutura

### 27 — Serviço de encurtamento

Criar do zero um pequeno serviço a partir de requisitos de produto e contrato HTTP. O repositório contém somente enunciado, contrato OpenAPI, ambiente do banco e convenções de entrega.

- **Tecnologias:** C#, .NET 10, contratos de persistência.
- **Armadilha:** overengineering, geração de código não determinística, códigos curtos com colisões ou redirecionamento aberto fora do contrato.
- **Critérios:** [M] criar e resolver links obedece ao contrato; [M] códigos são únicos sob concorrência; [M] dados sobrevivem a reinício; [I] validação e respostas de erro são consistentes; [D] projeto possui testes, health check, migration e documentação executável.

### 28 — Scripts de desenvolvimento

Uma equipe executa uma sequência manual e sujeita a erros para restaurar ferramentas, aplicar migrations, gerar fixtures e rodar verificações. O estudante deve criar scripts seguros e claros.

- **Tecnologias:** Bash, PowerShell, .NET 10, npm.
- **Armadilha:** depender do diretório atual, ignorar exit codes, apagar caminho amplo ou funcionar apenas quando tudo já está instalado.
- **Critérios:** [M] setup funciona a partir de qualquer diretório; [M] falha encerra com código e mensagem úteis; [M] caminhos de limpeza são validados e restritos; [I] segunda execução é idempotente; [D] Bash e PowerShell apresentam comportamento equivalente no harness.

### 29 — Ambiente local reproduzível

Preparar Docker Compose para uma API que depende de PostgreSQL, Redis e um worker. Dockerfiles, aplicação e contratos de health check já existem; a orquestração está incompleta.

- **Tecnologias:** Docker, Docker Compose, .NET 10, PostgreSQL, Redis.
- **Armadilha:** usar `depends_on` sem readiness, persistir build output local na imagem ou expor credenciais reais.
- **Critérios:** [M] um comando inicia todos os serviços saudáveis; [M] API espera dependências prontas; [M] dados persistem/reinicializam conforme comandos; [I] imagens executam como usuário não root e têm contexto enxuto; [D] rebuild sem mudanças aproveita cache e serviços aceitam portas configuráveis.

### 30 — Pipeline de integração

Consertar e completar o pipeline de um monorepo com API .NET e frontend TypeScript. O pipeline deve validar o mesmo que o ambiente local e publicar artefatos somente quando apropriado.

- **Tecnologias:** .NET 10, TypeScript, YAML de CI, containers locais de validação.
- **Armadilha:** mascarar exit codes, usar cache sem chave de lockfile, deixar testes de um projeto fora ou expor segredo em logs.
- **Critérios:** [M] falha de build/teste faz o job falhar; [M] backend e frontend são verificados; [M] artefato só é produzido após validações; [I] cache invalida quando dependências mudam; [D] pipeline fixture não revela segredos e evita trabalho duplicado em etapas independentes.

## Cobertura dos casos solicitados

| Caso | Exercícios principais |
| --- | --- |
| Criação de features | 01, 10 |
| Correção de bugs | 02, 08, 12, 13, 16 |
| Projeto do zero | 27 |
| Performance | 03, 09, 17, 18, 19 |
| Segurança | 22, 23, 24, 25 |
| Refatoração | 06, 14 |
| Integração | 11, 16, 25, 26, 30 |
| Scripts | 28 |
| Infraestrutura local | 21, 29 |
| Interfaces frontend | 07, 09, 10, 11 |
| Manipulação de dados | 03, 04, 13, 18 |
| Queries | 03, 17, 23 |
| Design patterns | 05, 14 |
| Arquitetura | 06, 27 |
| Concorrência em processo | 08, 19, 20 |
| Concorrência entre aplicações | 20, 21, 25, 26 |
