from send_email import send_email
import requests
import json

api=None #to_fill
url = f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={api}"

request = requests.get(url)

msg =''
res=json.loads(request.text)
for i in res['articles']:
    msg+=f"{i['title']} \n {i['url']} \n\n"

send_email(message=msg, to=None, subject="TechNews")