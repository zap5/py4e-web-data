import urllib.request
import json 

url = input('Enter URL: ')
print('Retrieving ' + url)

handle = urllib.request.urlopen(url)
data = handle.read().decode()
print('Retrieved ', len(data), ' characters')

js = json.loads(data)

comments = js['comments']
sum = 0
count = len(comments)

for comment in comments:
    sum += comment['count']

print('Count: ' + str(count))
print('Sum: ' + str(sum))