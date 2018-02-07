import requests
from handler import handle_message

while True:
    res = requests.get()
    d = res.json()

    for elem in d["result"]:
        text = elem["messages"]["text"]
        ans = handle_message(text)
        chat_id = elem["messages"]["chat"]["id"]

        requests.post("URL", params={"chat_id": chat_id, "text": text}) (ред.)
