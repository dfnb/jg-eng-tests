# Avaliação: Formulário por esquema

- **ID:** 10
- **Nível:** intermediate
- **Duração:** 150 minutos
- **Tecnologias:** angular, typescript

## Intenção e estado inicial

Avaliar feature dinâmica, tipos e validação orientada por dados.

**Causa/omissão:** a implementação cria apenas campos text e ignora regras.

**Armadilha:** hardcode dos campos do exemplo.

## Critérios

| ID | Nível | Peso | Condição | Teste |
| --- | --- | ---: | --- | --- |
| C01 | mínimo | 3 | três tipos suportados são montados | `C01` |
| C02 | mínimo | 2 | required controla validade | `C02` |
| C03 | mínimo | 2 | min/max numérico é aplicado | `C03` |
| C04 | intermediário | 2 | tipo desconhecido gera erro seguro | `C04` |
| C05 | desejado | 1 | componente usa ReactiveFormsModule | `C05` |

Soluções estruturalmente diferentes são aceitas se preservarem o contrato observável e a acessibilidade. A referência é um exemplo, não um molde obrigatório.
