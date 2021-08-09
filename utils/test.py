from tinydb import TinyDB, Query, where


db = TinyDB("db.json", indent=4)
db.truncate()


adherents = db.table("adherent")


adherents.insert({"nom": "herlant", "prenom": "christophe", "age": 49})
adherents.insert({"nom": "herlant", "prenom": "sebastien", "age": 43})
adherents.insert({"nom": "herlant", "prenom": "loyce", "age": 16})
adherents.insert({"nom": "herlant", "prenom": "lola", "age": 14})

for adherent in adherents:
    print(adherent)
    
Adherent = Query()

print("******")

lola = adherents.search(Adherent.prenom == "lola")
print(lola)

loyce = adherents.search(where("prenom") == "loyce")
print(loyce)

sebastien = adherents.get(doc_id=2)
print(sebastien)


print("******")


adherents.update({"age": 50}, Adherent.prenom == "christophe")

christophe = adherents.get(doc_id=1)
print(christophe)