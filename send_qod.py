#!/usr/bin/env python3
import os
import random
import requests
from requests.exceptions import ConnectionError
from config import (TWILIO_AUTH_TOKEN, TWILIO_ACCT_SID, OUTGOING_LIST,
                    SENDING_NUMBER, QUOTES_API_KEY)
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException


def main():
    client = Client(TWILIO_ACCT_SID, TWILIO_AUTH_TOKEN)

    headers = {
        "X-TheySaidSo-Api-Secret": QUOTES_API_KEY,
        "Accept": "application/json",
    }

    categories = ['love', 'management', 'inspire', 'sports', 'life', 'funny',
                  'students', 'art',]

    params = {
        'category': random.choice(categories),
        'language': 'en',
    }

    print(f"Category Today :: {params['category']}");
    res = None
    count = 0
    while count < 5 and not res:
        count += 1
        try:
            res = requests.get("https://quotes.rest/qod",
                               headers=headers,
                               params=params)
            print(f"Response Code :: {res.status_code}")
        except ConnectionError as e:
            print(f"API Connection error...{e}")

    if res and res.status_code == 200:
        res_dict = res.json()
        quote_obj = res_dict['contents']['quotes'][0]
        print(f"QUOTE: {quote_obj['quote']}")
        print(f"AUTHOR: {quote_obj['author']}")
        fmt_quote = f"{quote_obj['quote']}\n\n\t- {quote_obj['author']}"
        print("Sending formatted quote message...")

        for number in OUTGOING_LIST:
            print(f"Sending QOD to {number}")
            try:
                message = client.messages.create(body=fmt_quote,
                                                 from_=SENDING_NUMBER,
                                                 to=str(number))
                print(message.sid)
            except TwilioRestException as e:
                print(e)
                print(f"ERROR: Could not send quote to phone number {number}")
    else:
        print("ERROR: Could not properly execute quote request...")


if __name__ == '__main__':
    main()

