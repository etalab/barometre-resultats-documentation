# Déployer Parcoursup 
## Description générale du jeu de données 
**Action prioritaire** : avec Parcoursup, le Ministère de l’enseignement supérieur, de la recherche et de l’innovation (MESRI) a engagé une profonde transformation de l’accès à l’enseignement supérieur pour lutter contre l’échec dans le premier cycle de l’enseignement supérieur. Le nouveau dispositif d'orientation permet de :
-	Supprimer le tirage au sort pour l’accès à l’enseignement supérieur 
-	Rendre aux candidats la liberté de formuler librement leurs vœux afin d’accéder aux formations de leur choix et leur donner le dernier mot, 
-	Lutter contre les inégalités d’accès à l’information et lever les freins à la démocratisation de l’accès à l’enseignement supérieur,
-	Favoriser la mobilité géographique des étudiants, en particulier des plus modestes,
-	Développer la personnalisation des parcours et accompagner la réussite des étudiants, en créant des parcours adaptés à ceux qui ne disposent pas de tous les atouts pour réussir.

**Indicateur** : *Taux de réussite aux examens de licence 1*

Il s'agit du taux mesuré de passage en L2 des néo-bacheliers inscrits en L1 à la rentrée précédente. Il correspond au ratio « Inscrits en L2 / Inscrits en L1 », calculé sur la population des néo-bacheliers inscrits en L1.
Ce ratio est très différent selon les caractéristiques du public accueilli. Par exemple, les bacheliers de la série générale réussissent en moyenne mieux que ceux de la série technologique. Les caractéristiques moyennes des bacheliers diffèrent selon les établissements et donc les académies, rendant les comparaisons territoriales délicates. Des indicateurs affinés de valeur ajoutée, prenant en compte ces caractéristiques, sont également disponibles.

## Description du mode de production du jeu de données 
Les données sont constituées à partir de remontées administratives recueillies via le Système d’information du Suivi de l’Etudiant (SISE). Ces données sont élaborées par la sous-direction des Systèmes d'Information et des Études Statistiques (SIES) du MESRI. 
Ces données sont exhaustives sur le champ des néo-bacheliers inscrits en première année de licence, à la rentrée N.
Ces données donnent lieu à publication régulière par le MESRI : la dernière publication date du mois d’octobre 2020. Elle est consultable [ici](https://www.enseignementsup-recherche.gouv.fr/cid154937/reussite-et-assiduite-en-premiere-annee-de-licence-impact-de-la-loi-ore-nouveaux-indicateurs.html).

## Description des métadonnées 
Synthèse : 
-	Fréquence de mise à jour : annuel
-	Couverture temporelle : 2017-2019
-	Couverture spatiale : France 
-	Granularité spatiale : nationale, départementale
-	Nature des données : valeurs en pourcentage

Le champ des indicateurs est constitué des néo-bacheliers N inscrits en première année de licence (L1) à la rentrée universitaire N. En sont exclus les étudiants ayant pris une inscription parallèle en STS, DUT ou CPGE ou ayant obtenu le diplôme de Licence à l’issue de la première année.

L1 = première année du cursus Licence.

L2 = deuxième année du cursus Licence.

Les indicateurs sont ici calculés et diffusés au niveau de l’académie. 

## Lexique des termes 
- Inscrits en L1 : étudiants néo-bacheliers inscrits en L1 dans l’établissement à la rentrée universitaire N.
- Inscrits en L2 : étudiants inscrits en L2 à la rentrée universitaire N+1, quel que soit l’établissement d’accueil.
- Valeur ajoutée :
Chaque université possède sa propre population étudiante, qui diffère par ses caractéristiques sociales et le parcours antérieur : série du baccalauréat, âge au moment de son obtention... Or, les études sur la réussite à l’université montrent que la réussite varie fortement selon ces caractéristiques.

Aussi, à côté des indicateurs bruts, des taux simulés peuvent être calculés dans chaque établissement, correspondant à la réussite qu’on pourrait observer dans cet établissement si sa population étudiante avait les mêmes caractéristiques que la population étudiante au niveau national, caractéristiques définies par les critères suivants :
-	Sexe
-	Âge au baccalauréat (3 modalités : à l’heure ou en avance, en retard d’un an, en retard de plus d’un an)
-	Série du baccalauréat (6 modalités : Littéraire, Economique, Scientifique, Technologique STG, Autre technologique, Professionnel)
-	Mention obtenue au baccalauréat (6 modalités : Très bien, Bien, Assez bien, Passable au premier groupe, passable au deuxième groupe, Inconnue)
-	Origine sociale (5 modalités : très favorisé (cadres, enseignants…), favorisé (professions intermédiaires), assez défavorisé (employés…), défavorisé (ouvriers…), non réponse)
-	Discipline (5 modalités en 2018 : Droit, Sciences Politiques ; Sciences Economiques, Gestion, Administration Economique et Sociale (AES) ; Arts, Lettres, Langues, Sciences Humaines et Sociales (SHS) ; Sciences, Santé ; Sciences et Techniques des Activités Physiques et Sportives (STAPS).

L’écart entre le taux observé et le taux simulé est appelé la valeur ajoutée. Elle permet de situer une université par rapport à la moyenne nationale une fois ces effets de structure pris en compte.

Les valeurs ajoutées ne sont pas diffusées ici.