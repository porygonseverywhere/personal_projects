
global API_DICT
API_DICT = {
    200: {'status': 'OK', 
            'description': 'The request was completed.'},
    201: {'status': 'Created', 
            'description': 'A new resource was successfully created.'},
    400: {'status': 'Bad Request', 
            'description': 'The request was invalid.'},
    401: {'status': 'Unauthorized', 
            'description': 'The request did not include an authentication token or the authentication token was expired.'},
    403: {'status': 'Forbidden', 
            'description': 'The client did not have permission to access the requested resource.'},
    404: {'status': 'Not Found', 
            'description': 'The requested resource was not found.'},
    405: {'status': 'Method Not Allowed', 
            'description': 'The HTTP method in the request was not supported by the resource. For example, the DELETE method cannot be used with the Agent API.'},
    409: {'status': 'Conflict', 
            'description': 'The request could not be completed due to a conflict. For example, POST ContentStore Folder API cannot complete if the given file or folder name already exists in the parent location.'},
    500: {'status': 'Internal Server Error', 
            'description': 'The request was not completed due to an internal error on the server-side.'},
    503: {'status': 'Service Unavailable', 
            'description': 'The server was unavailable.'}
    }

global BASE_URL
BASE_URL = "http://pokeapi.co/api/v2"

# api endpoints of interest from api
global ENDPOINTS
ENDPOINTS = [
    "ability",
    "encounter-condition",
    "encounter-condition-value",
    "encounter-method",
    "generation",
    "pokemon",
    "type",
    "version",
    "version-group",
]


import requests
import json
import pandas as pd 
import os




class Connect_to_API:

    def get_data(self, api):
        """
        Pull root api data that allows you to make connections to other dataframes.
        """
        response = requests.get(f"{api}")
        if response.status_code == 200:
            print("Sucessfully fetched the data.")
            self.data = self.root_json_to_df(response.json())
        elif response.status_code in API_DICT.keys():
            print(API_DICT[response.status_code])
        else:
            print("Something went wrong. The api status code was not found in our dictionary.")



    def root_json_to_df(self, obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        data = pd.json_normalize(obj)
        return data


    def __init__(self, api):
        self.get_data(api)
        self.data = pd.DataFrame()
        

    # def __call__(self):
    #     return self.data



def api_url(base, endpoint):
    return '{}/{}'.format(base, endpoint)

def main():

    for x in ENDPOINTS:
        api = Connect_to_API(api_url(BASE_URL, x))
        print(api.data)




if __name__ == "__main__":
    main()

#makes the api calls but how do we return the df and make it accessible?


# present a list of Game Versions
# with the input of a game version, return pokemon, type, damage relationships

# database that contains pokemon table 1, game version table 2, generation? table 3, damage relationship{double dmg from, double dmg to, half damage from, non damg to, etc.}
