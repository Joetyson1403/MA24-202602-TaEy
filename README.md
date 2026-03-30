# Othello Python

Projet de jeu Othello développé en Python avec les bibliothèques Pygame et Tkinter dans le cadre du module MA-24.

## Description du projet

Ce jeu propose une implémentation complète des règles classiques de l'Othello (aussi connu sous le nom de Reversi). Il a été structuré au travers d'une architecture MVC abstraite séparant strictement la logique métier (Core) des interfaces graphiques (Gfx).

## Fonctionnalités

* Menu principal en Tkinter : Saisie des pseudos, paramétrage complet de la partie.
* Plateau de jeu interactif en Pygame : Affichage dynamique de la grille avec ombres et reflets, prévisualisation des coups valides.
* Modes de jeu : Jouez à 2 (1v1 Humain) ou en solo contre l'ordinateur (vs IA).
* Thèmes personnalisables : Trois ambiances visuelles (Classique, Nuit, Néon) modifiables en direct.
* Ambiance sonore : Musique d'ambiance en boucle avec gestion de volume en temps réel sans quitter la partie.

## Installation

1. Assurez-vous d'avoir Python 3 d'installé sur votre machine.
2. Installez les dépendances requises via pip :
   pip install -r requirements.txt

## Exécution

Lancez le fichier d'entrée depuis votre terminal ou invite de commandes :
python main.py

## Structure des dossiers

Le projet s'organise autour d'une séparation claire :
* main.py : Le point d'entrée qui orchestre la communication entre le menu et le plateau de jeu.
* core/game_logic.py : Gère tout l'état du plateau de jeu Othello, la validation des coups, et l'algorithme décisionnel de l'IA.
* gfx/menu_tkinter.py : Fenêtre d'interface native Tkinter pour l'accueil.
* gfx/game_pygame.py : Fenêtre de jeu principale s'appuyant sur la rapidité d'affichage de Pygame.

## Développement

Auteurs : Eyuel Worku, Taveeporn Matta.
Code assisté par IA.
Readme rédigé par IA.
Musique : Eric Skiff - Underclocked (libre de droits).
