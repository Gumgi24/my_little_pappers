import requests

menu_choix = input("Choisissez un mode de recherche : \n1. Recherche par SIRET\n2. Recherche par Nom\n 3. Recherche par Ville\n 4. Recherche par Catégorie\n \n Mode de recherche : ")

if menu_choix == "1":
  recherche1 = input("Entrez un SIRET: ")
  champ1 = "siret"

elif menu_choix == "2":
  recherche2 = input("Entrez un nom: ")
  champ2 = "denominationUniteLegale"

elif menu_choix == "3":
  recherche3 = input("Entrez une ville: ")
  champ3 = "libelleCommuneEtablissement"

elif menu_choix == "4":
  recherche4 = input("Entrez une catégorie: ")
  champ4 = "categorieEntreprise"

def recherche_siret(field1, query1, field2, query2, field3, query3, field4, query4):
  url = "https://api.insee.fr/api-sirene/3.11/siret?q=" + field1 + "%3A" + query1 #49516065700062 = Exemple Lexfo
  
  if field2:
    url += "%2C%20" + field2 + "%3A" + query2
  if field3:
    url += "%2C%20" + field3 + "%3A" + query3
  if field4:
    url += "%2C%20" + field4 + "%3A" + query4
  

  payload = {}
  headers = {
    'accept': 'application/json',
    'X-INSEE-Api-Key-Integration': 'd49e0d28-c33a-4983-9e0d-28c33aa9835c'
  }

  response = requests.request("GET", url, headers=headers, data=payload)


  print(response.status_code)
  response = response.json()
  print(response['etablissements'][0]['uniteLegale']['denominationUniteLegale'])
  print(response['etablissements'][0]['uniteLegale']['dateCreationUniteLegale']) 
  print(response['etablissements'][0]['uniteLegale']['categorieEntreprise'])
  adresse_etablissement = response['etablissements'][0]['adresseEtablissement']
  print(
    adresse_etablissement["numeroVoieEtablissement"],  
    adresse_etablissement["typeVoieEtablissement"],
    adresse_etablissement["libelleVoieEtablissement"], 
    adresse_etablissement["codePostalEtablissement"],
    adresse_etablissement["libelleCommuneEtablissement"])

recherche_siret(champ1, recherche1, champ2, recherche2, champ3, recherche3, champ4, recherche4)
