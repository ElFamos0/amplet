# Sixième CR

31/12/2021: December 31, 2021

## Présents :

- Malo
- Tristan
- Jules
- LV

# Ordre du jour :

- Point sur les jalons
- Répartition de ceux qui restent
- Point sur l’avancement du rapport

## Point sur jalons :

**Consultation / Inscription sur les Amplet des particuliers :** Mise en forme fonctionnel du système de consultation et de recherche d’amplets, inscriptions sur les amplets en forme (à relier à la base de donnée)

**Création d’amplets particuliers :** il reste à lier à la BD le post d’une Amplet pour les stocker, et la possibilité d’accepter ou non un participant.

## Jalons restants :

Il reste 1.4 que Jules récupère car c’est très lié à 1.3 qu’il a réalisé.

Les adresses précises des utilisateurs ne sont pas stockées, seulement les codes postaux, on retire donc les fonctionnalités Distance maximale (1.5.2) et le tri des Amplet par proximité (qui reste à l’état d’ébauche)

Pour les plus courts trajets l’équipe est d’accord pour faire une recherche exhaustive tant que le nombre de magasins ne dépasse pas 6. → 60 chemins

LV : Page commande à faire

**Système de vote :**

Jules: A un instant T, faire une fonction qui calcule à partir d’un id_amp (une navette dont on ferme le vote) :

- la liste des magasins choisis
- la liste des participants (et leurs produits) choisis
- Actualise le score des magasins

Malo : Link l’envoi de la liste à la base de donnée (user mis ‘en attente’ dans participant_amp)

LV : affiche à l’utilisateur un retour sur quels produits vont lui être servis ou non sur la page commande

Tristan : Doit faire, sur le serveur, un système qui permet de fermer les votes d’une navette donnée à une date donnée et de lancer le processus de ‘fin de vote’.

## Rapport :

Tristan et Malo ont avancé sur la partie technique du rapport notamment la section performance et test mais également la partie développement. LV va s’occuper de la partie gestion de projet et de corriger les fautes.

La matrice RACI a été actualisée et le schéma E/A aussi. Il faudra régler le problème entre adresse et coordonnées pour qu’elle soit à nouveau en 2NF.
