# We need 2 libraries
# So we import and install needed libraries

import schedule
import time
from number import mobile_number
import requests


def send_message():
    resp = requests.post('https://textbelt.com/text', {
    'phone': mobile_number,
    'message': 'Hello, good morning',
    'key': 'textbelt',
    })
    print(resp.json())


schedule.every().day.at('06:00').do(send_message())
