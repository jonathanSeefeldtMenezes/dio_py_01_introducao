
def contador_letras(lista_palavras):
    contador = []

    for i in lista_palavras:
        quantidade = len(i)
        contador.append(quantidade)
    return contador


if __name__ == '__main__':
    lista = ['cachorro', 'gato', 'elefante', 'bufalo', 'galinha', 'leopardo']
    print(contador_letras(lista))

    contador_letras_lambda = lambda listagem: [len(i) for i in listagem]
    print(contador_letras_lambda(lista))