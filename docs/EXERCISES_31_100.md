# Catálogo dos exercícios 31–100

Este documento detalha a expansão planejada. Os cinco critérios de cada exercício são observáveis pelo grader; C01–C03 formam o mínimo, C04 é intermediário e C05 é desejado.

| ID | Exercício | Área | Tecnologia | Foco |
| --- | --- | --- | --- | --- |
| 31 | Compatibilidade de versões da API | Backend | .NET 10 / C# | contratos HTTP |
| 32 | Semântica de PATCH | Backend | .NET 10 / C# | model binding |
| 33 | Erros com Problem Details | Backend | .NET 10 / C# | contratos de erro |
| 34 | Atualização com ETag | Backend | .NET 10 / C# | concorrência otimista |
| 35 | POST idempotente | Backend | .NET 10 / C# | idempotência HTTP |
| 36 | Resultado parcial em lote | Backend | .NET 10 / C# | APIs em lote |
| 37 | Download com Range | Backend | .NET 10 / C# | streaming HTTP |
| 38 | Negociação de conteúdo | Backend | .NET 10 / C# | HTTP |
| 39 | Mensagens localizadas | Backend | .NET 10 / C# | localização |
| 40 | Rate limit por janela | Backend | .NET 10 / C# | rate limiting |
| 41 | Papel e escopo | Backend | .NET 10 / C# | autorização |
| 42 | Expiração de token | Backend | .NET 10 / C# | autenticação |
| 43 | Redação de logs | Backend | .NET 10 / C# | observabilidade |
| 44 | Proteção contra SSRF | Backend | .NET 10 / C# | segurança de rede |
| 45 | Return URL seguro | Backend | .NET 10 / C# | segurança web |
| 46 | Proteção contra mass assignment | Backend | .NET 10 / C# | model binding |
| 47 | Atualização de hash de senha | Backend | .NET 10 / C# | segurança de credenciais |
| 48 | Identidade Unicode | Backend | .NET 10 / C# | normalização |
| 49 | Paginação keyset | Backend | .NET 10 / C# | queries |
| 50 | Tokenização de busca | Backend | .NET 10 / C# | queries |
| 51 | Plano de outbox | Backend | .NET 10 / C# | integração de dados |
| 52 | Migration expand-contract | Backend | .NET 10 / C# | evolução de schema |
| 53 | Upcasting de eventos | Backend | .NET 10 / C# | compatibilidade de schema |
| 54 | Jitter de cache | Backend | .NET 10 / C# | cache |
| 55 | Invalidação por tags | Backend | .NET 10 / C# | cache |
| 56 | Fencing token de lease | Backend | .NET 10 / C# | concorrência distribuída |
| 57 | Retry-After | Backend | .NET 10 / C# | resiliência HTTP |
| 58 | Circuit breaker half-open | Backend | .NET 10 / C# | resiliência |
| 59 | Isolamento por bulkhead | Backend | .NET 10 / C# | resiliência |
| 60 | Compensação de saga | Backend | .NET 10 / C# | arquitetura distribuída |
| 61 | Ordenação de eventos | Backend | .NET 10 / C# | mensageria |
| 62 | Read-your-writes | Backend | .NET 10 / C# | consistência eventual |
| 63 | Cancelamento cooperativo | Backend | .NET 10 / C# | performance CPU |
| 64 | Canal com capacidade | Backend | .NET 10 / C# | producer-consumer |
| 65 | Liberação de recursos | Backend | .NET 10 / C# | gestão de recursos |
| 66 | Navegação com formulário sujo | Frontend | React / TypeScript | roteamento |
| 67 | Estado sincronizado com URL | Frontend | Angular / TypeScript | roteamento |
| 68 | Fallback de erro | Frontend | React / TypeScript | resiliência de UI |
| 69 | Estados de carregamento | Frontend | Angular / TypeScript | estado de UI |
| 70 | Pluralização de mensagens | Frontend | React / TypeScript | i18n |
| 71 | Data no fuso do usuário | Frontend | Angular / TypeScript | datas |
| 72 | Foco em modal | Frontend | React / TypeScript | acessibilidade |
| 73 | Combobox acessível | Frontend | Angular / TypeScript | acessibilidade |
| 74 | Reordenação por teclado | Frontend | React / TypeScript | acessibilidade |
| 75 | Tabela responsiva | Frontend | Angular / TypeScript | responsividade |
| 76 | Virtualização com alturas | Frontend | React / TypeScript | performance |
| 77 | Dependências de memoização | Frontend | Angular / TypeScript | performance |
| 78 | Closure obsoleta | Frontend | React / TypeScript | estado assíncrono |
| 79 | Atualização imutável | Frontend | Angular / TypeScript | estado |
| 80 | Reducer de fluxo | Frontend | React / TypeScript | arquitetura frontend |
| 81 | Validação assíncrona de campo | Frontend | Angular / TypeScript | forms |
| 82 | Progresso de upload | Frontend | React / TypeScript | integração |
| 83 | Scroll infinito sem duplicatas | Frontend | Angular / TypeScript | paginação |
| 84 | Reconexão WebSocket | Frontend | React / TypeScript | tempo real |
| 85 | Fila offline | Frontend | Angular / TypeScript | offline-first |
| 86 | Versão de cache offline | Frontend | React / TypeScript | service worker |
| 87 | Texto rico seguro | Frontend | Angular / TypeScript | segurança XSS |
| 88 | Sanitização de links | Frontend | React / TypeScript | segurança |
| 89 | Envio de CSRF | Frontend | Angular / TypeScript | segurança |
| 90 | Nonce de CSP | Frontend | React / TypeScript | segurança |
| 91 | Imports tree-shakable | Frontend | Angular / TypeScript | bundle size |
| 92 | Rotas lazy | Frontend | React / TypeScript | bundle size |
| 93 | Imagem responsiva | Frontend | Angular / TypeScript | performance web |
| 94 | Ciclo de listeners | Frontend | React / TypeScript | memory leaks |
| 95 | Limpeza de observers | Frontend | Angular / TypeScript | memory leaks |
| 96 | Particionamento para Web Worker | Frontend | React / TypeScript | performance CPU |
| 97 | Reordenação otimista | Frontend | Angular / TypeScript | estado otimista |
| 98 | Merge em tempo real | Frontend | React / TypeScript | colaboração |
| 99 | Tokens de tema | Frontend | Angular / TypeScript | design system |
| 100 | Teste de UI determinístico | Frontend | React / TypeScript | qualidade de testes |

