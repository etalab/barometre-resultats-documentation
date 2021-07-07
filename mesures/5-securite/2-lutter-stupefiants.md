# Lutter contre les stupéfiants 
## Description générale du jeu de données 
**Description** : L'action des forces de sécurité vise à réduire l’offre de stupéfiants par le démantèlement des réseaux et la neutralisation judiciaire des trafiquants, le démantèlement des circuits de blanchiment et en saisissant les avoirs criminels, et par l’interruption des routes de la drogue.

**Indicateur** : *Nombre d’amendes forfaitaires délictuelles dressées*.

L'indicateur recense le nombre d’amendes forfaitaires délictuelles verbalisées par les services de police et des unités de gendarmerie.
Après avoir été déployée progressivement à compter du 16 juin 2020 sur les ressorts des tribunaux judiciaires de Rennes, Reims, Créteil, Lille et Marseille, l’amende forfaitaire délictuelle pour usage de stupéfiants a été généralisée à l’ensemble du territoire national le 1er septembre 2020. 
Ce dispositif sanctionne l'usage de stupéfiants d'une amende forfaitaire de 200€ (montant minoré à 150 € et majoré à 450€ en fonction des délais de paiement). Elle est constatée par les forces de l’ordre par procès-verbal électronique. Si l’amende met fin aux poursuites judiciaires, elle entraîne néanmoins une inscription des faits au casier judiciaire, l’usage de stupéfiants étant un délit.

Production labellisée : Service statistique ministériel de la sécurité intérieure (SSMSI)

## Description du mode de production du jeu de données 
Nombre d’amendes forfaitaires délictuelles recensées en faits constatés par le code NATINF 180 au sein de l’index 57 dans l’état 4001. Cet indicateur est alimenté à partir des données fournies par l’agence nationale de traitement automatisé des infractions (ANTAI) sur la base de l’activité de verbalisation réalisée par les services de police et de gendarmerie.

Pour une amende dressée, il n’y a qu’un seul auteur associé. Dans le cas où plusieurs AFD sont dressées pour un même auteur au cours de la période considérée, une nouvelle procédure est bien créée à chaque fois, autant de fois que d’amendes dressées. 

Les données sur les AFD sont prises en compte dans l’état 4001 à la date de leur réception au service informatique du ministère de l’Intérieur, c’est-à-dire en général le lendemain de leur réception à l’ANTAI. Il peut néanmoins arriver exceptionnellement qu’elles soient réceptionnées avec quelques jours voire semaines de délai au service informatique du MI, et donc ne soient comptabilisées dans l’état 4001 qu’à ce moment-là.

## Description des métadonnées 
-	Fréquence de mise à jour : mensuelle
-	Couverture temporelle : depuis la création de l’AFD (juin 2020)
-	Couverture spatiale : France métropolitaine et Outre-mer
-	Granularité spatiale : nationale, régionale, départementale
-	Nature des données : données mensuelles non cumulées

Dans le cadre du baromètre des résultats, les données ont été décumulées afin d’afficher des valeurs mensuelles non-cumulées.

## Lexique des termes 
État 4001 : formulaire administratif utilisé par les services de police et les unités de gendarmerie des années 1970 aux années 2000 pour retracer leur activité judiciaire. Aujourd’hui, l’équivalent de l’état 4001 est reconstitué grâce à l’interrogation des logiciels d’enregistrement des procédures de la police nationale (LRPPN) et de la gendarmerie nationale (LRPGN).

NATINF (NATure d’INFraction) : la NATINF est la nomenclature des infractions créée par le ministère de la justice en 1978 pour les besoins de l'informatisation du casier judiciaire et des juridictions pénales. Elle recense la plupart des infractions pénales en vigueur ou abrogées, et évolue au gré des modifications législatives et réglementaires. Elle répond à un objectif de connaissance du droit pénal général et spécial en vigueur, et à un besoin de standardisation de la norme pénale pour la gestion informatique des procédures, de la constatation des infractions à l’exécution des sanctions. Elle permet aussi la production de statistiques relatives aux contentieux traités, aux sanctions prononcées et à leur évolution.

## Description des changements majeurs
L’amende forfaitaire délictuelle (AFD) pour usages de stupéfiants a été expérimentée sur 5 territoires pilotes à compter de juin 2020 puis généralisée depuis le 1er septembre 2020 à l’ensemble du territoire métropolitain et ultra-marin.