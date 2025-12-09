import requests
from time import sleep

r = requests.get('http://127.0.0.1:8000/')
 
# if type(r.json()) != dict:
#     print("esperando")
#     sleep(5)

print(r.text)