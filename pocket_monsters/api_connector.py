"""
This file contains the initial code to simply connect to various pokebase api endpoints, and generate dataframes from them.
Intention is to connect, pull, format, store, read back in, and explore.
Reminder to clean code, provide helpful context and create a more organized structure.
"""


"""
dictionary of common api codes and responses helpful for debugging
"""
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


"""
more can be appended in the future. these contain the various endpoints for the api url's
"""
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
import numpy as np


def build_url(base, endpoint):
    return '{}/{}'.format(base, endpoint)


def connect_to_api(api):
    if 'api' not in locals():
        raise Exception("No api url found in connect_to_api(). Stopping the script.")

    response = requests.get(f"{api}")

    if response.status_code == 200:
        print("Sucessfully fetched the data.")

    elif response.status_code in API_DICT.keys():
        print(API_DICT[response.status_code])
    else:
        print("Something went wrong. The api status code was not found in our dictionary.")

    return response

def root_json_to_df(obj):
    #text = json.dumps(obj, sort_keys=True, indent=4)
    df = pd.DataFrame.from_dict(obj['results'])
    """
    api calls seem to have the same structure.
    so str[-2] grabs the id
    replace the "name" w/ the str[-3]?
    """
    df['id'] = df['url'].str.split('/').str[-2]
    df.rename(columns = {'name' : df['url'].str.split('/').str[-3].iloc[0]}, inplace = True)
    df = df.drop(columns = ['url'])
  
    return df


def main():

    
    combined_poke_data = {}

    for x in ENDPOINTS:
        api_call = connect_to_api(build_url(BASE_URL, x))

        combined_poke_data["df_{}".format(x)] = root_json_to_df(api_call.json())
        #You can access the dataframes by call combined_poke_data[key], where key = "df_endpoint_1", "df_endpoint_2", ...
        #print(combined_poke_data["df_{}".format(x)])





if __name__ == "__main__":
    main()
