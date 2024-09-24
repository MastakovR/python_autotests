
import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2' 
TOKEN = '' #your token here
HEADER = {'Content-type':'application/json', 'trainer_token':TOKEN} 
TRAINER_ID = '' #your Trainer ID


def test_status_code(): 
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID} )
    assert response.status_code == 200, 'Unexpected status code'

def test_part_of_response(): 
     response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID} )
     assert response_get.json()['data'][0]["name"] == 'thwackey', 'another name'


@pytest.mark.parametrize('key, value', [('name', 'thwackey'), ('trainer_id', TRAINER_ID), ('id', '73894')]) 
def test_parametrize(key, value): 
     response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID}) 
     assert response_parametrize.json()["data"][0][key] == value, 'Unexpected id code'
