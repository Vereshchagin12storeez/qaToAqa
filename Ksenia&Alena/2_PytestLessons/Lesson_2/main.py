import requests
import json
from pprint import pprint

# url = "https://staging.12stz.tech/catalog/new/womencollection"
# body = {"key": "value"}
# body_json = json.dumps(body)
#
#
# response = requests.request(method="POST",
#                             url=url,
#                             data=body)
# print(response.text)


url = "https://api.nbrb.by/exrates/currencies"

payload = {}
headers = {}

response0 = requests.request(method="GET",
                             url=url,
                             headers=headers,
                             data=payload)

response1 = requests.get(url=url,
                         headers=headers,
                         data=payload)

pprint(response0.text)
# pprint(response1.text)
