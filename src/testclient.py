import socket

name = socket.gethostname()
print(name)
socket.gethostbyname(name)
client = socket.socket()
client.connect(('mynascube.ddns.net', 1880))
data = '{"user": {"user_id": "...","profile": {"given_name": "John","family_name": "Doe","display_name": "John Doe"},"access_token": "..."},"device": {"location": {"coordinates": {"latitude": 123.456,"longitude": -123.456},"formatted_address": "1234 Random Road, Anytown, CA 12345, United States","city": "Anytown","zip_code": "12345"}},"conversation": {"conversation_id": "...","type": "ACTIVE","conversation_token": "..."  },"inputs": [{"intent": "assistant.intent.action.MAIN","raw_inputs": [{"query": "..."}],"arguments": [{"name": "destination","raw_text": "SFO","location_value": {"latlng": {"latitude": 37.620565,"longitude": -122.384964},"formatted_address": "1000 Broadway, San Francisco, CA 95133"}}]}]}'
client.send(data.encode())
client.close()