## 31 — Compatibilidade de versões da API

- **Área:** Backend (.NET 10)
- **Foco:** contratos HTTP
- **Problema:** Manter clientes v1 enquanto a representação v2 evolui.
- **Critérios discretos:**

  - C01 (mínimo): v1 não recebe campo novo.
  - C02 (mínimo): v2 recebe nome e email.
  - C03 (mínimo): nome vazio é preservado.
  - C04 (intermediário): v2 preserva caracteres.
  - C05 (desejado): versão futura segue contrato atual.

## 32 — Semântica de PATCH

- **Área:** Backend (.NET 10)
- **Foco:** model binding
- **Problema:** Distinguir campo ausente, nulo e valor explícito em atualização parcial.
- **Critérios discretos:**

  - C01 (mínimo): ausente preserva valor.
  - C02 (mínimo): null limpa valor.
  - C03 (mínimo): valor substitui.
  - C04 (intermediário): valor é normalizado.
  - C05 (desejado): vazio explícito permanece vazio.

## 33 — Erros com Problem Details

- **Área:** Backend (.NET 10)
- **Foco:** contratos de erro
- **Problema:** Produzir códigos de erro estáveis sem vazar exceções internas.
- **Critérios discretos:**

  - C01 (mínimo): 404 possui tipo estável.
  - C02 (mínimo): 409 representa conflito.
  - C03 (mínimo): 422 usa validation.
  - C04 (intermediário): trace é preservado.
  - C05 (desejado): mensagem interna não é incluída.

## 34 — Atualização com ETag

- **Área:** Backend (.NET 10)
- **Foco:** concorrência otimista
- **Problema:** Aplicar If-Match e rejeitar escrita sobre versão obsoleta.
- **Critérios discretos:**

  - C01 (mínimo): versão atual atualiza.
  - C02 (mínimo): versão antiga falha.
  - C03 (mínimo): versão futura falha.
  - C04 (intermediário): etag vazio falha.
  - C05 (desejado): etag textual compara exatamente.

## 35 — POST idempotente

- **Área:** Backend (.NET 10)
- **Foco:** idempotência HTTP
- **Problema:** Decidir criação, replay ou conflito a partir de chave e hash do payload.
- **Critérios discretos:**

  - C01 (mínimo): chave nova cria.
  - C02 (mínimo): mesmo hash reproduz.
  - C03 (mínimo): hash diferente conflita.
  - C04 (intermediário): payload vazio ainda tem hash.
  - C05 (desejado): comparação é exata.

## 36 — Resultado parcial em lote

- **Área:** Backend (.NET 10)
- **Foco:** APIs em lote
- **Problema:** Representar sucesso e falha por item sem perder a ordem original.
- **Critérios discretos:**

  - C01 (mínimo): mistura preserva ordem.
  - C02 (mínimo): todos válidos.
  - C03 (mínimo): todos inválidos.
  - C04 (intermediário): um item funciona.
  - C05 (desejado): índice é estável.

## 37 — Download com Range

- **Área:** Backend (.NET 10)
- **Foco:** streaming HTTP
- **Problema:** Validar intervalo inclusivo e produzir Content-Range correto.
- **Critérios discretos:**

  - C01 (mínimo): range válido.
  - C02 (mínimo): último byte.
  - C03 (mínimo): fim fora falha.
  - C04 (intermediário): ordem inválida falha.
  - C05 (desejado): início negativo falha.

## 38 — Negociação de conteúdo

