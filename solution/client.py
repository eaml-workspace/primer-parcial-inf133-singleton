import requests

url= "http://localhost:8000/guess"

new_post={
    "player":"Julian"
}
response=requests.request(method="POST", url=url, json=new_post)
print(response.text)