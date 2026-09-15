# Arquitetura da coleção

## Estrutura de alto nível

```text
.
├── README.md
├── docs/
├── exercises/
│   └── NN-slug/
│       ├── exercise/
│       ├── solution/
│       ├── grader/
│       └── EVALUATION.md
├── templates/
└── scripts/
```

`scripts/` concentrará comandos da coleção, como validação estrutural, execução dos avaliadores e empacotamento da versão entregue aos estudantes. Esses comandos não substituem os scripts que cada repositório simulado precisa oferecer.

## Contrato de um exercício

### `exercise/`

É um repositório simulado e a única parte visível para o estudante. Deve conter:

- `README.md` com domínio da aplicação, arquitetura relevante, pré-requisitos e comandos;
- `CHALLENGE.md` com objetivo, comportamento esperado, restrições e forma de entrega;
- código e configuração suficientes para iniciar o trabalho imediatamente;
- testes públicos que ajudem a verificar o ambiente, sem revelar toda a avaliação;
- scripts equivalentes `setup`, `start`, `test`, `lint` e, quando aplicável, `reset-data`;
- `.env.example`, dados sintéticos e Docker Compose quando houver dependências de infraestrutura;
- histórico Git opcional apenas quando o exercício avaliar investigação histórica.

O projeto inicial deve executar. A única exceção é quando falha de build, configuração ou inicialização for explicitamente o objeto do exercício.

### `solution/`

Cópia independente do repositório com uma implementação de referência. Deve:

- satisfazer todos os critérios desejados;
- incluir testes adicionados pela solução;
- preservar o escopo e evitar melhorias não relacionadas;
- conter `SOLUTION_NOTES.md` explicando decisões, alternativas válidas e limitações;
- executar com os mesmos comandos documentados no exercício.

### `grader/`

Área privada do avaliador. Contém testes comportamentais, fixtures, analisadores estáticos e um comando único `run`. O avaliador deve produzir resultado legível por máquina, inicialmente JSON, além de saída humana.

Exemplo de resultado:

```json
{
  "exercise": "01-order-discount",
  "criteria": [
    { "id": "C01", "status": "pass", "points": 2 },
    { "id": "C02", "status": "fail", "points": 0 }
  ],
  "score": 2,
  "maximum": 10,
  "minimumPassed": false
}
```

Os testes devem observar contratos públicos sempre que possível. Inspeção de código é reservada a requisitos que não podem ser comprovados externamente, como ausência de segredo ou uso correto de consulta parametrizada.

### `EVALUATION.md`

Documento privado com:

- competência e nível pretendido;
- tecnologias utilizadas;
- duração estimada;
- pré-requisitos;
- o que está deliberadamente incompleto ou quebrado;
- sinais que o estudante deve descobrir;
- armadilhas introduzidas e falsos caminhos;
- critérios mínimos, intermediários e desejados;
- vínculo de cada critério com um teste automatizado;
- soluções alternativas aceitas;
- roteiro para avaliação manual complementar;
- instruções para restaurar o estado inicial.

## Isolamento e distribuição

O comando futuro `scripts/package-exercise` copiará apenas `exercise/`, removerá artefatos locais e produzirá um arquivo com checksum. O processo deve falhar se encontrar referências a `solution/`, `grader/` ou `EVALUATION.md` dentro do material do estudante.

## Identificação

- Diretórios usam número de dois dígitos e slug em inglês: `01-order-discount`.
- Critérios usam identificadores estáveis `C01`, `C02`, etc.
- Testes privados incluem o identificador do critério que comprovam.
- IDs não são reutilizados quando um critério é removido.

## Limites de realismo

Os repositórios devem parecer aplicações reais, mas o volume de código deve servir ao diagnóstico. Código decorativo, microsserviços desnecessários e dependências sem função pedagógica aumentam ruído e devem ser evitados. Nomes, dados e segredos serão sempre fictícios.
