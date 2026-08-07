#!/usr/bin/env python3
"""FF-04 — nenhum conceito tem forma canônica em inglês, e todo prefLabel tem língua.

R19/R20: não deve existir língua central por padrão. Num vocabulário SKOS isso é
verificável: se um conceito tem exatamente um prefLabel e ele é `en`, o inglês
virou o padrão de fato — mesmo que ninguém tenha decidido isso.
"""
import pathlib, sys

try:
    from rdflib import Graph
    from rdflib.namespace import SKOS
except ImportError:
    sys.exit("falta rdflib:  mise run setup")

g = Graph()
arquivos = sorted(pathlib.Path("vocabulario").rglob("*.ttl"))
if not arquivos:
    print("  ⚠ nenhum .ttl em vocabulario/ — verificação vazia")
    sys.exit(0)
for a in arquivos:
    g.parse(a)

faltas = []
conceitos = list(g.subjects(None, SKOS.Concept))
for c in conceitos:
    rotulos = list(g.objects(c, SKOS.prefLabel))
    if not rotulos:
        faltas.append(f"{c}: sem prefLabel")
        continue
    linguas = {r.language for r in rotulos}
    if None in linguas:
        faltas.append(f"{c}: prefLabel sem tag de língua (BCP 47 obrigatório)")
    if linguas == {"en"}:
        faltas.append(f"{c}: único prefLabel é 'en' — FF-04 proíbe forma canônica em inglês")
    if len(rotulos) != len(linguas):
        faltas.append(f"{c}: mais de um prefLabel na mesma língua (SKOS proíbe)")

if faltas:
    print("FF-04 / SKOS violados:", file=sys.stderr)
    for f in faltas:
        print(f"  ✗ {f}", file=sys.stderr)
    sys.exit(1)
print(f"  ✓ {len(conceitos)} conceitos, todos com prefLabel etiquetado e sem canônico em inglês")
