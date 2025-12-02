import json
import os.path
from datetime import datetime

class DatoBehandler:
    def getDato(self, time):
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
        return [self.getDato("Dag"), self.getDato("Måned"), self.getDato("År")]

    def deadlineInput(self):
        while True:
            dato: str = input("Hvad er projektets deadline? Skriv i format DD-MM-YYYY\n")
            if len(dato) != 10:
                print("Error! Tjek formatering.\n")
            elif dato[2] and dato[5] != "-":
                print("Error! Mangler seperatorerne '-'! Tjek formatering.")
            elif not dato.replace("-", "").isdigit():
                print("Error! Ikke eksklusivt numerisk mellem seperatorerne!")
            else: break

        out: list = dato.split(sep="-")
        return out


class Fil:
    def __init__(self, name: str):
        db = DatoBehandler()
        if not os.path.isfile("Filer/"+name+".json"):
            self.deadline = db.deadlineInput()
        else:
            with open("Filer/"+name+".json", "r") as file:
                finfo = json.load(file)
                self.deadline = finfo["Deadline"]
                file.close()
        self.dato = db.dato()
        self.info = {"Dato":self.dato, "Deadline":self.deadline, "Navn":name}

    def writeFile(self):
        #potentiel overflødig kode
        '''if not os.path.isfile("Filer/" + self.info["Navn"]):
            self.info["Navn"]: str = input("Angiv filnavn\n")
            print(self.info["Navn"])'''
        with open("Filer/" + self.info["Navn"] + ".json", "w") as file:
            json.dump(self.info, file)
            file.close()


    def readFile(self):
        with open("Filer/" + self.info["Navn"] + ".json", "r") as file:
            print(json.load(file))
            file.close()



test = Fil("test")
#test.writeFile()
test.readFile()


'''jsontest = json.dumps(test.info) #konverter python dict til json string (s i dumps betyder str)

loadjsontest = json.loads(jsontest) #konverter json string til python dict
print("dato test " + str(loadjsontest["Dato"]) + "\ndeadline test " + str(loadjsontest["Deadline"]))

with open("Filer/test.txt","w") as file:
    file.write("test text")

if os.path.isfile("Filer/test.txt"):
    print("test")'''