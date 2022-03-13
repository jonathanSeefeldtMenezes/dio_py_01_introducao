
class Error(Exception):
    pass


class InputError(Error):
    def __init__(self, message):
        self.message = message


while True:
    try:
        nota = int(input('Informe uma nota de 0 a 10: '))

        if nota > 10:
            raise InputError('A nota não pode ser maior que 10.')
        elif nota < 0:
            raise InputError('A nota não pode ser menor que 0')

        break
    except ValueError:
        print('Valor inválido. Deve-se informar apenas números de 0 a 10.')
    except InputError as ex:
        print(ex)
