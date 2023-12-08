import requests
from send_email import send_email

topic = 'tesla'
url = f'https://newsapi.org/v2/everything?q={topic}&from=\
    2023-11-08&sortBy=publishedAt&apiKey=7783b9e8a33548649207c58f0b0c9ce4&language=en'
api_key = '7783b9e8a33548649207c58f0b0c9ce4'

request = requests.get(url)
content = request.json()

body = ''
for article in content['articles'][:20]:
    title = article.get('title', '')
    description = article.get('description', '')
    if title and description:
        url1 = article['url']
        body += f"{title}\n{description}\n{url1}\n\n"
body = body.encode("utf-8")
send_email(messege=body)