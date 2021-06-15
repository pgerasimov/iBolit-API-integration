import requests

from api_auth import get_token
from config import client_key as key
from config import clinic_secret as secret

token = str('Bearer ' + get_token(secret, key))

headers = {
    'Content-Type': 'application/json',
    'Authorization': token
}

request = requests.get('https://api.ibolit.pro/public/v1/doctors', headers=headers)

print('Врач')
print(request.json())
