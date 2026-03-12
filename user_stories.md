# User Stories - Projet Othello

Voici la liste des fonctionnalités du point de vue de l'utilisateur.

## Sprint 1 : Base du jeu
- [ ] En tant que joueur, je veux voir l'interface (Tkinter) s'ouvrir lorsque je lance le jeu, pour pouvoir démarrer une partie.
- [ ] En tant que joueur, je veux pouvoir cliquer sur un bouton "Jouer" dans le menu, pour lancer le plateau Pygame.
- [ ] En tant que joueur, je veux voir un damier 8x8 avec les 4 pions de départ (2 noirs, 2 blancs) au centre, pour commencer à jouer.

## Sprint 2 : Logique principale
- [ ] En tant que joueur Noir (premier à jouer), je veux pouvoir cliquer sur une case vide pour poser mon pion.
- [ ] En tant que joueur, je veux que mon clic ne soit accepté que s'il encadre les pions adverses selon les règles d'Othello, pour éviter de tricher.
- [ ] En tant que joueur, je veux voir les pions adverses encadrés se retourner et prendre ma couleur après mon coup.
- [ ] En tant que joueur, je veux que le tour passe automatiquement à mon adversaire après un coup valide.

## Sprint 3 : Fin de partie 
- [ ] En tant que joueur, je veux que le score (nombre de pions sur le plateau) soit mis à exposé en temps réel à chaque coup.
- [ ] En tant que joueur, si je n'ai aucun coup valide, je veux que mon tour soit passé automatiquement.
- [ ] En tant que joueur, je veux que la partie s'arrête lorsqu'il n'y a plus de coups possibles pour aucun joueur, pour connaître le vainqueur.
- [ ] En tant que joueur, je veux voir un message m'indiquant qui a gagné, pour célébrer la victoire.

## Sprint 4 : Nouvelles Fonctionnalités & Bonus
- [ ] **Menu principal** : En tant que joueur, je veux arriver sur un écran d'accueil complet avec des options claires (Jouer, Règles, Thèmes, Quitter).
- [ ] **Noms des joueurs** : En tant que joueur, je veux pouvoir saisir mon pseudo dans le menu pour qu'il s'affiche pendant la partie.
- [ ] **Section règles du jeu** : En tant que nouveau joueur, je veux pouvoir lire les règles du jeu d'Othello depuis le menu principal pour comprendre comment jouer.
- [ ] **Musique d'ambiance** : En tant que joueur, je veux entendre une musique de fond pendant ma partie pour une meilleure immersion.
- [ ] **Thèmes de couleurs** : En tant que joueur, je veux pouvoir choisir entre plusieurs thèmes visuels (ex: Classique, Nuit, Néon) pour personnaliser mon expérience.
- [ ] **Mode 2 Joueurs (Local)** : En tant que joueur, je veux pouvoir sélectionner un mode "Joueur contre Joueur" pour affronter un ami sur le même écran.
- [ ] **Mode vs IA** : En tant que joueur solo, je veux pouvoir affronter une Intelligence Artificielle (ordinateur) au lieu d'un autre joueur humain.
