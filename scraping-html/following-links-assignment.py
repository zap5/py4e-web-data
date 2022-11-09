from urllib.request import urlopen 
from bs4 import BeautifulSoup
import ssl 
import re

# Ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False 
ctx.verify_mode = ssl.CERT_NONE 

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: ')) - 1 # Account for the fact that assignment says names aren't zero indexed
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup.findAll('a')

newURL = ''
newHTML = ''
newSoup = ''
newTags = tags
i = 0

print('Retrieving ' + url)

while i < count:
    newURL = newTags[position].attrs['href']
    print('Retrieving ' + newURL)
    newHTML = urlopen(newURL, context=ctx).read()
    newSoup = BeautifulSoup(newHTML, 'html.parser')
    newTags = newSoup.findAll('a')
    i += 1

