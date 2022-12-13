import urllib.request, urllib.parse, urllib.error
import json
import ssl

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

api_key = 42

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break 

    params = dict()
    params['address'] = address
    params['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(params)

    print('Retrieving ', url)
    handle = urllib.request.urlopen(url, context = ctx)
    data = handle.read().decode()
    print('Retrieved ', len(data), ' characters')

    js = json.loads(data)
    print('Place id: ', js['results'][0]['place_id'])
