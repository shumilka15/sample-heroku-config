from time import sleep

import requests
from handler import handle_message

while True:
    res = requests.get("https://api.telegram.org/bot502815445:AAEuKSBpwXge3YjTRS8owspX6FvYQZs5lU/getUpdates")
    d = res.json()
    for elem in d["result"]:
        text = elem["message"]
        print(elem["from"]["username"], text)
        ans = handle_message(text)
        chat_id = elem["message"]["chat"]["id"]
        requests.post("https://api.telegram.org/bot502815445:AAEuKSBpwXge3YjTRS8owspX6FvYQZs5lU/sendMessage", params={"chat_id": chat_id, "text": text} )
