#!/usr/bin/env python3
import os
import requests
from config import TWILIO_AUTH_TOKEN, TWILIO_ACCT_SID
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
        fmt_quote = f"{quote_obj['quote']}\n\n\t-{quote_obj['author']}"
        print("Sending formatted quote message...")

        message = client.messages.create(body=fmt_quote,
                                         from_='+12029466054',
                                         to='+19144868258')

        print(message.sid)


if __name__ == '__main__':
    main()

