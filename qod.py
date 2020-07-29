#!/usr/bin/env python3
import random
import requests
from config import QUOTES_API_KEY


def main():
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


if __name__ == '__main__':
    main()

