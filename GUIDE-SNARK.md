# Preuves SNARK

## Circuit et witness

Distinguer entrées publiques, valeurs privées, contraintes et conversions. Une propriété métier absente du circuit ne sera pas garantie par une preuve pourtant valide.

## Paramètres

Identifier le SRS éventuel, la cérémonie, la proving key et la verification key. Documenter les hypothèses de confiance et les conséquences d’une mauvaise génération des paramètres.

## Transcript

Suivre encodage, challenges, engagements et contrôles algébriques ou de pairing. Les erreurs d’encodage et de domaine peuvent modifier la propriété réellement prouvée.

## Limites

Une preuve atteste le circuit exprimé, pas les propriétés externes au circuit, la disponibilité du service ou la sûreté de l’intégration EVM.
