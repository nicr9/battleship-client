import json

class PlayerState(object):
    def __init__(self, blob):
        self.update(blob)

    def update(self, blob):
        self.name = blob['name']
        self._id = blob['id']

        if 'token' in blob:
            self.token = blob['token']

        if 'won' in blob:
            self.won = blob['won']

        if 'lost' in blob:
            self.lost = blob['lost']

class GameState(object):
    def __init__(self, blob):
        self.update(blob)

    def update(self, blob):
        self._id = blob['id']
        self.status = blob['status']

        if 'height' in blob:
            self.height = blob['height']

        if 'width' in blob:
            self.width = blob['width']

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

    class GetCurrentGameStateResponse(object):

        def __init__(self, game_id, status, width, height,
            winner, players, boards):
            self.game_id = game_id
            self.status = status
            self.width = width
            self.height = height
            self.winner = winner
            self.players = players
            self.boards = boards

    class GetJoinGameResponse(object):

        # def __init__(self)

    class GetGamesList(object):



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

class Game(object):
            """Represents a game in a game list response"""
            def __init__(self, game_id, status, width, height):
                self.game_id = game_id
                self.status = status
                self.width = width
                self.height = height



