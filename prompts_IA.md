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
    * « *Comment faire des pions ronds avec un peu de relief ?* »
*   **Réponse IA** : 
    *   Modification de `game_pygame.py` pour utiliser `pygame.draw.circle` avec des superpositions simples pour créer un effet d'ombre et de reflet sur les pions, sans utiliser d'images externes complexes.

## 4. Amélioration du menu et gestion du volume

*   **Description de la problématique** : Le menu Tkinter était très basique, il manquait le choix du thème, la gestion du volume, l'option de retour menu depuis le jeu, et le volume en jeu.
*   **Prompt effectué** : 
    1. « *Peux-tu améliorer le menu Tkinter pour ajouter un curseur de volume et un bouton pour retourner au menu depuis la fenêtre de jeu ?* »
    2. « *Comment faire pour que le volume soit pris en compte dans le jeu Pygame ?* »
    3. « *Mets l'option volume musique aussi quand on joue* »
*   **Réponse IA** : 
    *   Modification de `gfx/menu_tkinter.py` pour ajouter un `tk.Scale` pour le volume.
    *   Modification de `gfx/game_pygame.py` pour ajouter des boutons `+` et `-` de volume, un bouton "Retour Menu" sur le panneau d'information, et gestion de ces clics dynamiquement.
    *   Refonte de la boucle principale dans `main.py` pour gérer le retour d'état (Action `menu` vs `quit`), et boucler sur `show_menu()`.

## 5. Intégration du Mode IA et Refonte Design du Menu

*   **Description de la problématique** : Demande d'ajouter la possibilité de jouer contre une IA (Intelligence Artificielle) et demande de refonte esthétique complète du menu principal.
*   **Prompt effectué** : 
    1. « *Peux tu m'aider à ajouter l'option de jouer contre une ia et aussi l'amélioration du menu* »
*   **Réponse IA** : 
    *   Dans `core/game_logic.py`, ajout de `get_ai_move` : l'ordinateur fait la liste des coups valides et sélectionne un coin s'il en a l'opportunité, sinon il choisit un coup aléatoire.
    *   Dans `gfx/game_pygame.py`, automatisation du tour de Blanc si l'option "vs IA" est cochée (le jeu bloque la souris pendant 600ms pour simuler le délai de "réflexion").
    *   Refonte totale de `gfx/menu_tkinter.py` avec `ttk`, implémentation d'un thème sombre moderne ("clam"), polices lisses Segoe UI, mise en forme sous forme de "cartes" et ajout d'un petit logo.