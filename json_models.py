import json

class JSONResponseModels:
    """Contains objects for JSON requests"""

    class CreateNewPlayerResponse(object):

        def __init__(self, name, player_id, token):
            self.name = name
            self.player_id = player_id
            self.token = token

    class CreateNewGameResponse(object):
        """
        Creates a game with one player. The other can be added with a join
        request later.
        """

        def __init__(self, game, players):
            self.game = game
            self.player = players

    class CreateNewGameTwoPlayersResponse(object):
        """Creates and starts a game with two players"""

        def __init__(self, game_id, status, width, height, players):
            self.game_id = game_id
            self.status = status
            self.width = width
            self.height = height
            self.players = players

    class GetOpenGamesResponse(object):
        def __init__(self,open_games):
            self.open_games = open_games

    class GetGamesList(object):

        class Game(object):
            def __init__(self,game_id,status,width,height):
                self.game_id = game_id
                self.status = status
                self.width = width
                self.height = height

        def all_created_games():
            pass

        def all_finished_games():
            pass

        def all_ready_games():
            pass

        def all_ongoing_games():
            pass

        def my_finished_games():
            pass

        def my_ready_games():
            pass

        def my_ongoing_games():
            pass



