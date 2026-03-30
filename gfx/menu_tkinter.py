import tkinter as tk
from tkinter import ttk, messagebox

def draw_logo(canvas):
    # Dessine un pion noir et un pion blanc pour le logo
    canvas.create_oval(10, 10, 50, 50, fill="#111", outline="#4CAF50", width=2)
    canvas.create_oval(30, 10, 70, 50, fill="#eee", outline="#4CAF50", width=2)

def show_menu():
    window = tk.Tk()
    window.title("Othello - Menu Principal")
    window.geometry("450x700")
    window.configure(bg="#1E1E24")
    window.resizable(False, False)
    
    # Configuration du thème
    style = ttk.Style(window)
    if "clam" in style.theme_names():
        style.theme_use("clam")
        
    BG = "#1E1E24"
    FG = "#FFFFFF"
    ACCENT = "#4CAF50"
    PANEL = "#2B2B36"
    
    style.configure("TFrame", background=BG)
    style.configure("Panel.TFrame", background=PANEL)
    
    style.configure("TLabel", background=BG, foreground=FG, font=("Segoe UI", 11))
    style.configure("Panel.TLabel", background=PANEL, foreground=FG, font=("Segoe UI", 11))
    style.configure("Title.TLabel", background=BG, foreground=ACCENT, font=("Segoe UI", 28, "bold"))
    
    style.configure("TRadiobutton", background=PANEL, foreground=FG, font=("Segoe UI", 11))
    style.map("TRadiobutton", 
              background=[("active", PANEL)], 
              indicatorcolor=[('selected', ACCENT), ('!selected', BG)])
              
    style.configure("TScale", background=PANEL, troughcolor=BG)
    
    style.configure("TButton", font=("Segoe UI", 12), padding=8)
    style.configure("Play.TButton", font=("Segoe UI", 14, "bold"), background=ACCENT, foreground="white")
    style.map("Play.TButton", background=[("active", "#45a049")])
    
    style.configure("Action.TButton", font=("Segoe UI", 11), background="#3A3A4A", foreground="white")
    style.map("Action.TButton", background=[("active", "#4A4A5A")])
    
    style.configure("Quit.TButton", font=("Segoe UI", 11), background="#d32f2f", foreground="white")
    style.map("Quit.TButton", background=[("active", "#b71c1c")])
    
    # Variables pour les choix
    mode_var = tk.StringVar(value="1v1")
    theme_var = tk.StringVar(value="classique")
    volume_var = tk.DoubleVar(value=0.5)
    
    start_game = False
    p1_name = "Noir"
    p2_name = "Blanc"
    is_ai = False
    selected_theme = "classique"
    volume_val = 0.5
    
    # Header
    header_frame = ttk.Frame(window)
    header_frame.pack(pady=(25, 15))
    
    canvas = tk.Canvas(header_frame, width=80, height=60, bg=BG, highlightthickness=0)
    draw_logo(canvas)
    canvas.grid(row=0, column=0, padx=5)
    
    ttk.Label(header_frame, text="OTHELLO", style="Title.TLabel").grid(row=0, column=1, padx=5)
    
    # Conteneur principal
    main_frame = ttk.Frame(window)
    main_frame.pack(fill="x", padx=30, pady=10)
    
    # --- Mode de jeu ---
    mode_frame = ttk.Frame(main_frame, style="Panel.TFrame")
    mode_frame.pack(fill="x", pady=5)
    ttk.Label(mode_frame, text="Mode de jeu", style="Panel.TLabel", font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=15, pady=(10, 5))
    ttk.Radiobutton(mode_frame, text="1 vs 1 (Humain)", variable=mode_var, value="1v1").pack(anchor="w", padx=20, pady=2)
    ttk.Radiobutton(mode_frame, text="vs IA (Ordinateur)", variable=mode_var, value="ia").pack(anchor="w", padx=20, pady=(2, 10))
    
    # --- Noms des joueurs ---
    names_frame = ttk.Frame(main_frame, style="Panel.TFrame")
    names_frame.pack(fill="x", pady=5)
    ttk.Label(names_frame, text="Noms des joueurs", style="Panel.TLabel", font=("Segoe UI", 12, "bold")).grid(row=0, column=0, columnspan=2, sticky="w", padx=15, pady=(10, 5))
    
    ttk.Label(names_frame, text="Joueur Noir :", style="Panel.TLabel").grid(row=1, column=0, sticky="w", padx=20, pady=5)
    entry_p1 = tk.Entry(names_frame, width=15, font=("Segoe UI", 11), bg=BG, fg=FG, insertbackground=FG, relief="flat", highlightbackground=PANEL, highlightcolor=ACCENT, highlightthickness=1)
    entry_p1.insert(0, "Noir")
    entry_p1.grid(row=1, column=1, sticky="e", padx=20, pady=5)
    
    ttk.Label(names_frame, text="Joueur Blanc :", style="Panel.TLabel").grid(row=2, column=0, sticky="w", padx=20, pady=(5, 10))
    entry_p2 = tk.Entry(names_frame, width=15, font=("Segoe UI", 11), bg=BG, fg=FG, insertbackground=FG, relief="flat", highlightbackground=PANEL, highlightcolor=ACCENT, highlightthickness=1)
    entry_p2.insert(0, "Blanc")
    entry_p2.grid(row=2, column=1, sticky="e", padx=20, pady=(5, 10))
    
    # --- Volume ---
    vol_frame = ttk.Frame(main_frame, style="Panel.TFrame")
    vol_frame.pack(fill="x", pady=5)
    ttk.Label(vol_frame, text="Volume Musique", style="Panel.TLabel", font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=15, pady=(10, 0))
    ttk.Scale(vol_frame, variable=volume_var, from_=0.0, to=1.0, orient="horizontal", value=0.5).pack(fill="x", padx=20, pady=(5, 15))

    def play_click():
        nonlocal start_game, p1_name, p2_name, is_ai, selected_theme, volume_val
        start_game = True
        selected_theme = theme_var.get()
        is_ai = mode_var.get() == "ia"
        volume_val = volume_var.get()
        
        name1 = entry_p1.get().strip()
        name2 = entry_p2.get().strip()
        if name1: p1_name = name1
        if is_ai: p2_name = "Ordinateur (IA)"
        elif name2: p2_name = name2
        
        window.destroy()

    def show_rules():
        rules_txt = ("1. Tour par tour, placez un pion de votre couleur.\n"
                     "2. Encadrez les pions adverses pour les retourner.\n"
                     "3. Passez votre tour si aucun coup n'est possible.\n"
                     "4. Fin quand le plateau est plein ou blocage total.\n"
                     "5. Le gagnant est celui qui a le plus de pions.")
        messagebox.showinfo("Règles du jeu - Othello", rules_txt)

    def show_themes():
        tw = tk.Toplevel(window)
        tw.title("Thèmes")
        tw.geometry("260x240")
        tw.configure(bg=BG)
        
        tw.grab_set() # Focus modal
        
        ttk.Label(tw, text="Choix du thème", font=("Segoe UI", 14, "bold"), foreground=ACCENT).pack(pady=15)
        ttk.Radiobutton(tw, text="Classique", variable=theme_var, value="classique", style="TRadiobutton").pack(anchor="w", padx=40, pady=5)
        ttk.Radiobutton(tw, text="Nuit", variable=theme_var, value="nuit", style="TRadiobutton").pack(anchor="w", padx=40, pady=5)
        ttk.Radiobutton(tw, text="Néon", variable=theme_var, value="neon", style="TRadiobutton").pack(anchor="w", padx=40, pady=5)
        
        ttk.Button(tw, text="Valider", command=tw.destroy, style="Play.TButton").pack(pady=15)

    # --- Actions ---
    action_frame = ttk.Frame(window)
    action_frame.pack(fill="x", padx=30, pady=10)
    
    ttk.Button(action_frame, text="JOUER", style="Play.TButton", command=play_click).pack(fill="x", pady=5)
    ttk.Button(action_frame, text="Règles", style="Action.TButton", command=show_rules).pack(fill="x", pady=3)
    ttk.Button(action_frame, text="Thèmes", style="Action.TButton", command=show_themes).pack(fill="x", pady=3)
    ttk.Button(action_frame, text="Quitter", style="Quit.TButton", command=window.destroy).pack(fill="x", pady=(15, 0))

    window.mainloop()
    return start_game, p1_name, p2_name, is_ai, selected_theme, volume_val
