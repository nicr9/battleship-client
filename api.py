"""
Handles api requests

Handles API requests. Note that request_string should not begin with a /
"""

import requests

API_ADDRESS = "http://battleship-env-1.elasticbeanstalk.com/"

def create_new_player(player_name):
    return requests.get(API_ADDRESS + "/player/new?=" + player_name

def shoot(token, game_id, x, y):
    # TODO: Make sure game is in fight status
    return requests.get(API_ADDRESS + token + "/game/" + game_id + \
        "/shoot/", params = {'x' : x, 'y' : y} ).json()

def raw_get(request_string):
    """Returns JSON response from API with provided request string"""
    return requests.get(API_ADDRESS + request_string).json()

# if __name__ == '__main__':
#    print(raw_get("player/new?name=Player Name"))