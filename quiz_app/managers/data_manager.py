from managers.file_manager import FileManager
from parsers.question_parser import QuestionParser
from parsers.record_parser import RecordParser
from models.record import Record

class DataManager:
    def __init__(self, questions_path, records_path):
        self.__questions_path = questions_path
        self.__records_path = records_path
        self.__questions = []
        self.__records = []

    def init_data(self):
        raw_questions = FileManager.get_file_content(self.__questions_path)
        raw_records = FileManager.get_file_content(self.__records_path)
        self.__questions = QuestionParser.json_to_questions(raw_questions)
        self.__records = RecordParser.json_to_records(raw_records)
    
    @property
    def questions(self):
        return self.__questions
    
    @property
    def records(self):
        return self.__records
    
    def save_record(self, record : Record):
        self.records.append(record)
    
    def commit(self) -> None:
        FileManager.write(self.__records_path, list(map(RecordParser.to_dict, self.records)))