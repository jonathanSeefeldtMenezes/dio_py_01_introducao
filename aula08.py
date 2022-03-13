# Importação de módulos

from aula07 import Televisao

tv = Televisao(com_mensagem=True)

i = 1
while i < 3:
    tv.power(com_mensagem=True)
    i += 1
