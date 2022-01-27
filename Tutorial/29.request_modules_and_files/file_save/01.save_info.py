import requests

res = requests.get("https://shakilbabu.vercel.app/")
with open("shakilbabu.html", 'w') as f:
    f.write(res.text)
