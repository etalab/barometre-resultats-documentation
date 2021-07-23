# Verdir le parc automobile
## Description générale du jeu de données 
**Action prioritaire** : une des actions de l’Etat en faveur du verdissement du parc automobile vise à soutenir le renouvellement du parc automobile et à aider les ménages et les professionnels à acquérir un véhicule peu polluant. Cette action repose notamment sur deux aides : le bonus écologique et la prime à la conversion. Elle nécessite aussi d’augmenter le nombre de points de recharge électrique sur le territoire.

**Indicateur 1** : *Nombre de primes à la conversion et de bonus écologiques*

Il s’agit de la somme :
-	du nombre de bonus accordés à des particuliers ou des personnes morales pour l’achat ou la location longue durée d’un véhicule électrique, hydrogène ou hybride rechargeable ;
-	et du nombre de primes accordées pour l’achat ou la location longue durée d’un véhicule éligible au dispositif, lorsqu’il s’accompagne de la mise au rebut d’un véhicule ancien polluant.

**Indicateur 2** : *Nombre de bornes de recharge pour véhicules électriques déployées*

L’indicateur mesure le nombre de points de recharge pour véhicules électriques et hybrides rechargeables ouverts au public sur le territoire français. Les points de recharge dédiés à une recharge résidentielle ou professionnelle sont exclus (on en compte environ 600 000 en France, chez les particuliers et dans les entreprises). Un point de recharge correspond à une interface associée à un emplacement de stationnement qui permet de recharger un seul véhicule à la fois.

## Description du mode de production du jeu de données 

**Indicateur 1** : *Nombre de primes à la conversion et de bonus écologiques*

Les données sont recueillies et transmises par l’Agence de services et de paiement (ASP), dans le cadre du traitement des dossiers de demandes de bonus et de primes à la conversion. L’ASP est l’opérateur de l’Etat chargé du recueil des demandes, de leurs traitements et du paiement des aides.

Les données sont collectées par l’ASP par l’intermédiaire d’une plateforme internet pour les demandes de particuliers, et par un extranet pour les demandes des professionnels
[primealaconversion.gouv.fr](https://www.primealaconversion.gouv.fr/)

**Indicateur 2** : *Nombre de bornes de recharge pour véhicules électriques déployées*

Les données sont fournies par Girève ([gireve.com](https://www.gireve.com)), plate-forme d’interopérabilité, de façon mensuelle. Elles proviennent des professionnels connectés à cette plateforme et des informations que Girève a pu collecter notamment celles transmises par les opérateurs et aménageurs d’infrastructures de recharge en open data sur le site [data.gouv.fr](https://data.gouv.fr), conformément au décret n°2017-26. 

Sur la base des jeux de données apportés par les aménageurs sur [data.gouv.fr](https://data.gouv.fr), Etalab consolide mensuellement un fichier de l’ensemble des données disponibles, mis lui-même en open data. Les données présentes sur [data.gouv.fr](https://data.gouv.fr) ne sont toutefois pas exhaustives car certains aménageurs peuvent omettre de déclarer ou de mettre à jour les informations les concernant.


## Description des métadonnées 

**Indicateur 1** : *Nombre de primes à la conversion et de bonus écologiques*

-	Fréquence de mise à jour : trimestrielle
-	Couverture temporelle :  depuis mars 2018
-	Couverture spatiale : France métropolitaine, Guadeloupe, Guyane, Martinique, Réunion, et Mayotte.
-	Granularité spatiale : nationale, régionale, départementale
-	Nature des données : valeurs trimestrielles non-cumulées

Les données sont transmises à un rythme trimestriel depuis 2018, à l’échelle départementale (incluant l’outre-mer). Les données ne sont pas cumulatives, il s’agit des dossiers acceptés dans la durée du trimestre correspondant.

**Indicateur 2** : *Nombre de bornes de recharge pour véhicules électriques déployées*

-	Fréquence de mise à jour : actuellement mensuelle. Les données historiques sont disponibles sur une base trimestrielle (avec une qualité inégale selon les points de recharge).
-	Couverture temporelle : depuis septembre 2019
-	Couverture spatiale : France métropolitaine, Guadeloupe, Guyane, Martinique et La Réunion.
-	Granularité spatiale : nationale, régionale, départementale
-	Nature des données : Il s’agit de données cumulatives, correspondant au nombre de points de charge ouverts au public sur le territoire français à un moment donné.

## Lexique des termes 
Bonus écologique : aide définie aux articles D. 251-1 et suivants du code de l’énergie, versée pour l’achat ou la location de longue durée d’un véhicule électrique, hydrogène ou hybride rechargeable répondant aux conditions d’éligibilité.

Prime à la conversion : aide définie aux articles D. 251-3 et suivants du code de l’énergie, versée pour l’achat ou la location de longue durée d’un véhicule peu polluant répondant aux conditions d’éligibilité, en échange de la mise au rebut d’un véhicule ancien éligible.

Point de recharge : interface associée à un emplacement de stationnement qui permet de recharger un seul véhicule électrique à la fois ;

Borne de recharge : appareil fixe raccordé à un point d'alimentation électrique, comprenant un ou plusieurs points de recharge et pouvant intégrer notamment des dispositifs de communication, de comptage, de contrôle ou de paiement ;

Station de recharge : zone comportant une borne de recharge associée à un ou des emplacements de stationnement ou un ensemble de bornes de recharge associées à des emplacements de stationnement, alimentée par un même point de livraison du réseau public de distribution d'électricité ou par une même installation locale de production ou de stockage d'énergie et exploitée par un seul opérateur ou groupement d'opérateurs ;

Point de recharge ouvert au public : point de recharge, exploité par un opérateur public ou privé, auquel les utilisateurs ont accès de façon non discriminatoire. L'accès non discriminatoire n'interdit pas d'imposer certaines conditions en termes d'autorisation, d'authentification, d'utilisation et de paiement ;

Plate-forme d’interopérabilité : opérateur qui fournit des services pour l'itinérance de la recharge en facilitant, sécurisant et optimisant les transactions et échanges de données entre les opérateurs d'infrastructure de recharge et les opérateurs de mobilité.