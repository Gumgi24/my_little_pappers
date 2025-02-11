import requests

SIRET = ""
NOM = ""
VILLE = ""
CTI = ""

while True:
  print("\n=== Menu de Recherche ===")
  print("1. Entrer SIRET (actuel : )")
  print("2. Entrer Nom (actuel : )")
  print("3. Entrer Ville (actuel : )")
  print("4. Entrer Catégorie (actuel : )")
  print("5. Lancer la recherche dans le CYBERESPACE")

  menu_choix = input("Entrez votre choix: ")

  if menu_choix == "1":
    SIRET = input("Entrez un SIRET: ")

  elif menu_choix == "2":
    NOM = input("Entrez un nom: ")

  elif menu_choix == "3":
    VILLE = input("Entrez une ville: ")

  elif menu_choix == "4":
    CTI = input("Entrez une catégorie: ")
  
  elif menu_choix == "5":
    break

  else:
    print("Choix invalide, CONNARD.")

def construction_query(siret, nom, ville, catégorie):
  query = ""
  
  if siret:
        query += "siret%3A" + siret

  if nom:
    if query:
      query += "%20AND%20"
    query += "denominationUniteLegale%3A" + nom

  if ville:
    if query:
      query += "%20AND%20"
    query += "libelleCommuneEtablissement%3A" + ville

  if catégorie:
    if query:
      query += "%20AND%20"
    query += "categorieEntreprise%3A" + catégorie

  return query

recherche = construction_query(SIRET, NOM, VILLE, CTI)

def recherche_siret(query):
  url = "https://api.insee.fr/api-sirene/3.11/siret?q=" + query #49516065700062 = Exemple Lexfo
  

  payload = {}
  headers = {
    'accept': 'application/json',
    'X-INSEE-Api-Key-Integration': 'd49e0d28-c33a-4983-9e0d-28c33aa9835c'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  print(url)
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

recherche_siret(recherche)
