# Preuves STARK

## Trace et AIR

Le calcul est représenté par une trace soumise à des contraintes algébriques. L’analyse doit identifier colonnes, transitions, état initial et conditions de terminaison.

## Engagements

Le prouveur engage la trace ou ses évaluations dérivées. Le vérificateur doit s’assurer que les ouvertures, les défis et les contrôles portent sur le même objet engagé.

## FRI et transcript

FRI vérifie récursivement une propriété de faible degré. Le transcript Fiat-Shamir lie chaque défi aux engagements précédents ; son ordre exact est une propriété de sécurité.

## Revue

Relier ces étapes au code, aux paramètres et aux erreurs. Coût de vérification et taille de preuve ne suffisent pas à établir la sécurité globale.
