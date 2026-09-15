# Estado da implementação

## Coleção completa

Os 130 exercícios planejados estão implementados. Cada diretório contém:

- repositório incompleto/defeituoso em `exercise/`;
- implementação de referência e notas em `solution/`;
- grader privado com resultado JSON em `grader/`;
- rubrica, intenção e armadilhas em `EVALUATION.md`;
- comandos `setup`, `start`, `test` e `lint` no material do estudante e na referência.

## Evidências de validação

| Verificação | Resultado |
| --- | --- |
| Quantidade e estrutura | 130/130 válidos |
| Graders nas referências | 130/130 aprovados, 100% dos critérios |
| Auditoria dos estados iniciais | 130/130 falham em pelo menos um mínimo |
| Testes públicos | 260/260 variantes executáveis e aprovadas |
| Lint/build das expansões | 200/200 variantes aprovadas |
| Lockfiles frontend | presentes nos 55 exercícios, em ambos os estados |
| Perfil 101–130 | 55–59 arquivos e 954–1.030 linhas não vazias em `src/` por variante |
| Pacotes e checksums | 130 ZIPs, 130 checksums válidos e nenhum arquivo privado |
| Dependências npm | 0 vulnerabilidades reportadas na geração dos lockfiles |

Os graders C# foram executados com SDK .NET 10.0.401 instalado pelo mise. Os testes frontend foram executados com o runner nativo do Node; os repositórios fixam Node 24.15.0 em `.node-version` para compatibilidade com Angular 22.

O exercício 29 teve seu Compose validado sintaticamente e por regras privadas. A subida completa de containers depende do daemon Docker disponível na máquina do avaliador.

## Distribuição

`scripts/package-exercise.py` usa uma allowlist estrutural: somente o conteúdo de `exercise/` entra no ZIP. Diretórios `bin`, `obj`, `node_modules` e cobertura são excluídos. Cada pacote recebe um arquivo SHA-256 adjacente.

## Regeneração

Os arquivos foram produzidos por geradores mantidos em `tools/`:

- `generate_dotnet_exercises.py` — exercícios 01–06;
- `generate_frontend_exercises.py` — exercícios 07–11;
- `generate_dotnet_exercises_12_18.py` — exercícios 12–18;
- `generate_dotnet_exercises_19_27.py` — exercícios 19–27;
- `generate_special_exercises.py` — exercícios 28–30.
- `extended_definitions.py` — matriz comportamental dos exercícios 31–100;
- `extend_catalog_100.py` — catálogo e documentação da expansão;
- `generate_extended_backend.py` — exercícios 31–65;
- `generate_extended_frontend.py` — exercícios 66–100.
- `production_scale_definitions.py` — matriz comportamental 101–130;
- `extend_catalog_130.py` — catálogo, plano e metadados do perfil de produção;
- `generate_production_scale_exercises.py` — bases completas 101–130.

Os geradores da expansão reutilizam lockfiles canônicos de React e Angular com versões fixas. Ao atualizar dependências, regenere conscientemente os lockfiles de todos os exercícios frontend.
