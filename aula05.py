# Listas
print('Listas (São mutáveis)')

listaAnimal = ['gato', 'cachorro', 'arara', 'cavalo', 'elefante', 'passarinho', 'cobra']

listaAnimal.sort()
print(f'\nLista ordenada [A=>Z]: f{listaAnimal}')

listaAnimal.reverse()
print(f'\nLista ordenada [Z=>A]: f{listaAnimal}')

print('\nLista de animais:')
for animal in listaAnimal:
    print(f'{listaAnimal.index(animal)} - {animal}')

print(f'\nPrimeiro animal por ordem alfabética: f{min(listaAnimal)}')

print(f'\nÚltimo animal por ordem alfabética: f{max(listaAnimal)}')

print('\nAdiciona o animal lobo:')
listaAnimal.append('lobo')
print(listaAnimal)

print('\nRemove o último animal inserido, que é o lobo:')
listaAnimal.pop()
print(listaAnimal)

print('\nRemove o animal cavalo:')
listaAnimal.remove('cavalo')
print(listaAnimal)

print('\nTuplas (Imutáveis)')

tupla_animais = tuple(listaAnimal)
print(tupla_animais)
