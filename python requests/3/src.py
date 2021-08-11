import requests

data = {
    "name": "ahmed",
    "age": 17
}
files = {'files': open("myfile.txt", "rb")}
res = requests.post("https://httpbin.org/post", files=files)
print(res.text)
