# My Little Pappers

Voici notre projet Python My Little Papers.

# Instructions

=================

L’objectif de ce projet est de créer votre propre outil de collecte d’information sur les entreprises en utilisant [l’API Sirene](https://portail-api.insee.fr/catalog/api/2ba0e549-5587-3ef1-9082-99cd865de66f). Cette API permet de requêter les données du répertoire Sirene des entreprises depuis 1973. Ce répertoire contient les unités légales (SIREN) et les établissements (SIRET).

Pré-requis
----------

Avant de commencer, il est nécessaire de [créer un compte](https://portail-api.insee.fr/) sur le site de l’INSEE.

*   Cliquer sur “Se Connecter”
*   Connexion pour les externes
*   Enregistrement

Une fois l’enregistrement, vous pouvez vous connecter sur le site. Se rendre sur la page dédiée à [l’API Sirene](https://portail-api.insee.fr/catalog/api/2ba0e549-5587-3ef1-9082-99cd865de66f).

*   Cliquer sur “Souscrire”
*   Cliquer sur “Suivant”. _Notez que vous êtes limités à 30 requêtes par minute_
*   Je souhaite créer une application
    *   Général:
        *   Nom de l’application : A votre discrétion
        *   Description : Mettez qu’il s’agit d’un projet pédagogique pour de la recherche en sources ouvertes
        *   Domaine utilisé par l’application : Laisser vide
        *   Image de l’application : Laisser vide
    *   Sécurité :
        *   Simple : Tout laisser vide et cliquer sur suivant
    *   Souscription :
        *   Cliquer sur “Souscrire”
        *   Dans le panneau latéral droit, une ligne s’affiche. Pas besoin de laisser de commentaire
        *   Cliquer sur Suivant
    *   Cliquer sur créer l’application
*   Cliquer sur “L’application XX est prête”
*   Cliquer sur l’onglet “Souscription”
*   Dans la liste, cliquer sur l’API Sirene
*   Sur le panneau latéral droit, un onglet “Clés d’API” apparait
    *   Cette clé API est indispensable pour réaliser vos requêtes API. Gardez-le précieusement. En cas de “vol”, vous pouvez le révoquer (il ne sera plus utilisable) ou le renouveller.

Ce projet, bien que guidé, nécessitera que vous preniez connaissance de la documentation de l’API : ce sont les instructions laissées par les développeurs pour que vous puissiez l’utiliser correctement. La documentation est disponible [ici](https://portail-api.insee.fr/catalog/api/2ba0e549-5587-3ef1-9082-99cd865de66f/doc).

### Documentation Swagger

Dans le monde des API REST (la norme aujourd’hui), Swagger est l’outil de référence pour documenter les appels API. Il permet notamment de “jouer” les requêtes directement depuis la documentation, un peu comme Jupyter vous permet d’exécuter du code directement dans le cours. Cet outil est très puissant et sera votre alié !

Nous allons faire notre première requête ensemble, grâce au Swagger. Cliquer sur “Authorize” et coller dans la fenêtre le token API récupéré plus tôt.

*   Déplier l’onglet “Unité légale”
*   Déplier le premier bloc (GET)
*   Cliquer sur “Try it out”
*   Dans les paramètres, pour le champ `q`, entrer `siren:495160657`
    *   Les variables existantes sont disponibles sur [cette page](https://www.sirene.fr/static-resources/documentation/v_sommaire_311.htm#descvar)
        *   _Note_ : Les variables en **gras** sont dites **historisées**. Leur utilisation est donc différente
*   Cliquer ensuite sur Execute : la réponse au format JSON devrait s’afficher. Sinon :
    *   Erreur 401 : Il faut remettre votre clé API en cliquant sur Authorize
    *   Erreur 400 : Problème dans la requête. Il faut lire le message d’erreur pour essayer de comprendre où se situe le problème
*   Nous allons utiliser une variable **historisée** : sa valeur a pu changer au cours de la vie de l’entreprise. Prenons par exemple son nom. Pour rechercher “Lexfo”, nous allons donc faire la requête :
    *   q=periode(denominationUniteLegale:Lexfo)

Pour plus d’informations sur l’API [ici](https://www.sirene.fr/static-resources/documentation/sommaire_311.html)

Palier 1
--------

Dans ce premier palier, le programme doit demander à l’utilisateur un code SIREN. S’il est valide (bonne taille et composé uniquement de nombre), le programme requête l’API pour récupérer les informations sur l’entreprise. Il doit afficher :

*   Le dernier nom de l’entreprise connu
*   Date de création de l’entreprise
*   Catégorie d’entreprise
*   Adresse de l’entreprise

Palier 2
--------

A compléter :

*   Avoir un menu permettant de choisir le champ sur lequel on veut filtrer:
    *   Nom de l’entreprise
    *   Ville de l’entreprise
    *   SIRET
    *   Catégorie

Palier 3
--------

A compléter :

*   Importer une liste de SIREN depuis un fichier texte et exporter les résultats dans un CSV

Bonus
-----

*   Gérer les dates des périodes sur lesquelles les recherches ont lieu
*   Permettre de faire une recherche sur plusieurs champs (avec des and/or)
*   Amusez vous
