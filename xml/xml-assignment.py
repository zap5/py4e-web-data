from urllib.request import urlopen 
from bs4 import BeautifulSoup
import ssl 
import re
import xml.etree.ElementTree as ET


# Ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False 
ctx.verify_mode = ssl.CERT_NONE 

url = input('Enter URL: ')
data = urlopen(url, context=ctx).read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')
sum = 0

for count in counts:
    sum += int(count.text)

print(sum)