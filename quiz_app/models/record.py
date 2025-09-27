from models.player import Player

class Record:
    def __init__(self, player : Player, score : int):
        self.__player = player
        self.__score = score
    
    @property
    def player(self) -> Player:
        return self.__player
    
    @property
    def score(self) -> int:
        return self.__score

    def __str__(self) -> str:
        return f'{self.player.name} - {self.score}'