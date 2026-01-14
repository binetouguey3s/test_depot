#Exercice 4 : Création d'une Fiche d'Identification Animale Stable
# Dans un centre de recensement, certaines informations d’un animal ne doivent pas être modifiées.
# Stockage initial :
# Créez une fiche d’identité en utilisant un tuple :
# ("Milo", "Chien", 7, "A1234")

tuple_animal = ("Milo", "Chien", 7, "A1234")

# Consultation :
# Affichez séparément :

# le nom,
nom = tuple_animal[0]

# l’espèce,
espece = tuple_animal[1]

# l’âge,
age = tuple_animal[2]

# l’identifiant.
identidiant = tuple_animal[3]

# Vérification :
# Déterminez et affichez si l’animal a plus de 5 ans.

age  =  tuple_animal[2] 

for age in tuple_animal():
    print(age)
    if age > 5 {
        print("L'enfant a plus de 5ans")
    else 
        print("L'enfant a moins de 5ans")
}

# Ajout d’information non fixe :
# Sans modifier le tuple, créez une nouvelle structure (par exemple un dictionnaire) contenant :
# la fiche d’identité (tuple),

animal_nouveau= {
    "identite_fixe": tuple_animal,
    "remarque": "Doit être vacciné en mars"
}

# une remarque modifiable (ex : "Doit être vacciné en mars").

animal_nouveau["remarque"] = "Vaccination effectuée"
print("Modification :", animal_nouveau)

# Affichez cette structure.
print("Fiche nouvelle :", animal_nouveau)




