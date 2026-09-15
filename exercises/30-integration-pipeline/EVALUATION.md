# Avaliação: Pipeline de integração

| ID | Nível | Peso | Condição |
| --- | --- | ---: | --- |
| C01 | mínimo | 3 | falhas não são mascaradas |
| C02 | mínimo | 2 | backend e frontend têm build/test |
| C03 | mínimo | 2 | artefato depende de sucesso |
| C04 | intermediário | 2 | cache referencia os dois lockfiles |
| C05 | desejado | 1 | workflow não imprime secrets |
