from urllib.request import urlopen 
from bs4 import BeautifulSoup
import ssl 
import re

# Ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False 
ctx.verify_mode = ssl.CERT_NONE 

url = input('Enter URL: ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
sum = 0

for ele in tags:
    values = re.findall('[0-9]+', str(ele))
    for num in values:
        sum += int(num)

print(sum)