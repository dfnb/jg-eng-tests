# Busca fora de ordem

Este repositório simula a busca incremental React cujo transporte simula respostas com latências diferentes.

## Stack

    react, typescript, Node.js 24.15.0 (fixado em `.node-version`). A lógica testável está em `src/challenge.ts`; o componente do framework está ao lado dela.

## Executar

```bash
./scripts/setup.sh
./scripts/test.sh
./scripts/lint.sh
```

Os testes públicos cobrem apenas o ambiente e o caminho básico. Preserve as exportações existentes.
