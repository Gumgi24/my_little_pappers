import requests

menu_choix = input("Choisissez un mode de recherche : \n1. Recherche par SIRET\n2. Recherche par Nom\n 3. Recherche par Ville\n 4. Recherche par Catégorie\n \n Mode de recherche : ")

if menu_choix == "1":
  recherche = input("Entrez un SIRET: ")
  champ = "siret"

elif menu_choix == "2":
  recherche = input("Entrez un nom: ")
  champ = "denominationUniteLegale"

elif menu_choix == "3":
  recherche = input("Entrez une ville: ")
  champ = " "

elif menu_choix == "4":
  recherche = input("Entrez une catégorie: ")
  champ = " "

def recherche_siret(field, query):
  url = "https://api.insee.fr/api-sirene/3.11/siret?q=" + field + "%3A" + query #49516065700062

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

recherche_siret(champ, recherche)
