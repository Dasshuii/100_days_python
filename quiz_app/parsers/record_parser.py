from models.record import Record
from models.player import Player

class RecordParser:
    @staticmethod
    def json_to_records(records : dict) -> list:
        record_list = []
        for record in records:
            record_list.append(RecordParser.fromJson(record))
        return record_list

    @staticmethod
    def fromJson(record : dict) -> Record:
        return Record(Player(record['player']), record['score'])

    @staticmethod
    def to_dict(record : Record) -> dict:
        return dict(player = record.player.name, score = record.score)