import json
import uuid


class task:
    def __init__(self,description,priority):
        self.description = description
        self.id = str(uuid.uuid4().fields[-1])[:5]
        if(int(priority) >= 0 and int(priority) <= 10):
            self.priority = priority

        else:
            print("podano zły priorytet!")

    def to_dictonary(self):
        data = {}
        data['Description'] = self.description
        data['Priority'] = self.priority
        data['ID:'] = self.id
        return data

    def get_id(self):
        return int(self.id)


