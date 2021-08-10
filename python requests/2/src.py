import requests

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}

url = "https://www.instagram.com/greedalbadi/?__a=1"

r = requests.get(url, headers=header)
name = r.json()["graphql"]["user"]["full_name"]
id = r.json()["graphql"]["user"]["id"]
print(name)
print(id)
