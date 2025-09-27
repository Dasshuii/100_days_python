class Question:
    def __init__(self, category : str, type : str, difficulty : str, question : str, answer : str):
        self.__category = category
        self.__type = type
        self.__difficulty = difficulty
        self.__question = question
        self.__answer = answer

    @property
    def category(self) -> str:
        return self.__category
    
    @property
    def type(self) -> str:
        return self.__type
    
    @property
    def difficulty(self) -> str:
        return self.__difficulty

    @property
    def question(self) -> str:
        return self.__question
    
    @property
    def answer(self) -> str:
        return self.__answer
    
    def __str__(self) -> str:
        return self.__question