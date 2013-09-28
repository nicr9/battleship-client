"""
Actually plays the game.
"""

import api
import json
import time
from statespace import StateSpace

if __name__ == '__main__':
    # Create both players
    player1 = api.create_new_player("DROPdsf")
    player2 = api.create_new_player("TESTasd")
    # Host starts game
    new_game = api.create_and_start_game(
        token=player1["token"],player2_id=player2["id"])
    # Setup ships for both players
    player1_ship_poitions = api.set_ships_random(
        token=player1["token"], game_id=new_game["id"])
    player2_ship_poitions = api.set_ships_random(
        token=player2["token"], game_id=new_game["id"])
    #print("Player 1 board: " + str(player1_ship_poitions))
    print("Player 2 board: " + str(player2_ship_poitions))
    while player2_ship_poitions["status"] != "fight":
        sleep(0.1)
    # print("READY!")
    #statespace = StateSpace(x=player1_ship_poitions[""])
    #api.shoot(token=player1["token"], game_id=new_game["id"],
    #    x=)
    # TODO: Being fighting using AI algos
    # TODO: Catch exception on shoot when game has finished
