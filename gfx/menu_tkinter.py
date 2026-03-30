# gfx/menu_tkinter.py
# Fichier pour le menu principal Tkinter

import tkinter as tk
from tkinter import messagebox

def show_menu():
    # Création de la fenêtre principale
    window = tk.Tk()
    window.title("Othello")
    window.geometry("450x450")
    window.configure(bg="#2b2b2b")
    
    # Titre du jeu
    title_label = tk.Label(window, text="Othello", font=("Helvetica", 28, "bold"),
                           fg="white", bg="#2b2b2b")
    title_label.pack(pady=(20, 10))
    
    # Champs pour les noms des joueurs
    frame_names = tk.Frame(window, bg="#2b2b2b")
    frame_names.pack(pady=10)
    
    lbl_p1 = tk.Label(frame_names, text="Joueur Noir :", fg="white", bg="#2b2b2b", font=("Helvetica", 12))
    lbl_p1.grid(row=0, column=0, padx=5, pady=5)
    entry_p1 = tk.Entry(frame_names, font=("Helvetica", 12), width=15)
    entry_p1.insert(0, "Noir")
    entry_p1.grid(row=0, column=1, padx=5, pady=5)
    
    lbl_p2 = tk.Label(frame_names, text="Joueur Blanc :", fg="white", bg="#2b2b2b", font=("Helvetica", 12))
    lbl_p2.grid(row=1, column=0, padx=5, pady=5)
    entry_p2 = tk.Entry(frame_names, font=("Helvetica", 12), width=15)
    entry_p2.insert(0, "Blanc")
    entry_p2.grid(row=1, column=1, padx=5, pady=5)
    
    start_game = False
    p1_name = "Noir"
    p2_name = "Blanc"
    
    # Fonction appelée quand on clique sur Jouer
    def play_click():
        nonlocal start_game, p1_name, p2_name
        start_game = True
        name1 = entry_p1.get().strip()
        name2 = entry_p2.get().strip()
        if name1: p1_name = name1
        if name2: p2_name = name2
        window.destroy()

    def show_rules():
        rules_text = (
            "Règles d'Othello :\n\n"
            "1. Le jeu se déroule sur un plateau 8x8.\n"
            "2. À son tour, un joueur doit poser un pion de sa couleur sur une case vide.\n"
            "3. Le coup doit encadrer au moins un pion adverse entre le pion posé et "
            "un autre pion de sa couleur (horizontalement, verticalement ou diagonalement).\n"
            "4. Les pions adverses encadrés sont retournés.\n"
            "5. Si un joueur ne peut pas jouer, il passe son tour.\n"
            "6. La partie s'arrête quand aucun joueur ne peut plus jouer.\n"
            "7. Le gagnant est celui qui a le plus de pions de sa couleur."
        )
        messagebox.showinfo("Règles du jeu", rules_text)

    def show_themes():
        messagebox.showinfo("Thèmes", "La sélection des thèmes sera ajoutée plus tard.")
        
    # Boutons du menu
    btn_play = tk.Button(window, text="Jouer", font=("Helvetica", 14, "bold"),
                         bg="#4CAF50", fg="white", width=15, relief="flat", command=play_click)
    btn_play.pack(pady=5)
    
    btn_rules = tk.Button(window, text="Règles", font=("Helvetica", 12),
                          bg="#2196F3", fg="white", width=15, relief="flat", command=show_rules)
    btn_rules.pack(pady=5)
    
    btn_themes = tk.Button(window, text="Thèmes", font=("Helvetica", 12),
                           bg="#FF9800", fg="white", width=15, relief="flat", command=show_themes)
    btn_themes.pack(pady=5)
    
    btn_quit = tk.Button(window, text="Quitter", font=("Helvetica", 12),
                         bg="#555555", fg="white", width=15, relief="flat", command=window.destroy)
    btn_quit.pack(pady=5)
    
    # On lance la boucle Tkinter
    window.mainloop()
    
    # On renvoie les informations
    return start_game, p1_name, p2_name
