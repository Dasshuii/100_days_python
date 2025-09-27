from util.input_util import InputUtil
from models.record import Record
from models.player import Player
from managers.data_manager import DataManager

class Game:
    def __init__(self, data_manager : DataManager):
        self.__score = 0
        self.__data_manager = data_manager
        self.__questions = data_manager.questions

    def ask_user(self, question : str, index : int) -> str:
        prompt = 'Q.{index}: {text}? '
        return InputUtil.get_user_input(prompt.format(index = index + 1, text = question))
    
    def check_answer(self, question_answer : str, answer : str) -> bool:
        return question_answer.lower() == answer.lower()
    
    def result_message(self, correct : bool, question_answer : str, score : int) -> str:
        message = f'{'You got it right!' if correct else 'That\'s wrong.'}\nThe correct answer was: {question_answer}\nYour current score is: {score}'
        return message

    def start(self, player : Player) -> None:
        for index, question in enumerate(self.__questions):
            answer = self.ask_user(question.question, index)
            correct = self.check_answer(question.answer, answer)
            if correct:
                self.__score += 1
            print(self.result_message(correct, question.answer, self.__score))
        self.__data_manager.save_record(Record(player, self.__score))
    