- **Área:** Backend (.NET 10)
- **Foco:** HTTP
- **Problema:** Escolher JSON ou CSV respeitando q-values e retornar 406 quando nenhum é aceito.
- **Critérios discretos:**

  - C01 (mínimo): JSON é padrão aceito.
  - C02 (mínimo): CSV explícito.
  - C03 (mínimo): q maior vence.
  - C04 (intermediário): tipos negados retornam 406.
  - C05 (desejado): tipo desconhecido retorna 406.

## 39 — Mensagens localizadas

- **Área:** Backend (.NET 10)
- **Foco:** localização
- **Problema:** Resolver mensagem por cultura com fallback previsível e pluralização.
- **Critérios discretos:**

  - C01 (mínimo): português singular.
  - C02 (mínimo): português plural.
  - C03 (mínimo): inglês singular.
  - C04 (intermediário): inglês plural.
  - C05 (desejado): cultura desconhecida cai em inglês.

## 40 — Rate limit por janela

- **Área:** Backend (.NET 10)
- **Foco:** rate limiting
- **Problema:** Contar somente requisições dentro da janela móvel e produzir allow/deny.
- **Critérios discretos:**

  - C01 (mínimo): abaixo do limite.
  - C02 (mínimo): no limite nega.
  - C03 (mínimo): evento antigo expira.
  - C04 (intermediário): limite zero nega.
  - C05 (desejado): borda de 60s expira.

## 41 — Papel e escopo

- **Área:** Backend (.NET 10)
- **Foco:** autorização
- **Problema:** Exigir simultaneamente role e scope, sem confundir OR com AND.
- **Critérios discretos:**

  - C01 (mínimo): role e scope permitem.
  - C02 (mínimo): só role nega.
  - C03 (mínimo): só scope nega.
  - C04 (intermediário): listas contêm requisitos.
  - C05 (desejado): nomes parciais não permitem.

## 42 — Expiração de token

- **Área:** Backend (.NET 10)
- **Foco:** autenticação
- **Problema:** Validar expiração com clock skew limitado e relógio injetado.
- **Critérios discretos:**

  - C01 (mínimo): antes de expirar.
  - C02 (mínimo): na expiração.
  - C03 (mínimo): dentro do skew.
  - C04 (intermediário): fora do skew.
  - C05 (desejado): sem skew expira imediatamente.

## 43 — Redação de logs

- **Área:** Backend (.NET 10)
- **Foco:** observabilidade
- **Problema:** Remover valores sensíveis mantendo estrutura e correlação.
- **Critérios discretos:**

  - C01 (mínimo): senha é redigida.
  - C02 (mínimo): token é redigido.
  - C03 (mínimo): authorization ignora caixa.
  - C04 (intermediário): campo comum permanece.
  - C05 (desejado): múltiplos segredos somem.

## 44 — Proteção contra SSRF

- **Área:** Backend (.NET 10)
- **Foco:** segurança de rede
- **Problema:** Permitir somente HTTPS público e bloquear loopback, link-local e credenciais na URL.
- **Critérios discretos:**

  - C01 (mínimo): HTTPS público permite.
  - C02 (mínimo): HTTP nega.
  - C03 (mínimo): localhost nega.
  - C04 (intermediário): link local nega.
  - C05 (desejado): credencial embutida nega.

## 45 — Return URL seguro

- **Área:** Backend (.NET 10)
- **Foco:** segurança web
- **Problema:** Aceitar somente caminho local absoluto sem barra dupla ou esquema.
- **Critérios discretos:**

  - C01 (mínimo): caminho local permanece.
  - C02 (mínimo): URL externa cai na raiz.
  - C03 (mínimo): protocol-relative cai na raiz.
  - C04 (intermediário): texto relativo cai na raiz.
  - C05 (desejado): query local permanece.

## 46 — Proteção contra mass assignment

- **Área:** Backend (.NET 10)
- **Foco:** model binding
- **Problema:** Aplicar allowlist de campos editáveis e ignorar role/owner enviados pelo cliente.
- **Critérios discretos:**

  - C01 (mínimo): nome é aceito.
  - C02 (mínimo): role é ignorado.
  - C03 (mínimo): owner é ignorado.
  - C04 (intermediário): dois campos permitidos ordenam.
  - C05 (desejado): somente proibidos gera vazio.

## 47 — Atualização de hash de senha

- **Área:** Backend (.NET 10)
- **Foco:** segurança de credenciais
- **Problema:** Decidir quando rehash é necessário sem comparar senha em texto.
- **Critérios discretos:**

  - C01 (mínimo): custo antigo rehash.
  - C02 (mínimo): custo atual mantém.
  - C03 (mínimo): custo maior mantém.
  - C04 (intermediário): zero rehash.
  - C05 (desejado): política reduzida não enfraquece.

## 48 — Identidade Unicode

- **Área:** Backend (.NET 10)
- **Foco:** normalização
- **Problema:** Normalizar identificadores com NFKC e comparação case-insensitive invariável.
- **Critérios discretos:**

  - C01 (mínimo): caixa é ignorada.
  - C02 (mínimo): full-width normaliza.
  - C03 (mínimo): acentos são preservados.
  - C04 (intermediário): compatibilidade normaliza.
  - C05 (desejado): espaço não é removido implicitamente.

