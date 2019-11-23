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
first_page = re.get("https://api.artsy.net/api/artists", headers={'X-Xapp-Token': token})
first_page_text = json.loads(first_page.text)
artists = first_page_text['_embedded']['artists']
next_page = first_page_text['_links']['next']['href']
artists_str= json.dumps(artists)
count = 0
with open(f"C:/Users/harsh/OneDrive/Desktop/CodeBase/Artmosphere/Data/artists_{}.txt".format(count),'w') as f:
    f.write(artists_str)
while ((next_page is not None) and (count <10)):
    new_page = re.get(next_page, headers={'X-Xapp-Token': token})
    new_page_text = json.loads(new_page.text)
    count = count+1
    print(count)
    next_page = new_page_text['_links']['next']['href']
    artists = new_page_text['_embedded']['artists']
    artists_str = json.dumps(artists)
    with open(f"C:/Users/harsh/OneDrive/Desktop/CodeBase/Artmosphere/Data/artists_{}.txt".format(count),'w') as f:
        f.write(json.dumps(artists_str))