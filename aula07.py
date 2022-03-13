# Classes e funções

class Calculadora_init_valores:

    def __init__(self, num_1, num_2):
        self.numero_1 = num_1
        self.numero_2 = num_2
        print(f'Calculadora inicializada com os valores: {self.numero_1}, {self.numero_2}')

    def somar(self):
        return self.numero_1 + self.numero_2

    def subtrair(self):
        return self.numero_1 - self.numero_2

    def multiplicar(self):
        return self.numero_1 * self.numero_2

    def dividir(self):
        return self.numero_1 / self.numero_2


if __name__ == '__main__':
    calc = Calculadora_init_valores(10, 2)
    print(f'Soma.........: {calc.somar()}')
    print(f'Subtração....: {calc.subtrair()}')
    print(f'Multiplicação: {calc.multiplicar()}')
    print(f'Divisão......: {calc.dividir()}')
    print('#--------------------------------------#')

class Calculadora_sem_init_valores:

    def __init__(self):
        pass

    def somar(self, numero_1, numero_2):
        return numero_1 + numero_2

    def subtrair(self, numero_1, numero_2):
        return numero_1 - numero_2

    def multiplicar(self, numero_1, numero_2):
        return numero_1 * numero_2

    def dividir(self, numero_1, numero_2):
        return numero_1 / numero_2

if __name__ == '__main__':
    calc = Calculadora_sem_init_valores()
    print(f'Soma.........: {calc.somar(15,10)}')
    print(f'Subtração....: {calc.subtrair(200,150)}')
    print(f'Multiplicação: {calc.multiplicar(10,53)}')
    print(f'Divisão......: {calc.dividir(8798,85)}')
    print('#--------------------------------------#')

class Televisao:

    def __init__(self, com_mensagem):
        self.ligada = False

        if com_mensagem:
            print('A televisão está desligada.')

    def power(self, com_mensagem):
        self.ligada = not self.ligada

        if com_mensagem:
            if self.ligada:
                print('A televisão está ligada.')
            else:
                print('A televisão está desligada.')


if __name__ == '__main__':
    tv = Televisao(com_mensagem=True)
    tv.power(com_mensagem=True)
    tv.power(com_mensagem=True)
