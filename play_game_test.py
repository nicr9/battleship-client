"""
Actually plays the game.
"""

import api
import json

if __name__ == '__main__':
    # Create both players
    player1 = api.create_new_player("DROP")
    player2 = api.create_new_player("TEST")
    # Host starts game
    new_game = api.create_and_start_game(
        token=player1["token"],player2_id=player2["id"])
    # Setup ships for both players
    player1_ship_poitions = api.set_ships_random(
        token=player1["token"], game_id=new_game["id"])
    player2_ship_poitions = api.set_ships_random(
        token=player2["token"], game_id=new_game["id"])
    print("Player 1 board: " + str(player1_ship_poitions))
    print("Player 2 board: " + str(player2_ship_poitions))
    # TODO: Being fighting using AI algos
    # TODO: Catch exception on shoot when game has finished
