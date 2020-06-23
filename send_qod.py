#!/usr/bin/env python3
import os
import requests
from config import TWILIO_AUTH_TOKEN, TWILIO_ACCT_SID, OUTGOING_LIST, SENDING_NUMBER
from twilio.rest import Client


def main():
    account_sid = TWILIO_ACCT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    res = requests.get("https://quotes.rest/qod?language=en")
    print(f"Response Code: {res.status_code}")
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


if __name__ == '__main__':
    main()

