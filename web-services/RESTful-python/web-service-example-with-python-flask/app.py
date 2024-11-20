import requests

response = requests.get("http://127.0.0.1:5000/")
if response.status_code == 200:
    data = response.json()
    print(data)
