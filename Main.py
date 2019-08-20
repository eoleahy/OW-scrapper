import requests
import json


def main():
    account=""
    URL = "https://ow-api.com/v1/stats/pc/eu/"+account+"/profile"

    r=requests.get(url=URL,params="")
    data=r.json()

    with open("data.json","w")as f:
        f.write(json.dumps(data,indent=4,sort_keys=True))

    compStats=data['rating']
    print(account,compStats)

if __name__ == '__main__':
    main()
