# gfx/menu_tkinter.py
# Fichier pour le menu principal Tkinter

import tkinter as tk

def show_menu():
    # Création de la fenêtre principale
    window = tk.Tk()
    window.title("Othello")
    window.geometry("400x350")
    window.configure(bg="#2b2b2b")
    
    # Titre du jeu
    title_label = tk.Label(window, text="Othello", font=("Helvetica", 28, "bold"),
                           fg="white", bg="#2b2b2b")
    title_label.pack(pady=(40, 5))
    
    # Variable pour savoir si on a cliqué sur Jouer
    start_game = False
    
    # Fonction appelée quand on clique sur Jouer
    def play_click():
        nonlocal start_game
        start_game = True
        window.destroy()
        
    # Bouton Jouer
    btn_play = tk.Button(window, text="Jouer", font=("Helvetica", 14, "bold"),
                         bg="#4CAF50", fg="white", width=15, height=1,
                         relief="flat", command=play_click)
    btn_play.pack(pady=10)
    
    # Bouton Quitter
    btn_quit = tk.Button(window, text="Quitter", font=("Helvetica", 12),
                         bg="#555555", fg="white", width=15, height=1,
                         relief="flat", command=window.destroy)
    btn_quit.pack(pady=10)
    
    # On lance la boucle Tkinter
    window.mainloop()
    
    # On renvoie True si le joueur a cliqué sur Jouer
    return start_game
