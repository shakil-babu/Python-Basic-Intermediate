import requests
res = requests.get("https://shakilbabu.vercel.app/")

print(res.ok)
print(res.status_code)
print(res.reason)
