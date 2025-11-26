import json
from datetime import datetime

class dateManager:
    def getDate(self, time):
        match time:
            case "Dag":
                return datetime.today().strftime('%d')
            case "Måned":
                return datetime.today().strftime('%m')
            case "År":
                return datetime.today().strftime('%Y')
            case _:
                print("Invalid getDate() argument")
                return "Error"

    def dato(self):
        return [self.getDate("Dag"), self.getDate("Måned"), self.getDate("År")]


class Fil:
    def __init__(self):
        dm = dateManager()
        self.dato = dm.dato()


test = Fil()

print(test.dato)