## 49 — Paginação keyset

- **Área:** Backend (.NET 10)
- **Foco:** queries
- **Problema:** Decidir se registro vem depois do cursor composto `(score desc, id asc)`.
- **Critérios discretos:**

  - C01 (mínimo): score menor vem depois.
  - C02 (mínimo): score maior vem antes.
  - C03 (mínimo): empate ID maior vem depois.
  - C04 (intermediário): mesmo item não repete.
  - C05 (desejado): comparação é ordinal.

## 50 — Tokenização de busca

- **Área:** Backend (.NET 10)
- **Foco:** queries
- **Problema:** Normalizar termos, remover vazios e escapar curingas de LIKE.
- **Critérios discretos:**

  - C01 (mínimo): termos viram tokens.
  - C02 (mínimo): espaços repetidos somem.
  - C03 (mínimo): percentual é escapado.
  - C04 (intermediário): underscore é escapado.
  - C05 (desejado): barra é escapada primeiro.

## 51 — Plano de outbox

- **Área:** Backend (.NET 10)
- **Foco:** integração de dados
- **Problema:** Garantir que entidade e evento sejam gravados no mesmo commit lógico.
- **Critérios discretos:**

  - C01 (mínimo): save/event antes do commit é atômico.
  - C02 (mínimo): ordem interna pode variar.
  - C03 (mínimo): evento depois do commit é inseguro.
  - C04 (intermediário): save depois do commit é inseguro.
  - C05 (desejado): falha sem commit reverte.

## 52 — Migration expand-contract

- **Área:** Backend (.NET 10)
- **Foco:** evolução de schema
- **Problema:** Classificar passos compatíveis com deploy gradual.
- **Critérios discretos:**

  - C01 (mínimo): ordem expand-contract é segura.
  - C02 (mínimo): drop cedo é inseguro.
  - C03 (mínimo): backfill antes de coluna falha.
  - C04 (intermediário): leitura antes de backfill falha.
  - C05 (desejado): passo ausente falha.

## 53 — Upcasting de eventos

- **Área:** Backend (.NET 10)
- **Foco:** compatibilidade de schema
- **Problema:** Converter versões antigas para o modelo atual preservando significado.
- **Critérios discretos:**

  - C01 (mínimo): v1 recebe default.
  - C02 (mínimo): v2 preserva moeda.
  - C03 (mínimo): v3 não muda.
  - C04 (intermediário): texto Unicode preserva.
  - C05 (desejado): default é determinístico.

## 54 — Jitter de cache

- **Área:** Backend (.NET 10)
- **Foco:** cache
- **Problema:** Adicionar jitter determinístico por chave para evitar expiração simultânea.
- **Critérios discretos:**

  - C01 (mínimo): mesma chave é estável.
  - C02 (mínimo): outra chave varia.
  - C03 (mínimo): jitter fica pequeno.
  - C04 (intermediário): base é respeitada.
  - C05 (desejado): Unicode é determinístico.

## 55 — Invalidação por tags

- **Área:** Backend (.NET 10)
- **Foco:** cache
- **Problema:** Invalidar somente entradas dependentes da entidade alterada.
- **Critérios discretos:**

  - C01 (mínimo): produto invalida detalhe/lista.
  - C02 (mínimo): usuário não invalida catálogo.
  - C03 (mínimo): tag ausente gera vazio.
  - C04 (intermediário): múltiplas tags localizam.
  - C05 (desejado): ordem de saída é estável.

## 56 — Fencing token de lease

- **Área:** Backend (.NET 10)
- **Foco:** concorrência distribuída
- **Problema:** Aceitar escrita somente com token de fencing não inferior ao último observado.
- **Critérios discretos:**

  - C01 (mínimo): token novo aceita.
  - C02 (mínimo): token igual é idempotente.
  - C03 (mínimo): token antigo falha.
  - C04 (intermediário): zero inicial aceita.
  - C05 (desejado): número grande compara corretamente.

## 57 — Retry-After

- **Área:** Backend (.NET 10)
- **Foco:** resiliência HTTP
- **Problema:** Interpretar delta-seconds e limitar espera máxima.
- **Critérios discretos:**

  - C01 (mínimo): delta válido.
  - C02 (mínimo): espera é limitada.
  - C03 (mínimo): zero é válido.
  - C04 (intermediário): negativo é inválido.
  - C05 (desejado): texto é inválido.

## 58 — Circuit breaker half-open

- **Área:** Backend (.NET 10)
- **Foco:** resiliência
- **Problema:** Modelar transições closed/open/half-open sem liberar várias sondas.
- **Critérios discretos:**

  - C01 (mínimo): limiar abre.
  - C02 (mínimo): timeout permite sonda.
  - C03 (mínimo): sonda boa fecha.
  - C04 (intermediário): sonda ruim reabre.
  - C05 (desejado): request enquanto aberto rejeita.

## 59 — Isolamento por bulkhead

