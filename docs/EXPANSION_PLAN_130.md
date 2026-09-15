# Plano de expansão 101–130: bases de produção

## Motivação

Os exercícios 101–130 adicionam uma competência deliberadamente ausente nos itens anteriores: navegar, formar um modelo mental e localizar a mudança correta em uma base semelhante a uma aplicação pequena de produção. O defeito ou feature continua focalizado, mas não aparece isolado em um projeto de duas ou três classes.

## Contrato de tamanho

Cada variante de cada exercício desta expansão deve possuir:

- pelo menos 40 arquivos de código de produção;
- pelo menos 800 linhas não vazias em `src/`;
- ao menos seis diretórios funcionais;
- camadas de domínio, aplicação, integração/infraestrutura e entrada pública;
- testes públicos, scripts uniformes, solução, grader e rubrica privada;
- somente uma lacuna deliberada ligada ao desafio.

O validador estrutural mede esses limites. Arquivos repetidos apenas para aumentar contagem não são suficientes: os módulos modelam entidades, repositórios, serviços, estado, adaptadores, utilitários e componentes coerentes com a aplicação simulada.

## Distribuição

| IDs | Área | Quantidade | Temas novos |
| --- | --- | ---: | --- |
| 101–115 | Backend .NET 10 | 15 | aprovação, contabilidade, configuração, histórico, alocação, digest, retenção, rotação, readiness, rollout, shutdown, fan-out, sunset, tracing e deadlocks |
| 116–130 | Frontend | 15 | permissões, undo/redo, autosave, wizard, gráficos acessíveis, movimento reduzido, números locais, identidade, cache, SSR, streaming, quota, clipboard, impressão e microfrontends |

## Estratégia de avaliação

O estudante recebe contexto do produto e comportamento esperado, mas não recebe o caminho do arquivo defeituoso. O grader entra pela API pública da aplicação, atravessando as mesmas fronteiras usadas pelo produto. Cinco critérios binários verificam cada exercício: três mínimos, um intermediário e um desejado.

## Gate de publicação

Todos os 30 itens precisam passar em referência, falhar no mínimo no estado inicial, executar testes públicos e lint/build nas duas variantes, cumprir o perfil de tamanho e gerar pacote sem material privado.
