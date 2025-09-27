from managers.data_manager import DataManager
from models.player import Player
from game import Game
from util.input_util import InputUtil

BASE_PATH = './data/'

def main():
    data_manager = DataManager(BASE_PATH + 'questions.json', BASE_PATH + 'records.json')
    data_manager.init_data()
    
    name = InputUtil.get_user_input('Your name? ')
    game = Game(data_manager)

    game.start(Player(name))
    data_manager.commit()
    

if __name__ == '__main__':
    main()