- **Área:** Backend (.NET 10)
- **Foco:** resiliência
- **Problema:** Admitir trabalho respeitando concorrência e fila limitada.
- **Critérios discretos:**

  - C01 (mínimo): slot livre executa.
  - C02 (mínimo): sem slot entra na fila.
  - C03 (mínimo): fila cheia rejeita.
  - C04 (intermediário): limite zero usa fila.
  - C05 (desejado): tudo zero rejeita.

## 60 — Compensação de saga

- **Área:** Backend (.NET 10)
- **Foco:** arquitetura distribuída
- **Problema:** Calcular compensações em ordem inversa apenas para etapas concluídas.
- **Critérios discretos:**

  - C01 (mínimo): duas etapas compensam inverso.
  - C02 (mínimo): falha inicial não compensa.
  - C03 (mínimo): sucesso completo define rollback potencial.
  - C04 (intermediário): uma etapa.
  - C05 (desejado): entrada vazia.

## 61 — Ordenação de eventos

- **Área:** Backend (.NET 10)
- **Foco:** mensageria
- **Problema:** Aplicar somente próxima versão, ignorar duplicata e detectar gap.
- **Critérios discretos:**

  - C01 (mínimo): próxima versão aplica.
  - C02 (mínimo): mesma versão duplica.
  - C03 (mínimo): versão antiga duplica.
  - C04 (intermediário): salto detecta gap.
  - C05 (desejado): primeiro evento aplica.

## 62 — Read-your-writes

- **Área:** Backend (.NET 10)
- **Foco:** consistência eventual
- **Problema:** Escolher réplica somente quando ela alcançou o token de consistência do cliente.
- **Critérios discretos:**

  - C01 (mínimo): réplica atual serve.
  - C02 (mínimo): réplica à frente serve.
  - C03 (mínimo): réplica atrasada usa primário.
  - C04 (intermediário): sem escrita lê réplica.
  - C05 (desejado): token grande não trunca.

## 63 — Cancelamento cooperativo

- **Área:** Backend (.NET 10)
- **Foco:** performance CPU
- **Problema:** Definir quantos itens são processados antes de observar cancelamento por chunks.
- **Critérios discretos:**

  - C01 (mínimo): cancela no primeiro chunk.
  - C02 (mínimo): cancela na borda seguinte.
  - C03 (mínimo): sem cancelamento processa tudo.
  - C04 (intermediário): total menor que chunk.
  - C05 (desejado): chunk unitário responde rápido.

## 64 — Canal com capacidade

- **Área:** Backend (.NET 10)
- **Foco:** producer-consumer
- **Problema:** Aplicar política wait/drop-oldest/drop-write quando buffer está cheio.
- **Critérios discretos:**

  - C01 (mínimo): há espaço escreve.
  - C02 (mínimo): cheio espera.
  - C03 (mínimo): drop oldest substitui.
  - C04 (intermediário): drop write descarta novo.
  - C05 (desejado): capacidade zero espera.

## 65 — Liberação de recursos

- **Área:** Backend (.NET 10)
- **Foco:** gestão de recursos
- **Problema:** Liberar recursos adquiridos em ordem inversa inclusive quando ocorre falha.
- **Critérios discretos:**

  - C01 (mínimo): dois recursos fecham inverso.
  - C02 (mínimo): falha fecha adquiridos.
  - C03 (mínimo): falha inicial não fecha.
  - C04 (intermediário): três recursos.
  - C05 (desejado): vazio.

## 66 — Navegação com formulário sujo

- **Área:** Frontend (React + TypeScript)
- **Foco:** roteamento
- **Problema:** Bloquear navegação somente quando há alterações não salvas.
- **Critérios discretos:**

  - C01 (mínimo): sujo pede confirmação.
  - C02 (mínimo): limpo navega.
  - C03 (mínimo): salvar não bloqueia.
  - C04 (intermediário): fechar aba confirma.
  - C05 (desejado): estado desconhecido não bloqueia.

## 67 — Estado sincronizado com URL

- **Área:** Frontend (Angular + TypeScript)
- **Foco:** roteamento
- **Problema:** Normalizar filtros em query string estável e compartilhável.
- **Critérios discretos:**

  - C01 (mínimo): query básica.
  - C02 (mínimo): page inválida vira um.
  - C03 (mínimo): espaços normalizam.
  - C04 (intermediário): Unicode codifica.
  - C05 (desejado): vazio tem defaults.

## 68 — Fallback de erro

- **Área:** Frontend (React + TypeScript)
- **Foco:** resiliência de UI
- **Problema:** Diferenciar erro recuperável, autenticação e falha fatal.
- **Critérios discretos:**

  - C01 (mínimo): rede tenta novamente.
  - C02 (mínimo): rede limita retry.
  - C03 (mínimo): auth pede login.
  - C04 (intermediário): render usa fallback.
  - C05 (desejado): fatal usa fallback.

## 69 — Estados de carregamento

