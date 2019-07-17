import datetime
from ..database import DB


class Hives(object):

    def __init__(self, number):
        self.number = number
        self.uterus = False
        self.frames = 0
        self.actions = []
        self.date_add = datetime.datetime.utcnow()
        self.date_check = None

    def insert(self):
        if not DB.find_one("hives", {"number": self.number}):
            DB.insert(collection='hives', data=self.json())

    def json(self):
        return {
            'number': self.name,
            'uterus': self.uterus,
            'frames': self.frames,
            'actions': self.actions,
            'date_add': self.date_add,
            'date_check': self.date_check,
        }
