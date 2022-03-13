
#Instruções IF/ELSE

valorA = int(input('Digite o primeiro valor: '))
valorB = int(input('Digite o segundo valor.: '))
valorC = int(input('Digite o terceiro valor: '))

if valorA > valorB and valorA > valorC:
    print(f'O maior número é {valorA}.')
elif valorB > valorA and valorB > valorC:
    print(f'O maior número é {valorB}.')
else:
    print(f'O maior número é {valorC}.')
