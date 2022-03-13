
# Escrever/Ler arquivo

def escrever_arquivo(texto):
    arquivo = open('teste_aula_09.txt', 'w', encoding='UTF-8')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('teste_aula_09.txt', 'a', encoding='UTF-8')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo():
    arquivo = open('teste_aula_09.txt', 'r', encoding='UTF-8')
    texto = arquivo.read()
    print(texto)
    arquivo.close()


if __name__ == '__main__':
    texto_inicial = 'Hoje é um novo dia, mais um aprendizado.\n'
    texto_final = 'Python é uma excelente linguagem, pretendo aprender' \
                  ' e utilizar muito daqui pra frente.\n'
    escrever_arquivo(texto_inicial)
    atualizar_arquivo(texto_final)
    ler_arquivo()
