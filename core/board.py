# core/board.py
# Eyuel Worku, Taveeporn Matta
# MA_24_Othello
# Fichier pour modéliser le plateau 8x8
 
class Board:
    def __init__(self):
        self.size = 8
        # Initialisation de la grille avec des 0 (cases vides)
        self.grid = [[0 for _ in range(self.size)] for _ in range(self.size)]
       
        # Placement initial des 4 pions au centre de la grille 8x8
        # 1 = Noir, 2 = Blanc
        self.grid[3][3] = 2
        self.grid[3][4] = 1
        self.grid[4][3] = 1
        self.grid[4][4] = 2
 
 