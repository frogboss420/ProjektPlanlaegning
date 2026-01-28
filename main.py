import json
import os.path
from datetime import datetime

#funktion der kan kalde Fil klassens readFile metode, eller LoadFil's overlæsset readFile metode
def læsFil(fil):
    fil.readFile()

def getDirFiles(): #Indsætter alle json filer i en liste
    out = []
    for i in os.listdir("Filer/"):
        if i.endswith(".json"):
            out.append(i)
    return out

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
                print("Invalid getDato() argument")
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


class LoadFil(Fil): #nedarvning af Fil
    def __init__(self, name: str):
        db = DatoBehandler
        if not os.path.isfile("Filer/" + name + ".json"):
            print("Error! Fil eksisterer ikke!")
        else:
            with open("Filer/" + name + ".json", "r") as file:
                self.info = json.load(file)
                file.close()
            self.dato = self.info["Dato"]
            self.deadline = self.info["Deadline"]

    def readFile(self): #overlæsning af nedarvet metode
        print("Dato for oprettelse af " + self.info["Navn"] + ": " + self.dato[0] + "/" + self.dato[1] + "/" + self.dato[2]
        + "\nDeadline for " + self.info["Navn"] + ": " + self.deadline[0] + "/" + self.deadline[1] + "/" + self.deadline[2])



#bruger grænseflade

while True:
    brugervalg = input("VÆLG eller OPRET projekt\n")

    if brugervalg.upper() == "OPRET":
        active = True
        while active:
            nyprojektnavn = input("Vælg navn på nyt projekt\n")

            if os.path.isfile("Filer/"+nyprojektnavn+".json"):
                cancel = input("Fil eksisterer allerede. Vil du annullere opretning af nyt projekt? (Y)\n")
                if cancel.upper() == "Y":
                    active = False
                    break
            else:
                nyprojekt = Fil(nyprojektnavn)
                nyprojekt.writeFile()
                print("Projekt '"+nyprojektnavn+"' gemt!")
                active = False


    if brugervalg.upper() == "VÆLG":
        print(getDirFiles())
        valgtfil = input("vælg fil\n")
        if not os.path.isfile("Filer/"+valgtfil+".json"):
            print("Error! Fil findes ikke!")
        else:
            ÅbnetFil = LoadFil(valgtfil)
            læsFil(ÅbnetFil)



'''jsontest = json.dumps(test.info) #konverter python dict til json string (s i dumps betyder str)

loadjsontest = json.loads(jsontest) #konverter json string til python dict
print("dato test " + str(loadjsontest["Dato"]) + "\ndeadline test " + str(loadjsontest["Deadline"]))

with open("Filer/test.txt","w") as file:
    file.write("test text")

if os.path.isfile("Filer/test.txt"):
    print("test")'''