# Quelle instruction permet de créer une liste vide en Python ?
nom_liste= [] # par exemple

#Comment ajouter un élément à la fin d’une liste ?
nom_liste = ["bap", "cap", "fap"]
nom_liste.append("zap")  # etant par exemple de dernier element de la liste 
nom_liste = list["bap", "cap", "fap","zap"] # Apres ajout

#Comment supprimer un élément d’une liste à partir de sa valeur ?
nom_liste = list["bap", "cap", "fap"]
nom_liste.pop(1) 
nom_liste = list["bap", "fap"] #  suppression du cap

#Quelle est la différence entre : #remove()  et #pop() 
.remove() permet de supprimer un element d'une liste hors pop permet de supprimer le dernier element d'une liste.

#Comment créer une copie d’une liste existante ?
nouvelle_liste= nom_liste.copy()
nouvelle_liste= nom_liste[:] # avec les slicing