- **Área:** Frontend (Angular + TypeScript)
- **Foco:** estado de UI
- **Problema:** Evitar spinner piscando e distinguir vazio, erro e sucesso.
- **Critérios discretos:**

  - C01 (mínimo): loading atrasado aparece.
  - C02 (mínimo): loading curto não pisca.
  - C03 (mínimo): zero itens é vazio.
  - C04 (intermediário): itens são sucesso.
  - C05 (desejado): erro prevalece.

## 70 — Pluralização de mensagens

- **Área:** Frontend (React + TypeScript)
- **Foco:** i18n
- **Problema:** Aplicar regras de plural sem concatenação inglesa fixa.
- **Critérios discretos:**

  - C01 (mínimo): pt singular.
  - C02 (mínimo): pt plural.
  - C03 (mínimo): pt zero plural.
  - C04 (intermediário): en singular.
  - C05 (desejado): en plural.

## 71 — Data no fuso do usuário

- **Área:** Frontend (Angular + TypeScript)
- **Foco:** datas
- **Problema:** Escolher o dia civil usando offset fornecido sem depender da máquina.
- **Critérios discretos:**

  - C01 (mínimo): offset cruza para ontem.
  - C02 (mínimo): UTC preserva dia.
  - C03 (mínimo): offset cruza amanhã.
  - C04 (intermediário): meia-noite local.
  - C05 (desejado): ano novo local.

## 72 — Foco em modal

- **Área:** Frontend (React + TypeScript)
- **Foco:** acessibilidade
- **Problema:** Ciclar foco, restaurá-lo e tratar modal sem controles.
- **Critérios discretos:**

  - C01 (mínimo): Tab avança.
  - C02 (mínimo): último volta ao primeiro.
  - C03 (mínimo): ShiftTab retrocede.
  - C04 (intermediário): Escape restaura.
  - C05 (desejado): sem controles foca container.

## 73 — Combobox acessível

- **Área:** Frontend (Angular + TypeScript)
- **Foco:** acessibilidade
- **Problema:** Filtrar opções e manter active descendant válido.
- **Critérios discretos:**

  - C01 (mínimo): filtra sem caixa.
  - C02 (mínimo): active inválido muda.
  - C03 (mínimo): sem resultado limpa active.
  - C04 (intermediário): vazio mantém active.
  - C05 (desejado): primeira opção vira active.

## 74 — Reordenação por teclado

- **Área:** Frontend (React + TypeScript)
- **Foco:** acessibilidade
- **Problema:** Mover item pela lista com setas preservando os demais.
- **Critérios discretos:**

  - C01 (mínimo): move para cima.
  - C02 (mínimo): move para baixo.
  - C03 (mínimo): topo não sai.
  - C04 (intermediário): fim não sai.
  - C05 (desejado): ID ausente não muda.

## 75 — Tabela responsiva

- **Área:** Frontend (Angular + TypeScript)
- **Foco:** responsividade
- **Problema:** Selecionar colunas essenciais por largura sem esconder ações críticas.
- **Critérios discretos:**

  - C01 (mínimo): celular tem essenciais.
  - C02 (mínimo): limite celular.
  - C03 (mínimo): tablet inclui status.
  - C04 (intermediário): desktop completo.
  - C05 (desejado): limite desktop.

## 76 — Virtualização com alturas

- **Área:** Frontend (React + TypeScript)
- **Foco:** performance
- **Problema:** Calcular intervalo visível a partir de alturas variáveis e overscan.
- **Critérios discretos:**

  - C01 (mínimo): primeira janela.
  - C02 (mínimo): offset pula linhas.
  - C03 (mínimo): overscan expande.
  - C04 (intermediário): viewport parcial inclui item.
  - C05 (desejado): fim é limitado.

## 77 — Dependências de memoização

- **Área:** Frontend (Angular + TypeScript)
- **Foco:** performance
- **Problema:** Construir chave incluindo todas as entradas que afetam o cálculo.
- **Critérios discretos:**

  - C01 (mínimo): inclui usuário.
  - C02 (mínimo): inclui locale.
  - C03 (mínimo): ordem de itens estabiliza.
  - C04 (intermediário): lista vazia.
  - C05 (desejado): usuários não colidem.

## 78 — Closure obsoleta

- **Área:** Frontend (React + TypeScript)
- **Foco:** estado assíncrono
- **Problema:** Aplicar atualizações funcionais acumuladas em vez de snapshot capturado.
- **Critérios discretos:**

  - C01 (mínimo): dois ticks acumulam.
  - C02 (mínimo): parte de valor atual.
  - C03 (mínimo): delta negativo.
  - C04 (intermediário): nenhum tick preserva.
  - C05 (desejado): muitos ticks.

## 79 — Atualização imutável

- **Área:** Frontend (Angular + TypeScript)
- **Foco:** estado
- **Problema:** Atualizar item aninhado preservando referências não afetadas por ID.
- **Critérios discretos:**

  - C01 (mínimo): altera alvo.
  - C02 (mínimo): preserva outros.
  - C03 (mínimo): ausente não muda.
  - C04 (intermediário): primeiro funciona.
  - C05 (desejado): valor vazio permitido.

