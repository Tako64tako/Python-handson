import requests

url_index = 'http://localhost:8888/'
url_get = 'http://localhost:8888/api'
url_post = 'http://localhost:8888/api/articles'

index = requests.get(url_index)
get = requests.get(url_get)
post = requests.post(url_post)

count = 0

if index.status_code == 200:
    count += 1
if get.status_code == 200:
    count += 1
if post.status_code == 200:
    count += 1

if count == 3:
    print('Success!')
else:
    print('Failed...')