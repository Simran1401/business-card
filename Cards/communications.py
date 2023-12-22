import requests
import base64
import json
import environ
import hashlib


def CreatePhonePyChecksome(payload):
    payload_json = json.dumps(payload)

    # Encode the JSON payload in Base64
    encoded_payload = base64.b64encode(payload_json.encode('utf-8')).decode('utf-8')

    # "/pg/v1/pay"
    path = "/pg/v1/pay"

    # Salt key
    salt_key = "b843d817-f5e8-4d36-8917-1c6e045a1af9"

    #live key
    # salt_key = "b011949f-2bf4-433d-91f3-220f1873cbed"

    # Salt index
    salt_index = "1"

    # Concatenate the string
    concatenated_string = encoded_payload + path + salt_key

    # Create a SHA256 hash object
    hash_object = hashlib.sha256()

    # Convert the concatenated string to bytes
    concatenated_bytes = concatenated_string.encode('utf-8')

    # Update the hash object with the concatenated bytes
    hash_object.update(concatenated_bytes)

    # Compute the final hash by appending salt index
    final_hash = hash_object.hexdigest() + "###" + salt_index

    #----------------------------- testing ----------------------------
    url = "https://api-preprod.phonepe.com/apis/merchant-simulator/pg/v1/pay"

    #live url
    # url = "https://api.phonepe.com/apis/hermes/pg/v1/pay"

    payload = {"request": encoded_payload}

    headers = {
        "accept": "application/json",
        "Content-Type":"application/json",
        "X-VERIFY": final_hash
    }

    response = requests.post(url, json=payload, headers=headers)
    response_data = response.json()

    # Extract the URL from the JSON data
    url = response_data['data']['instrumentResponse']['redirectInfo']['url']
    return url
