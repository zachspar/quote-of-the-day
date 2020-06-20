import requests

res = requests.get("https://quotes.rest/qod?language=en")
if res.status_code == 200:
    res_dict = res.json()
    quote_obj = res_dict['contents']['quotes'][0]
    print(f"QUOTE: {quote_obj['quote']}")
    print(f"AUTHOR: {quote_obj['author']}")

