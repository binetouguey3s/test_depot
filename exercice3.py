#Comment créer un dictionnaire vide ?
mon_dictio = {}

#Comment ajouter une nouvelle clé dans un dictionnaire ?
mon_dictio["nouvelle_cle"] = "valeur"

#Comment modifier la valeur associée à une clé existante ?
mon_dictio["cle existante"] = "nouvelle_valeur"

#Comment supprimer une clé d’un dictionnaire ?
del mon_dictio["ma_cle"] #Supprimer avec del
valeur = mon_dictio.pop("ma_cle") #Supprimer avec .pop

#Quelle instruction permet de parcourir un dictionnaire pour afficher :

#les clés ?
for cle in mon_dictio.keys():
    print(cle)

#les valeurs ?
for valeur in mon_dictio.values():
    print(valeur)

#Que se passe-t-il si on essaie d’accéder à une clé qui n’existe pas ?
Si on le fait Python entre une erreur KeyError et cela arretera le programme


