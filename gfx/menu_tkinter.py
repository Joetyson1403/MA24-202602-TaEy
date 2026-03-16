# gfx/menu_tkinter.py
# Fichier pour le menu principal Tkinter

import tkinter as tk

def show_menu():
    # Création de la fenêtre principale
    window = tk.Tk()
    window.title("Othello")
    window.geometry("400x300")
    
    # Titre du jeu
    title_label = tk.Label(window, text="Othello", font=("Helvetica", 24))
    title_label.pack(pady=30)
    
    # Variable pour savoir si on a cliqué sur Jouer
    start_game = False
    
    # Fonction appelée quand on clique sur Jouer
    def play_click():
        nonlocal start_game
        start_game = True
        window.destroy() # On ferme le menu pour lancer le jeu
        
    # Bouton Jouer
    btn_play = tk.Button(window, text="Jouer", font=("Helvetica", 14), command=play_click)
    btn_play.pack(pady=20)
    
    # Bouton Quitter
    btn_quit = tk.Button(window, text="Quitter", font=("Helvetica", 14), command=window.destroy)
    btn_quit.pack(pady=10)
    
    # On lance la boucle de la fenêtre Tkinter
    window.mainloop()
    
    # Si on a cliqué sur Jouer, on renvoie True au main.py pour qu'il lance la suite
    return start_game