## 80 — Reducer de fluxo

- **Área:** Frontend (React + TypeScript)
- **Foco:** arquitetura frontend
- **Problema:** Modelar transições válidas de um wizard sem estados impossíveis.
- **Critérios discretos:**

  - C01 (mínimo): submit inicia envio.
  - C02 (mínimo): sucesso conclui.
  - C03 (mínimo): falha retorna edição.
  - C04 (intermediário): reset reabre.
  - C05 (desejado): evento inválido preserva.

## 81 — Validação assíncrona de campo

- **Área:** Frontend (Angular + TypeScript)
- **Foco:** forms
- **Problema:** Aceitar resultado somente da geração mais recente.
- **Critérios discretos:**

  - C01 (mínimo): resultado atual aplica.
  - C02 (mínimo): antigo ignora.
  - C03 (mínimo): futuro ignora.
  - C04 (intermediário): primeira geração.
  - C05 (desejado): zero inicial.

## 82 — Progresso de upload

- **Área:** Frontend (React + TypeScript)
- **Foco:** integração
- **Problema:** Calcular progresso limitado e representar cancelamento.
- **Critérios discretos:**

  - C01 (mínimo): metade.
  - C02 (mínimo): completo.
  - C03 (mínimo): excesso limita.
  - C04 (intermediário): total desconhecido.
  - C05 (desejado): cancelado prevalece.

## 83 — Scroll infinito sem duplicatas

- **Área:** Frontend (Angular + TypeScript)
- **Foco:** paginação
- **Problema:** Mesclar páginas por ID mantendo a primeira ordem e a versão mais nova.
- **Critérios discretos:**

  - C01 (mínimo): páginas distintas concatenam.
  - C02 (mínimo): duplicata atualiza.
  - C03 (mínimo): página vazia.
  - C04 (intermediário): primeira vazia.
  - C05 (desejado): várias duplicatas não repetem.

## 84 — Reconexão WebSocket

- **Área:** Frontend (React + TypeScript)
- **Foco:** tempo real
- **Problema:** Calcular backoff exponencial limitado e resetar após conexão estável.
- **Critérios discretos:**

  - C01 (mínimo): primeira espera.
  - C02 (mínimo): segunda dobra.
  - C03 (mínimo): quinta cresce.
  - C04 (intermediário): limite mantém.
  - C05 (desejado): estável reseta.

## 85 — Fila offline

- **Área:** Frontend (Angular + TypeScript)
- **Foco:** offline-first
- **Problema:** Compactar comandos consecutivos sobre a mesma entidade sem perder delete.
- **Critérios discretos:**

  - C01 (mínimo): updates compactam.
  - C02 (mínimo): delete vence update anterior.
  - C03 (mínimo): update não ressuscita delete.
  - C04 (intermediário): IDs distintos permanecem.
  - C05 (desejado): vazio.

## 86 — Versão de cache offline

- **Área:** Frontend (React + TypeScript)
- **Foco:** service worker
- **Problema:** Escolher cache atual e remover versões antigas do mesmo aplicativo.
- **Critérios discretos:**

  - C01 (mínimo): remove versão anterior.
  - C02 (mínimo): preserva outro app.
  - C03 (mínimo): remove múltiplas antigas.
  - C04 (intermediário): sem caches.
  - C05 (desejado): não remove atual.

## 87 — Texto rico seguro

- **Área:** Frontend (Angular + TypeScript)
- **Foco:** segurança XSS
- **Problema:** Escapar HTML não confiável sem remover texto Unicode.
- **Critérios discretos:**

  - C01 (mínimo): script vira texto.
  - C02 (mínimo): ampersand escapa.
  - C03 (mínimo): aspas escapam.
  - C04 (intermediário): apóstrofo escapa.
  - C05 (desejado): Unicode permanece.

## 88 — Sanitização de links

- **Área:** Frontend (React + TypeScript)
- **Foco:** segurança
- **Problema:** Permitir apenas http/https/mailto e caminhos locais seguros.
- **Critérios discretos:**

  - C01 (mínimo): https permite.
  - C02 (mínimo): mailto permite.
  - C03 (mínimo): javascript bloqueia.
  - C04 (intermediário): caminho local permite.
  - C05 (desejado): protocol-relative bloqueia.

## 89 — Envio de CSRF

- **Área:** Frontend (Angular + TypeScript)
- **Foco:** segurança
- **Problema:** Anexar token somente em mutações same-origin.
- **Critérios discretos:**

  - C01 (mínimo): POST local recebe token.
  - C02 (mínimo): GET não recebe.
  - C03 (mínimo): origem externa não recebe.
  - C04 (intermediário): token ausente não inventa.
  - C05 (desejado): DELETE local recebe.

## 90 — Nonce de CSP

- **Área:** Frontend (React + TypeScript)
- **Foco:** segurança
- **Problema:** Propagar nonce recebido somente a scripts dinâmicos confiáveis.
- **Critérios discretos:**

  - C01 (mínimo): script confiável recebe nonce.
  - C02 (mínimo): não confiável bloqueia.
  - C03 (mínimo): nonce ausente bloqueia.
  - C04 (intermediário): valor é preservado.
  - C05 (desejado): não inventa nonce.

