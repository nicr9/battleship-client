
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

class JSONRequestModels:
    """Contains objects for JSON requests"""
