import time

import jwt


def get_token(secret, key):
    clinic_secret = secret
    client_key = key

    current_time = time.time()

    payload = {
        'sub': client_key,
        'iat': current_time,
        'exp': current_time + 300,
    }

    encoded_jwt = jwt.encode(payload, clinic_secret, algorithm="HS256")

    return encoded_jwt
