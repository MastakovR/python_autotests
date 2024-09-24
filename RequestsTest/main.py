import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '' # токен (нужно ввести свой)
HEADER = {'Content-type':'application/json', 'trainer_token':TOKEN} #хедеры


body_registration = {
    "trainer_token": TOKEN, 
    "email": "email@yandex.ru",
    "password":"Password1" 
}

body_confirmation = {
    "trainer_token": TOKEN 
}

body_create = {
    "name": "generate", #имя покемона
    "photo_id":"-1"     #аватар покемона
}


'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.status_code)

message = response_create.json()['message']
print(message)
