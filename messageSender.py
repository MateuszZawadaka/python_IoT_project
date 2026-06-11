import requests
from requests.auth import HTTPBasicAuth
import json

class MessageSender:
    def __init__(self, api_url, username, password, phone_number):
        self.api_url = api_url
        self.auth = HTTPBasicAuth(username, password)
        self.phone_number = phone_number

    def send_message(self, device_id, message, phone_number=None):
        if phone_number is None:
            phone_number = self.phone_number
        payload = {
            "message": message,
            "PhoneNumbers": [phone_number],
            "recipient_id": device_id,
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.api_url, auth=self.auth, headers=headers, json=payload)
        
        if response.status_code in [200, 202]:
            print("Message accepted successfully!")
            print(response.json())
        else:
            print(f"Failed to send message. Status code: {response.status_code}")
            print(response.text)