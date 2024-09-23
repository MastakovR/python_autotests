
import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2' 
TOKEN = '0ae8d757368e87a30bac66db9dc2e8d1' 
HEADER = {'Content-type':'application/json', 'trainer_token':TOKEN} 
TRAINER_ID = '6722' 


def test_status_code(): 
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID} )
    assert response.status_code == 200

def test_part_of_response(): 
     response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID} )
     assert response_get.json()['data'][0]["name"] == 'thwackey'


@pytest.mark.parametrize('key, value', [('name', 'thwackey'), ('trainer_id', TRAINER_ID), ('id', '73894')]) 
def test_parametrize(key, value): 
     response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID}) 
     assert response_parametrize.json()["data"][0][key] == value