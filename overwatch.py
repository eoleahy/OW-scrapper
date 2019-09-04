import requests
import json

class Overwatch():
    """A class for the Overwatch api
    each intance is an account which has its
    own platform region and account.
    For now the only info you can get is rating """

    platform=""
    region=""
    account=""

    def __init__(self,platform,region,account):
        self.platform=platform
        self.region=region
        self.account=account


    def get_profile(self):

        URL = "https://ow-api.com/v1/stats/%s/%s/%s/profile" % (self.platform,self.region,self.account)
        r=requests.get(url=URL,params="")
        data=r.json()
        return data


    def get_rating(self):

        data = self.get_profile()
        comp_stats=data['rating']
        #print(self.account,comp_stats)

        return comp_stats


    def profile_to_json(self):

        data = self.get_profile()
        with open("data.json","w")as f:
            f.write(json.dumps(data,indent=4,sort_keys=True))
