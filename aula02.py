
#Concatenação de string com valores

a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

sValores = ('\nValores:\n'
            f'Valor A: {a}\n'
            f'Valor B: {b}\n')

sResultadoComF = ('\nPrimeira forma de concatenar com f na frente da string:\n'
                  f'Soma.........: {soma}\n'
                  f'Subtração....: {subtracao}\n'
                  f'Multiplicação: {multiplicacao}\n'
                  f'Divisão......: {divisao}\n'
                  f'Resto........: {resto}\n')

sResultadoComFormat = ('\nOutra forma de concatenar, utilizando o .format:\n'
                        'Soma.........: {soma}\n'
                        'Subtração....: {sub}\n'
                        'Multiplicação: {mult}\n'
                        'Divisão......: {div}\n'
                        'Resto........: {resto}\n'
                        .format(soma=soma,
                                sub=subtracao,
                                mult=multiplicacao,
                                div=divisao,
                                resto=resto)
                        )

print(f'{sValores}'
      f'{sResultadoComF}'
      f'{sResultadoComFormat}')