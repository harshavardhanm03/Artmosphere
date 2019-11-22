import urllib
import pandas
import json
import requests as re
import pprint

client_id = '587fd503e28a69c380d7'
client_secret = '8da3ea7c788efdad602485c48d1f4e92'
posts = re.post("https://api.artsy.net/api/tokens/xapp_token",
                data={"client_id": client_id, "client_secret": client_secret})
j = json.loads(posts.text)
token = j['token']
r = re.get("https://api.artsy.net/api/artists", headers={'X-Xapp-Token': token})
# r = re.get("https://api.artsy.net/api/artists/5723c839139b2113a8000619", headers={'X-Xapp-Token': token})
artists = json.loads(r.text)
embedded_artists = artists['_embedded']['artists']
#print(embedded_artists)
next_page = embedded_artists[0]['_links']['self']['href']
print(next_page)
print(type(next_page))
count = 0
while (next_page is not None) or (count < 1):
    r = re.get(next_page, headers={'X-Xapp-Token': token})
    artists = json.loads(r.text)
    print(artists)
    count = count+1
# print(artists['_embedded']['artists'])
# print(artists['__links'])
# [0]['_links']['self']['href'])
# print(artists['_links']['image']['href'])
