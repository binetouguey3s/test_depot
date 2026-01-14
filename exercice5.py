# Exercice 5: 
# Vous êtes responsable de la gestion des contacts pour un festival de musique.
# Pour chaque contact, stockez :
# nom,
# prénom,
# numéro de téléphone,
# adresse e-mail.
Liste_contact = []

# Contraintes :
# utiliser un dictionnaire pour représenter un contact,
contact = {
    "nom": "Gueye",
    "prenom":"Astou",
    "numero":"771234567",
    "adresse_e_mail":"gueyastou@gmail.com"
}
# utiliser une liste pour stocker l’ensemble des contacts.

# Liste_contact= ["nom","prenom","numero","adresse_e_mail"]

# Travail demandé :
# créer au moins 3 contacts,
contact_1= ["Gueye","Astou","771234567","gueyastou@gmail.com"]
contact_2= ["Seye","Adja","787654321","seyeadja@gmail.com"]
contact_3= ["Ba","Fatou","780987654","fatouba@gmail.com"]


# les ajouter à la liste,
Liste_contact.extend(contact_1)
# Liste_contact.extend(contact_2)
# Liste_contact.extend(contact_3)
print(Liste_contact)

# afficher tous les contacts à l’aide d’une boucle.

for contacts in Liste_contact :
    print(f"le nom est:{contact['nom']}")
    print(f"le prenom est: {contact['prenom']}")
    print(f"le numero est: {contact['numero']}")
    print(f"le numero est:{contact['adresse_e_mail']}")
         
