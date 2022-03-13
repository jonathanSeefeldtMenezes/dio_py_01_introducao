# Request / Response

import requests


def obter_cep(cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

    if int(response.status_code) == 200:
        print(response.json())
    else:
        print('Não foi possível obter o cep informado.')


def obter_pokemon(pokemon):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')

    if int(response.status_code) == 200:
        print(response.json()['sprites']['front_shiny'])
    else:
        print('Não foi possível obter o pokemon informado.')


obter_cep('78735587')
obter_cep('96170000')

obter_pokemon('bulbasaur')
obter_pokemon('charizard')