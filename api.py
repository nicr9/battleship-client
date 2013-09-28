"""
Handles API requests

Handles API requests. Note that request_string should not begin with a /
"""

import requests

API_ADDRESS = "http://battleship-env-1.elasticbeanstalk.com/"

def create_new_player(player_name):
    """ creates player and gets you a token"""
    return requests.get(API_ADDRESS + "/player/new?=" + player_name).json()

def create_and_start_game(token, player2_id):
    """ sets game to ready and lets you set your ships"""
    return requests.get(API_ADDRESS + token + "/game/new/" + \
        str(player2_id)).json()

def join_game(token, game_id):
    """joins a game in progress and lets you start setting ships"""
    return requests.get(API_ADDRESS + token + "/game/" + str(game_id) + \
        "/join").json()

def set_ships_random(token, game_id):
    """sets the ships randomly"""
    return requests.get(API_ADDRESS + token + "/game/" + str(game_id) + \
        "/randomize").json()

def shoot(token, game_id, x, y):
    # TODO: Make sure game is in fight status
    return requests.get(API_ADDRESS + token + "/game/" + game_id + \
        "/shoot/", params = {'x' : x, 'y' : y} ).json()

def raw_get(request_string):
    """Returns JSON response from API with provided request string"""
    return requests.get(API_ADDRESS + request_string).json()

# if __name__ == '__main__':
#    print(raw_get("player/new?name=Player Name"))