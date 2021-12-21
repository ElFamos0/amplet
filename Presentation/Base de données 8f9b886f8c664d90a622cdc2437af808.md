# Base de données

# Table utilisateur :

| Identifiant (clé primaire) |
| --- |
| Nom |
| Prénom |
| Email |
| Mdp |
| Marchant (oui / non) |
| Points |

# Table Course :

| Identifiant Course (clé primaire) |
| --- |
| Identifiant Coursier |
| Date de début |
| Date de fin |
| Nombre de places proposées |
| Nombre de places réservées |

# Table Point

| Identifiant Point (clé primaire) |
| --- |
| Identifiant Trajet (clé secondaire) |
| Latitude |
| Longitude |
| Heure de passage |
| Ordre |

# Table Acheteur

| Identifiant Transaction (clé primaire)  |
| --- |
| Identifiant utilisateur (clé secondaire) |
| Identifiant course (clé secondaire) |
| Validé (oui / non) |

# Table Produits

| Identifiant Produit (clé primaire) |
| --- |
| Nom |
| Prix |

# Table Achat

| Identifiant transaction (clé primaire) |
| --- |
| Identifiant produit (clé primaire) |
| Prix à l'achat |

# Table Navette

| Identifiant Navette |
| --- |
| Date Départ |
| Date Arrivée |
| Marchant 1 |
| Marchant 2 |
| Marchant 3 |
| Marchant 4 |
| Marchant 5 |
