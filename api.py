"""
Handles api requests

Handles API requests. Note that request_string should not begin with a /
"""

import requests

API_ADDRESS = "http://battleship-env-1.elasticbeanstalk.com/"

def get(request_string):
    """Returns JSON response from API with provided request string"""
    return requests.get(API_ADDRESS + request_string).json()

def post(request_string):
    """Returns JSON response from API with provided request string"""
    return requests.get(API_ADDRESS + request_string).json()

# if __name__ == '__main__':
#    print(get("player/new?name=Player Name"))