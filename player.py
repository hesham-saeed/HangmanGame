
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"Player: {self.name} Score: {self.score}"