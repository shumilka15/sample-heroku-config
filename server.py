import requests 
from handler import handle_message 
lui = 0 
while True: 
    res = requests.get("https://api.telegram.org/bot502815445:AAGOuCHPn4pEgdVQtxnuoTMCeWpw6hn27lo/getUpdates", params = {"offset": lui}) 
    d = res.json() 

    for elem in d["result"]: 
        text = elem["message"]["text"] 
        ans = handle_message(text) 
        lui = elem["update_id"]+1 
        chat_id = elem["message"]["chat"]["id"] 

        requests.post("https://api.telegram.org/bot502815445:AAGOuCHPn4pEgdVQtxnuoTMCeWpw6hn27lo/sendMessage", params={ "chat_id": chat_id, "text": ans} )
