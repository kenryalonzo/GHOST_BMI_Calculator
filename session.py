import json


class Session():
    @classmethod
    def get_session(cls):
        with open("./Data/session.json", "r") as file:
            data_str = file.read()
            data = json.loads(data_str)
            return data

        pass
    
    
    @classmethod
    def make_session(cls, data):
        with open("./Data/session.json","w") as file:
            json.dump(data, file)
        pass
      