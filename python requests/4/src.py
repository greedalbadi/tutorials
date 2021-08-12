import requests

proxies = {
  "http": "http://13.84.170.134:8080",
  "https": "http://13.84.170.134:8080"
}
res = requests.get('https://httpbin.org/ip', proxies=proxies)
print(res.text)
