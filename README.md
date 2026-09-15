# Software Engineering Workbench

Coleção de exercícios que simulam situações comuns de produção de software e permitem avaliar, de forma objetiva, como estudantes de engenharia de software investigam, implementam, testam e explicam mudanças em bases de código realistas.

O foco não é medir memorização de sintaxe. Cada exercício entrega um repositório funcional e autocontido, com tudo o que não faz parte do problema já preparado. O estudante deve gastar seu tempo entendendo o contexto, tomando decisões e resolvendo apenas o desafio proposto.

## Escopo

A coleção contém **130 exercícios**. Os 30 itens iniciais estabelecem as trilhas fundamentais, a expansão 31–100 amplia a variedade e os itens 101–130 usam bases com porte de pequena aplicação de produção:

| Trilha | Exercícios | Foco |
| --- | ---: | --- |
| Backend e dados | 6 | C#, .NET 10, APIs, persistência e consultas |
| Frontend | 5 | TypeScript, React ou Angular, estado e interfaces |
| Bugs e qualidade | 5 | diagnóstico, testes, refatoração e legibilidade |
| Performance e concorrência | 5 | gargalos, assincronismo e consistência distribuída |
| Segurança e integração | 5 | controles de segurança, APIs externas e resiliência |
| DevEx, scripts e infraestrutura | 4 | automação, Docker Compose e criação de projetos |
| Contratos HTTP e APIs | 10 | versionamento, precondições, idempotência, ranges e rate limiting |
| Segurança backend | 8 | autorização, tokens, redaction, SSRF, redirects e binding seguro |
| Dados e cache avançados | 7 | keyset, migrations, evolução de eventos e invalidação |
| Resiliência e sistemas distribuídos | 10 | fencing, circuit breaker, sagas, ordenação e backpressure |
| Frontend avançado | 35 | roteamento, a11y, estado, offline, segurança, performance e colaboração |
| Backend em base de produção | 15 | navegação em domínio, aplicação, infraestrutura e API |
| Frontend em base de produção | 15 | navegação em features, estado, serviços, componentes e utilitários |

Os catálogos detalhados estão em [docs/EXERCISE_CATALOG.md](docs/EXERCISE_CATALOG.md), [docs/EXERCISES_31_100.md](docs/EXERCISES_31_100.md) e [docs/EXERCISES_101_130.md](docs/EXERCISES_101_130.md).

## Organização

Cada exercício ficará em `exercises/NN-slug/`:

```text
exercises/NN-slug/
├── exercise/          # único diretório entregue ao estudante
│   ├── README.md      # contexto do produto e como executar o projeto
│   ├── CHALLENGE.md   # pedido, restrições e forma de entrega
│   └── ...            # repositório simulado completo
├── solution/          # implementação de referência para o avaliador
├── grader/            # testes e ferramentas privadas de avaliação
└── EVALUATION.md      # intenção, rubrica e armadilhas do exercício
```

O diretório `exercise/` nunca pode depender de arquivos dos outros três diretórios. Ele deve poder ser copiado, versionado e executado isoladamente.

## Princípios

- O enunciado descreve comportamento e contexto, não dita a implementação.
- Só o problema avaliado fica incompleto ou defeituoso.
- Instalação, dados de exemplo e dependências locais devem ser reproduzíveis.
- Critérios obrigatórios são binários e verificáveis por testes.
- Qualidade acima do mínimo é medida por critérios discretos, não por impressão geral.
- A solução de referência demonstra uma solução sólida, mas não é a única solução aceita.
- Testes privados verificam resultados e propriedades observáveis, evitando exigir detalhes internos desnecessários.
- Todo exercício deve funcionar sem credenciais ou serviços pagos.

Para manter os desafios rápidos e determinísticos, integrações externas e persistência são representadas por contratos e implementações locais na maioria dos exercícios. PostgreSQL, Redis e containers reais ficam concentrados nos exercícios em que a infraestrutura é a competência avaliada.

## Documentação do projeto

- [Plano de execução](docs/ROADMAP.md)
- [Catálogo dos exercícios 01–30](docs/EXERCISE_CATALOG.md)
- [Catálogo dos exercícios 31–100](docs/EXERCISES_31_100.md)
- [Plano da expansão para 100](docs/EXPANSION_PLAN_100.md)
- [Catálogo dos exercícios 101–130](docs/EXERCISES_101_130.md)
- [Plano de bases com porte de produção](docs/EXPANSION_PLAN_130.md)
- [Arquitetura da coleção](docs/REPOSITORY_ARCHITECTURE.md)
- [Modelo de avaliação](docs/ASSESSMENT_MODEL.md)
- [Guia para criar exercícios](docs/AUTHORING_GUIDE.md)
- [Padrões técnicos](docs/TECHNICAL_STANDARDS.md)
- [Estado e validação da implementação](docs/IMPLEMENTATION_STATUS.md)

## Estado

Os 130 exercícios estão implementados e marcados como `ready` no `catalog.json`. As referências passam em todos os graders privados e cada estado inicial falha deliberadamente em pelo menos um critério mínimo. Nos itens 101–130, o validador também exige no mínimo 40 arquivos e 800 linhas não vazias de código de produção por variante.

## Operação da coleção

```bash
# Validar estrutura e isolamento
python3 scripts/validate-structure.py

# Executar graders contra todas as referências
python3 scripts/run-graders.py

# Confirmar que nenhum exercício já começa resolvido
python3 scripts/audit-initial-states.py

# Executar testes públicos dos dois estados
python3 scripts/run-public-tests.py

# Gerar o pacote entregue ao estudante
python3 scripts/package-exercise.py 01
```

Em máquinas onde o SDK foi instalado pelo mise, ative a versão configurada pelo mise antes dos comandos .NET.
