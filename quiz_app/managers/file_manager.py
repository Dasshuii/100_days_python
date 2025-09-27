import json

class FileManager:
    @staticmethod
    def get_file_content(DATA_PATH : str) -> dict:
        with open(DATA_PATH, 'r') as content:
            data = json.load(content)
        return data
    
    @staticmethod
    def write(DATA_PATH : str, data : str) -> None:
        with open(DATA_PATH, 'w') as file:
            json.dump(data, file, indent = 4)

