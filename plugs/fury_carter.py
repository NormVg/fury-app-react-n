import requests
import json
from plugs.config import carter_key
# from config import carter_key
def ask_fury(com,user):
    response = requests.post("https://api.carterlabs.ai/chat", headers={
        "Content-Type": "application/json"
    }, data=json.dumps({
        "text": f"{user} : {command}",
        "key": carter_key,
        "user_id": "Vishnu" 
    }))
    return response.json()['output']['text'],""

# print(ask_fury("tell space news fury",""))
