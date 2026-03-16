# main.py
# Point d'entrée principal du jeu Othello

from core.game_logic import GameLogic
from gfx.menu_tkinter import show_menu
from gfx.game_pygame import GameWindow

def main():
    print("Démarrage de Othello")
    
    # 1. Afficher le menu Tkinter
    start_game = show_menu()
    
    # Si le joueur a cliqué sur "Jouer"
    if start_game:
        # 2. Initialiser la logique (core)
        logic = GameLogic()
        
        # 3. Lancer la fenêtre de jeu Pygame (gfx)
        window = GameWindow(logic)
        window.main_loop()
    else:
        print("Fermeture du jeu")

if __name__ == "__main__":
    main()
