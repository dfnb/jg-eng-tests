# Plano de execução

## Estado deste roteiro

| Etapa | Estado |
| --- | --- |
| Fundação e ferramentas comuns | concluída |
| Seis pilotos | concluída |
| Núcleo profissional | concluída |
| Performance e sistemas distribuídos | concluída |
| Projeto aberto e pipeline | concluída |
| Validação automatizada e empacotamento 1.0 | concluída |
| Expansão 31–100 | concluída |
| Expansão com bases de produção 101–130 | concluída |
| Calibração com turmas reais | atividade operacional futura |

Todos os 130 exercícios estão implementados. A calibração com estudantes permanece como ciclo contínuo de manutenção e não como pendência de código.

## Resultado planejado

Entregar 130 exercícios autocontidos, com solução de referência, avaliador privado, documentação pedagógica e empacotamento seguro. Os primeiros 30 formam o núcleo, os itens 31–100 ampliam competências e os itens 101–130 acrescentam navegação em bases maiores conforme [EXPANSION_PLAN_130.md](EXPANSION_PLAN_130.md).

## Fase 0 — Fundação

**Objetivo:** estabelecer contratos antes de produzir código.

- definir estrutura, nomenclatura e templates;
- definir rubrica discreta e formato JSON do avaliador;
- criar validador estrutural da coleção;
- criar empacotador que exporta somente material do estudante;
- configurar verificações de segredos, licenças e referências privadas;
- preparar uma imagem/ambiente de desenvolvimento com SDKs compartilhados.

**Saída:** documentação atual mais scripts comuns testados.

## Fase 1 — Seis pilotos

Implementar um exercício representativo de cada trilha:

1. `01-loyalty-discount` — feature backend;
2. `07-accessible-checkout` — interface React;
3. `12-timezone-scheduling` — bug;
4. `17-catalog-n-plus-one` — performance;
5. `22-cross-tenant-orders` — segurança;
6. `29-reproducible-local-env` — infraestrutura.

Os pilotos validam:

- tempo real de setup e execução;
- clareza do README e do desafio;
- isolamento entre material público e privado;
- estabilidade do avaliador em ambiente limpo;
- distribuição de pontuação e qualidade das mensagens;
- duração com pelo menos três resoluções externas por exercício.

**Gate:** nenhum lote seguinte começa antes de os seis pilotos passarem por uma retrospectiva e os templates serem atualizados.

## Fase 2 — Núcleo profissional

Implementar os exercícios 02–06, 08, 13–16, 20, 23, 25 e 28. Esse lote cobre tarefas frequentes de júnior/intermediário: features, bugs, dados, refatoração, integração e automação.

**Gate:** cada exercício precisa de revisão cruzada, solução alternativa e pelo menos um mutante detectado por critério essencial.

## Fase 3 — Performance e sistemas distribuídos

Implementar 09–11, 18, 19, 21, 24 e 26. Estes exercícios exigem harnesses mais sensíveis e entram depois de o executor comum estar estável.

**Gate:** executar os avaliadores repetidamente no ambiente de referência sem flakiness e registrar baselines de recursos.

## Fase 4 — Projeto aberto e pipeline

Implementar 27 e 30. O projeto do zero vem no fim porque reutiliza convenções validadas nos demais; o pipeline valida a coleção full stack.

**Gate:** soluções estruturalmente diferentes devem ser aceitas desde que satisfaçam os contratos.

## Fase 5 — Calibração e publicação 1.0

- aplicar os exercícios a uma amostra de estudantes e profissionais;
- comparar tempo estimado com tempo observado;
- remover pistas excessivas e ruído não intencional;
- revisar acessibilidade, segurança e licenças;
- congelar versões e gerar checksums dos pacotes;
- publicar guia do avaliador e matriz de competências.

## Ordem dentro de cada exercício

1. Proposta curta com competência, duração e risco.
2. Critérios automatizáveis e fixtures.
3. Repositório resolvido e solução de referência.
4. Avaliador privado.
5. Derivação do estado inicial defeituoso/incompleto.
6. README e CHALLENGE.
7. Mutantes e solução alternativa.
8. Revisão técnica e pedagógica.
9. Empacotamento limpo.

## Definição de pronto

Um exercício só recebe estado `ready` quando:

- seu diretório segue o contrato estrutural;
- uma máquina limpa executa os comandos documentados;
- os testes públicos passam no estado inicial, salvo exceção justificada;
- o avaliador falha no estado inicial pelas razões planejadas;
- a referência passa em 100% dos critérios;
- cada mínimo possui teste independente e mensagem útil;
- ao menos uma solução alternativa válida passa;
- mutantes representam correções ingênuas e são rejeitados;
- duração e nível foram calibrados por execução externa;
- pacote final contém apenas `exercise/` e nenhuma informação privada.

## Acompanhamento

Cada exercício terá um estado: `proposed`, `designing`, `implementing`, `validating` ou `ready`. Um manifesto futuro na raiz guardará estado, versão, stack, duração e checksum. Mudanças que alterem enunciado ou critérios incrementam a versão do exercício.

## Riscos e respostas

| Risco | Resposta planejada |
| --- | --- |
| Testes frágeis de performance | medir operações e usar ambiente controlado antes de tempo de parede |
| Exercícios grandes demais | uma competência principal, limite de duração e revisão por diff ideal |
| Enunciado entrega a solução | revisão separada por alguém que não criou o exercício |
| Avaliador acoplado à referência | executar solução alternativa e preferir contratos públicos |
| Vazamento de arquivos privados | empacotamento allowlist e varredura automática |
| Dependências envelhecidas | versões fixas, revisão periódica e versão por exercício |
| Setup consome o tempo do estudante | scripts uniformes, fixtures locais e teste em máquina limpa |
| Correção por hardcoding | casos privados variados, propriedades e sementes registradas |

## Manutenção após 1.0

- verificação automatizada semanal de build e dependências;
- rodada trimestral de execução completa em ambiente limpo;
- correções compatíveis na versão patch;
- alteração de contrato somente em versão major do exercício;
- exercícios aposentados permanecem identificáveis para comparar resultados históricos.
