# Conjuntos e SubConjuntos

conjunto_1 = {1, 2, 3, 4, 5}
conjunto_2 = {5, 6, 7, 8, 9}
conjunto_uniao = conjunto_1.union(conjunto_2)
conjunto_interseccao = conjunto_1.intersection(conjunto_2)
conjunto_diff_1_2 = conjunto_1.difference(conjunto_2)
conjunto_diff_2_1 = conjunto_2.difference(conjunto_1)
conjunto_diff_simetrica = conjunto_1.symmetric_difference(conjunto_2)

print(f'Conjunto 1: {conjunto_1}')
print(f'Conjunto 2: {conjunto_2}')
print(f'Conjunto União: {conjunto_uniao}')
print(f'Conjunto intersecção: {conjunto_interseccao}')
print(f'Conjunto diferença 1 e 2: {conjunto_diff_1_2}')
print(f'Conjunto diferença 2 e 1: {conjunto_diff_2_1}')
print(f'Conjunto diferença simétrica: {conjunto_diff_simetrica}')

