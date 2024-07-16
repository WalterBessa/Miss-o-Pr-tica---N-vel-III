set_inicial = {11, 12, 13, 14}
print(set_inicial)

set_inicial.add(15)
print(set_inicial)

set_inicial.update({1, 2, 3, 4, 5})
print(set_inicial)

set_inicial.discard(13)
print(set_inicial)

novo_set = {20, 21, 23, 1, 2}
print(novo_set)

uniao_sets = set_inicial.union(novo_set)
print(uniao_sets)

intersecao_sets = set_inicial.intersection(novo_set)
print(intersecao_sets)

diferenca_sets = set_inicial.difference(novo_set)
print(diferenca_sets)

diferenca_simetrica_sets = set_inicial.symmetric_difference(novo_set)
print(diferenca_simetrica_sets)
