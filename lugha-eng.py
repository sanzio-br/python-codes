word = input ("enter a word in luhya : ")
dic ={"mkhana":"girl", "kuka": "grandpa", "ingokho":"kuku", "malwa":"alcohol", "ichupa":"bottle", "mafura":"oil", "matsi":"maji", "ichirishi":"bull", "shichiko":"spoon", "shilotwa":"knife", "makanda":"beans", "shitapu":"book", "thingutsa":"vegetables", "vusuma":"ugali", "inyama":"meat", "ingombe":"cow", "msiani":"boy", "sieva":"dance", "matuma":"maize", "msala":"tree"}

def get_val(key):
    return dic[key]

eng = get_val(word)
print(word + " in english is : " + eng)