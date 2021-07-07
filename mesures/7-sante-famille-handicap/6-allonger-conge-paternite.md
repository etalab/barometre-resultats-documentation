# Allonger le congé paternité pour un meilleur développement de l’enfant 
## Description générale du jeu de données
**La réforme** : Lors de la naissance d'un enfant, le père salarié bénéficie du congé de paternité et d'accueil de l'enfant. Si la mère de l'enfant vit avec une autre personne salariée, celle-ci peut également bénéficier du congé. Le bénéficiaire du congé doit respecter certaines conditions (démarches, date de départ en congé, durée maximale du congé, nombre d’heures travaillées lors du trimestre précédent, durée d’exercice d’une activité professionnelle). Le salarié en congé bénéficie d'une indemnisation versée par la Sécurité sociale. Un projet de réforme prévoit le doublement de la durée du congé de paternité et d'accueil de l'enfant à partir du 1er juillet 2021 et instaure une période obligatoire de prise du congé de sept jours à la naissance de l’enfant.

**Le contexte** : depuis son entrée en vigueur en 2002, le taux de recours au congé paternité stagne. En 2019, il s’élevait à 67%.

**Indicateur** : L'indicateur mesure le nombre de pères / conjoints qui ont pris un congé de paternité et d'accueil de l'enfant, les congés étant rattachés à la période en fonction de leur date de début.

## Description du mode de production du jeu de données 
Il est possible de disposer de données trimestrielles à la maille régionale et départementale, mais pas sur l’ensemble des bénéficiaires puisque seules les données relevant du régime général (y compris travailleurs indépendants), sont disponibles. Ces données sont issues du Sniiram, système de données géré par la caisse nationale d’assurance-maladie, au sein d’une gouvernance associant l’Etat et les professionnels de santé. Ce système d’information agrège les données de liquidation d’indemnités journalières paternité des régimes ci-dessus.
Pour les fonctionnaires, les données sont disponibles une fois par an après retraitement par la DREES, soit plusieurs mois après la fin de l’année N.
Attention, l'indicateur suit le nombre de congés pris et non le taux de recours.

## Description des métadonnées 
-	Fréquence de mise à jour : trimestrielle
-	Couverture temporelle : 2019
-	Champ : régime général yc SLM, RSI, MSA, CRPCEN - France entière
-	Granularité spatiale : nationale, régionale, départementale
-	Nature des données : nombre de congés

## Lexique des termes 
La Sécurité sociale inclut 2 régimes principaux et des régimes spéciaux, couvrant chacun une ou plusieurs catégories socioprofessionnelles spécifiques et se caractérisant par des modalités de gestion et de prise en charge différentes. Le régime général prend en charge la majorité de la population : les travailleurs salariés ainsi que les travailleurs indépendants depuis le 1er janvier 2018. Le régime agricole prend en charge les exploitants et salariés agricoles. De nombreux régimes spéciaux, comme celui des marins, des mines, de la SNCF, de la RATP, d’EDF-GDF, de l’Assemblée nationale, du Sénat, des clercs et employés de notaires.

## Description des changements majeurs 
La méthode de collecte de données a évolué en mars 2021 : l’extraction et le traitement des données a été confié à la CNAM, ce qui a conduit à modifier le champ des effectifs suivis. Seuls les bénéficiaires du congé paternité relevant du régime général sont désormais pris en compte, et plus les assurés relevant de la mutualité sociale agricole (MSA) ou de la caisse de retraite et de prévoyance des clercs de notaire (CRPCEN).