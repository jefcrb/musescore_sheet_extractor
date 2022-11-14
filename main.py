import requests
import wget
import json


id = ""
h = ""


id = input("Musescore sheet id: ")
h = input("Authorization header: ")

h = {'Authorization': h}


def get_sheets():
    i = 0

    while True:
        r = requests.get(f'https://musescore.com/api/jmuse?id={id}&index={i}&type=img&v2=1', headers=h)
        print(r.status_code)

        url = json.loads(r.text)["info"]["url"]

        try:
            wget.download(url)
        except:
            break

        i+=1

get_sheets()
print("Done")