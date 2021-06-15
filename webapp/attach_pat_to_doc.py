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

body = {
    "patient_id": 540124,
    "doctor_id": 224285
}

body = json.dumps(body, indent=4)

request = requests.post('https://api.ibolit.pro/public/v1/patients/attach', data=body, headers=headers)

print(request.status_code)
print(request.json())
