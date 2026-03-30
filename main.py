# main.py
# Point d'entrée principal du jeu Othello

from core.game_logic import GameLogic
from gfx.menu_tkinter import show_menu
from gfx.game_pygame import GameWindow

def main():
    print("Démarrage de Othello")
    
    # Boucle principale d'application pour gérer le retour au menu
    while True:
        # 1. Afficher le menu Tkinter
        result = show_menu()
        
        # Handling window closing without playing
        if len(result) == 6:
            start_game, p1_name, p2_name, is_ai, theme, volume = result
        else:
            break # Application fermée depuis le menu
        
        # Si le joueur a cliqué sur "Jouer"
        if start_game:
            # 2. Initialiser la logique (core)
            logic = GameLogic()
            
            # 3. Lancer la fenêtre de jeu Pygame (gfx)
            window = GameWindow(logic, p1_name, p2_name, is_ai, theme, volume)
            action = window.main_loop() # Attend que pygame se termine
            if action == "quit":
                print("Fermeture du jeu")
                break
            # si action == "menu", la boucle recommence et réaffiche show_menu()
        else:
            print("Fermeture du jeu")
            break

if __name__ == "__main__":
    main()
