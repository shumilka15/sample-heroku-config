from time import sleep

import requests
from handler import handle_message

while True:
    res = requests.get("https://api.telegram.org/bot502815445:AAGOuCHPn4pEgdVQtxnuoTMCeWpw6hn27lo/getUpdates")
    d = res.json()
    for elem in d["result"]:
        text = elem["message"]
        print(elem)
        #print(elem["message"]["from"]["username"], text)
        ans = handle_message(text)
        chat_id = elem["message"]["chat"]["id"]
        requests.post("https://api.telegram.org/bot502815445:AAGOuCHPn4pEgdVQtxnuoTMCeWpw6hn27lo/sendMessage", params={"chat_id": chat_id, "text": text} )
