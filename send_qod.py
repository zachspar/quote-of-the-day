#!/usr/bin/env python3
import os
import random
import requests
from config import (TWILIO_AUTH_TOKEN, TWILIO_ACCT_SID, OUTGOING_LIST,
                    SENDING_NUMBER, QUOTES_API_KEY)
from twilio.rest import Client


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
    res = requests.get("https://quotes.rest/qod",
                       headers=headers,
                       params=params)
    print(f"Response Code :: {res.status_code}")

    if res.status_code == 200:
        res_dict = res.json()
        quote_obj = res_dict['contents']['quotes'][0]
        print(f"QUOTE: {quote_obj['quote']}")
        print(f"AUTHOR: {quote_obj['author']}")
        fmt_quote = f"{quote_obj['quote']}\n\n\t- {quote_obj['author']}"
        print("Sending formatted quote message...")

        for number in OUTGOING_LIST:
            print(f"Sending QOD to {number}")
            message = client.messages.create(body=fmt_quote,
                                             from_=SENDING_NUMBER,
                                             to=str(number))
            print(message.sid)
    else:
        print("Could not properly execute request...")


if __name__ == '__main__':
    main()

