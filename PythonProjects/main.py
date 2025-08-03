import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7de2f8b9ef38dcbb00067eb4307f35d6'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "Bur",
    "photo_id": 200
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.json()) 

POKEMON_ID = response_create.json()['id']

body_change = {
    "pokemon_id": POKEMON_ID,
    "name": "Beer",
    "photo_id": 235
} 

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.json()) 

body_add_pokeball = {
    "pokemon_id": POKEMON_ID
}

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.json())   
