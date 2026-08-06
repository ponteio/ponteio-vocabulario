# ponteio-vocabulario

Vocabulário controlado multilíngue do PONTEIO, modelado em SKOS com desvio
deliberado (R56): para termos culturalmente irredutíveis, `skos:prefLabel`
existe apenas na língua de origem. Outras línguas recebem glosas
(`altLabel`, `scopeNote`, `definition`).

## Princípios

- Nenhum termo exige forma canônica em inglês (FF-04)
- O termo é canônico na própria língua (R20)
- Glosas divergentes coexistem sem exigir definição única
- Validação incorporada: termo que não pode ser tocado é termo ruim (R46)

## Uso

Este repositório é o único acoplamento permitido entre o PONTEIO e o
app do Casa 13 (R45, D14). Um arquivo versionado, sob controle de versão.
Sem API, sem dependência de execução.

## Formato

Arquivos Turtle (`.ttl`) em `vocabulario/`.

## Licença

CC-BY-SA 4.0
