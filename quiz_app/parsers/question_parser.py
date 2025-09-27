from models.question import Question

class QuestionParser:
    @staticmethod
    def json_to_questions(questions : dict) -> list:
        question_list = []
        for question in questions:
            question_list.append(QuestionParser.fromJson(question))
        return question_list
    
    @staticmethod
    def fromJson(question : dict) -> Question:
        return Question(question['category'], question['type'], question['difficulty'], question['question'], question['answer'])
    
    @staticmethod
    def toJson(question : Question) -> str:
        return '{' \
        '"category":"{category}",' \
        '"type":"{type}",' \
        '"question":"{question}"' \
        '"answer":"{answer}"' \
        '}'.format(category = question.category, type = question.type, question = question.question, answer = question.answer)