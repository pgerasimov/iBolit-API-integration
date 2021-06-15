import json

import requests

from api_auth import get_token
from config import client_key as key
from config import clinic_secret as secret

token = str('Bearer ' + get_token(secret, key))

headers = {
    'Content-Type': 'application/json',
    'Authorization': token
}

values = {
    'full_name': 'Тестовый Врач ИзАпи',
    'phone': '+79968651147',
    'birthday': '1986-01-01',
    'gender': 'male'
}

values = json.dumps(values, indent=4)

request = requests.post('https://api.ibolit.pro/public/v1/patients', data=values, headers=headers)

print(request.status_code)
print(request.json())