## 91 — Imports tree-shakable

- **Área:** Frontend (Angular + TypeScript)
- **Foco:** bundle size
- **Problema:** Classificar import granular como seguro e barrel amplo como custo evitável.
- **Critérios discretos:**

  - C01 (mínimo): submódulo é granular.
  - C02 (mínimo): pacote inteiro é pesado.
  - C03 (mínimo): barrel all é pesado.
  - C04 (intermediário): arquivo index é pesado.
  - C05 (desejado): função direta é granular.

## 92 — Rotas lazy

- **Área:** Frontend (React + TypeScript)
- **Foco:** bundle size
- **Problema:** Carregar área administrativa em chunk separado e manter shell imediato.
- **Critérios discretos:**

  - C01 (mínimo): admin lazy está correto.
  - C02 (mínimo): admin eager viola.
  - C03 (mínimo): subrota admin também.
  - C04 (intermediário): home pode ser eager.
  - C05 (desejado): login eager é aceitável.

## 93 — Imagem responsiva

- **Área:** Frontend (Angular + TypeScript)
- **Foco:** performance web
- **Problema:** Escolher menor candidato suficiente para viewport e DPR.
- **Critérios discretos:**

  - C01 (mínimo): viewport simples.
  - C02 (mínimo): DPR dois dobra alvo.
  - C03 (mínimo): menor suficiente.
  - C04 (intermediário): alvo maior usa máximo.
  - C05 (desejado): entrada desordenada funciona.

## 94 — Ciclo de listeners

- **Área:** Frontend (React + TypeScript)
- **Foco:** memory leaks
- **Problema:** Equilibrar add/remove em montagens repetidas.
- **Critérios discretos:**

  - C01 (mínimo): monta/desmonta limpa.
  - C02 (mínimo): montagem sem cleanup vaza.
  - C03 (mínimo): duas instâncias limpas.
  - C04 (intermediário): cleanup extra inválido.
  - C05 (desejado): uma sobra detecta.

## 95 — Limpeza de observers

- **Área:** Frontend (Angular + TypeScript)
- **Foco:** memory leaks
- **Problema:** Desconectar observers e cancelar timers ao destruir componente.
- **Critérios discretos:**

  - C01 (mínimo): observer limpo.
  - C02 (mínimo): timer limpo.
  - C03 (mínimo): um recurso vaza.
  - C04 (intermediário): dois limpos.
  - C05 (desejado): nenhum recurso.

## 96 — Particionamento para Web Worker

- **Área:** Frontend (React + TypeScript)
- **Foco:** performance CPU
- **Problema:** Dividir itens em chunks equilibrados sem perda.
- **Critérios discretos:**

  - C01 (mínimo): divide igualmente.
  - C02 (mínimo): distribui resto.
  - C03 (mínimo): mais workers que itens.
  - C04 (intermediário): zero itens.
  - C05 (desejado): zero workers vira um.

## 97 — Reordenação otimista

- **Área:** Frontend (Angular + TypeScript)
- **Foco:** estado otimista
- **Problema:** Reaplicar intenção do usuário após versão nova do servidor.
- **Critérios discretos:**

  - C01 (mínimo): move antes de item.
  - C02 (mínimo): move ao fim.
  - C03 (mínimo): estado novo preserva item novo.
  - C04 (intermediário): ID ausente é inserido.
  - C05 (desejado): alvo ausente vai ao início.

## 98 — Merge em tempo real

- **Área:** Frontend (React + TypeScript)
- **Foco:** colaboração
- **Problema:** Mesclar campos independentes e marcar conflito quando ambos alteram o mesmo campo.
- **Critérios discretos:**

  - C01 (mínimo): só remoto muda.
  - C02 (mínimo): só local muda.
  - C03 (mínimo): mudanças iguais mesclam.
  - C04 (intermediário): mudanças diferentes conflitam.
  - C05 (desejado): nenhuma mudança usa merged.

## 99 — Tokens de tema

- **Área:** Frontend (Angular + TypeScript)
- **Foco:** design system
- **Problema:** Resolver token por tema com fallback para base sem cores hardcoded.
- **Critérios discretos:**

  - C01 (mínimo): tema base.
  - C02 (mínimo): dark sobrescreve.
  - C03 (mínimo): dark herda accent.
  - C04 (intermediário): token ausente.
  - C05 (desejado): texto dark.

## 100 — Teste de UI determinístico

- **Área:** Frontend (React + TypeScript)
- **Foco:** qualidade de testes
- **Problema:** Escolher espera baseada em estado observável em vez de timeout fixo.
- **Critérios discretos:**

  - C01 (mínimo): evento pronto passa.
  - C02 (mínimo): poll pronto passa.
  - C03 (mínimo): sleep é frágil.
  - C04 (intermediário): estado incompleto não passa.
  - C05 (desejado): timeout fixo continua frágil.
