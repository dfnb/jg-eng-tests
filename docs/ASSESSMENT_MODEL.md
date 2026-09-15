# Modelo de avaliação

## Objetivo

A correção combina uma barreira mínima obrigatória com critérios discretos de qualidade. Isso evita aprovar uma solução bonita que não funciona e também diferencia uma correção frágil de uma solução pronta para manutenção.

## Critérios discretos

Cada exercício terá de 5 a 8 critérios independentes. Um critério recebe `pass` ou `fail`; não há pontuação subjetiva parcial dentro dele. Os pesos permitidos são 1, 2 ou 3:

- peso 3: comportamento essencial ou proteção contra dano relevante;
- peso 2: caso importante, robustez ou teste significativo;
- peso 1: qualidade adicional observável.

Todo critério deve declarar:

| Campo | Função |
| --- | --- |
| ID | referência estável, como `C03` |
| Nível | mínimo, intermediário ou desejado |
| Peso | 1, 2 ou 3 |
| Condição | afirmação única e verificável |
| Verificação | teste ou analisador que decide o resultado |
| Evidência de falha | mensagem útil, sem revelar a solução |

## Regra de aprovação

Uma submissão é aprovada quando:

1. todos os critérios marcados como **mínimos** passam;
2. a suíte original do projeto continua passando;
3. não há alteração em arquivos explicitamente protegidos;
4. a pontuação total atinge pelo menos 60%.

As faixas sugeridas são:

| Resultado | Condição |
| --- | --- |
| Ainda não atende | algum mínimo falhou ou pontuação abaixo de 60% |
| Adequado | mínimos atendidos e 60–74% |
| Bom | mínimos atendidos e 75–89% |
| Excelente | mínimos atendidos e 90–100% |

A pontuação ajuda a ordenar evidências, mas o relatório deve mostrar critérios individualmente. O número isolado não explica a competência demonstrada.

## O que automatizar

- resposta de API, eventos e efeitos persistidos;
- estados de interface e acessibilidade verificável;
- tempo ou número de operações dentro de limites estáveis;
- consistência sob execução concorrente;
- comportamento diante de falhas simuladas;
- presença de testes relevantes do estudante;
- build, lint, análise de dependências e scanners determinísticos;
- idempotência de scripts e provisionamento.

Métricas de performance usam orçamento amplo, ambiente controlado e, preferencialmente, contadores de consultas/operações em vez de milissegundos frágeis.

## Avaliação manual complementar

Pode existir, mas não altera automaticamente o resultado. Serve para entrevista e feedback sobre:

- clareza do raciocínio e comunicação;
- adequação dos nomes e limites de abstração;
- qualidade dos commits, quando solicitados;
- capacidade de explicar alternativas e riscos.

Esses itens nunca devem ser escondidos dentro de um critério supostamente objetivo.

## Proteção contra soluções acidentais

Antes da publicação, o avaliador deve ser executado em quatro estados:

1. exercício intacto: os critérios do desafio falham pelas razões esperadas;
2. solução de referência: todos passam;
3. mutações deliberadas: cada teste detecta pelo menos uma implementação incorreta plausível;
4. solução alternativa válida: não é rejeitada por acoplamento indevido à referência.

## Integridade

Os testes privados não serão distribuídos. Os testes públicos explicam contratos básicos, mas a combinação de casos, limites e fixtures privadas reduz hardcoding. Dados de entrada variam entre execuções quando isso não prejudica a reprodutibilidade; a semente usada deve aparecer no relatório do avaliador.
