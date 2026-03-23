# Journal d'utilisation de l'IA

## 1. Initialisation de l'architecture du projet

*   **Description de la problématique** : Besoin d'un squelette de départ propre pour faire le premier commit sur GitHub et répartir le travail.
*   **Prompt effectué** : 
    1. « *On doit programmer un jeu othello avec pygame et tkinter [...] Évaluation : Séparation du main, gfx et core. Peux tu nous aiguiller pour le projet* »
    2. « *Qu'est-ce que Core, Gfx et Main ?* »
    3. « *Peux tu faire le squelette de base pour initialiser le projet* »
*   **Réponse IA** : 
    *   Explication détaillée du modèle d'architecture (MVC Modèle-Vue-Contrôleur) avec les responsabilités de chaque dossier (`core` = règles du jeu pures sans affichage, `gfx` = fonctions de dessin et menus, `main.py` = point d'entrée qui relie les deux).
    *   Génération de l'arborescence des dossiers et des fichiers squelettes de base minimaux (contenant uniquement les classes et les structures vides) : `main.py`, `requirements.txt`, et les dossiers `core/` et `gfx/` pour amorcer proprement le dépôt GitHub.

## 2. Définition des User Stories

*   **Description de la problématique** : Nous avions listé toutes nos envies pour le jeu (poser un pion, retourner les pions, les scores, mais aussi la musique, le choix du thème, affronter l'IA ou un autre joueur, et un menu complet). Nous avions besoin de formater correctement cette liste pour l'évaluation.
*   **Prompt effectué** : 
    1. « *Voici tout ce qu'on veut pour notre jeu : un menu principal avec la possibilité d'entrer nos noms, pouvoir lire les règles du jeu, choisir entre jouer contre l'IA ou contre un ami en local. Pendant le jeu, on veut poser des pions qui respectent les règles d'Othello, que le score s'affiche, qu'il y ait de la musique en fond et qu'on puisse choisir un thème de couleur. Peux-tu mettre tout ça au propre sous forme de 'User Stories' pour notre rendu ?* »
*   **Réponse IA** : 
    *   Structuration, mise au propre et ajout de toutes ces fonctionnalités dans le document `user_stories.md` sous le format attendu ("En tant que joueur, je veux...").
    *   Mise à jour du squelette des tâches (`task.md`) pour inclure l'intégration de ces éléments dans les bons modules (Tkinter pour les menus/noms/règles, Pygame pour le plateau/audio, logique CPU pour l'IA).

## 3. Amélioration du design graphique (Tkinter et Pygame)

*   **Description de la problématique** : Le jeu initial était visuellement très basique (carrés unis, pas d'ombres, menu Tkinter par défaut) .
*   **Prompt effectué** : 
    1. « *Comment faire des pions arrondis avec un peu de relief ?* »
*   **Réponse IA** : 
    *   Modification de `game_pygame.py` pour utiliser `pygame.draw.circle` avec des superpositions simples pour créer un effet d'ombre et de reflet sur les pions, sans utiliser d'images externes complexes.
    *   Nettoyage et simplification des commentaires pour bien expliquer chaque étape du dessin (plateau, lignes, indicateurs de coups valides).
