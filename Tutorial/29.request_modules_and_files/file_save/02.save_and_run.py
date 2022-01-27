import requests
import os
import webbrowser as web

url = "http://dimikcomputing.com"
res = requests.get(url)

with open('dimik.html', "w", encoding=res.encoding) as f:
    f.write(res.text)

file_path = os.path.realpath("dimik.html")
print(file_path)
web.open("file://" + file_path)
