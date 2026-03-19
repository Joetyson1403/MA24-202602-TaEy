# core/game_logic.py
# Eyuel Worku, Taveeporn Matta
# MA_24_Othello
# Fichier pour la logique du jeu Othello
 
from .board import Board
 
class GameLogic:
    def __init__(self):
        # Initialisation de l'objet plateau pour la lecture par Pygame
        self.board = Board()
        # Le joueur 1 (Noir) commence toujours
        self.current_player = 1
 
    def get_valid_moves(self, player):
        # On cherche toutes les cases où le joueur peut poser un pion
        # Un coup est valide s'il encadre au moins un pion adverse
        valid_moves = []
        opponent = 2 if player == 1 else 1

        for row in range(8):
            for col in range(8):
                # La case doit être vide
                if self.board.grid[row][col] != 0:
                    continue

                # On vérifie dans les 8 directions autour de la case
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
                    r, c = row + dr, col + dc
                    found_opponent = False

                    # On avance tant qu'on trouve des pions adverses
                    while 0 <= r < 8 and 0 <= c < 8 and self.board.grid[r][c] == opponent:
                        found_opponent = True
                        r += dr
                        c += dc

                    # Si on a dépassé un ou plusieurs adverses et qu'on tombe sur un allié -> coup valide
                    if found_opponent and 0 <= r < 8 and 0 <= c < 8 and self.board.grid[r][c] == player:
                        valid_moves.append((row, col))
                        break  # No need to check other directions

        return valid_moves

    def play_move(self, row, col):
        # On vérifie si le coup est dans la liste des coups valides
        if (row, col) not in self.get_valid_moves(self.current_player):
            return False

        opponent = 2 if self.current_player == 1 else 1

        # On pose le pion du joueur courant
        self.board.grid[row][col] = self.current_player

        # On retourne les pions adverses dans les 8 directions
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
            pieces_to_flip = []
            r, c = row + dr, col + dc

            while 0 <= r < 8 and 0 <= c < 8 and self.board.grid[r][c] == opponent:
                pieces_to_flip.append((r, c))
                r += dr
                c += dc

            # On retourne seulement si on termine sur un pion allié
            if pieces_to_flip and 0 <= r < 8 and 0 <= c < 8 and self.board.grid[r][c] == self.current_player:
                for pr, pc in pieces_to_flip:
                    self.board.grid[pr][pc] = self.current_player

        # On passe au joueur suivant
        self.current_player = opponent

        return True