import requests
r = requests.get("https://www.google.com")
print(r.status_code)
