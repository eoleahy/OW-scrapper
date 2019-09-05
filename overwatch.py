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

        tank_rating=0
        damage_rating=0
        support_rating=0

        average_rating = data['rating']
        comp_stats=data['ratings']

        num_placements = len(comp_stats)#Number of roles that have been placed will be the size of the array

        if( num_placements == 0):
            return 0

        elif( num_placements == 1):

            role = comp_stats[0]['role']

            if( role == "tank" ):
                tank_rating = comp_stats[0]['level']

            elif( role == "damage"):
                damage_rating = comp_stats[0]['level']

            elif( role == "support"):
                support_rating = comp_stats[0]['level']

        elif( num_placements == 2 ):

            role1 = comp_stats[0]['role']
            role2 = comp_stats[1]['role']

            if( role1 == "tank" ):
                tank_rating = comp_stats[0]['level']

            elif( role1 == "damage"):
                damage_rating = comp_stats[0]['level']

            elif( role1 == "support"):
                support_rating = comp_stats[0]['level']

            if( role2 == "tank" ):
                tank_rating = comp_stats[1]['level']

            elif( role2 == "damage"):
                damage_rating = comp_stats[1]['level']

            elif( role2 == "support"):
                support_rating = comp_stats[1]['level']


        elif( num_placements == 3 ):
            tank_rating = comp_stats[0]['level']
            damage_rating = comp_stats[1]['level']
            support_rating = comp_stats[2]['level']


        stats = (tank_rating,damage_rating,support_rating,average_rating)
        #print(self.account,stats)

        return stats


    def profile_to_json(self):

        data = self.get_profile()
        with open("data.json","w")as f:
            f.write(json.dumps(data,indent=4,sort_keys=True))
