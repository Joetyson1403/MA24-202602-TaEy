# gfx/game_pygame.py
# Eyuel Worku, Taveeporn Matta
# MA_24_Othello
# Fichier pour l'affichage du plateau avec Pygame
 
import pygame
 
# Couleurs de base pour Othello
BOARD_GREEN = (34, 139, 34)  # Vert pour le fond
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0) # Lignes de séparation de la grille
HINT_COLOR = (0, 180, 0) # Couleur pour afficher les coups valides
GRAY = (50, 50, 50) # Couleur pour la barre de score
 
class GameWindow:
    def __init__(self, game_logic):
        self.game_logic = game_logic
       
        # Dimensions de la fenêtre et des cases
        self.cell_size = 75 # Pixels par case
        self.width = self.cell_size * 8
        self.board_height = self.cell_size * 8
        self.score_height = 40 # Hauteur de la barre de score en bas
        self.height = self.board_height + self.score_height
        self.game_over = False
 
    def draw_board(self, screen):
        # 1. Remplissage du fond de l'écran
        screen.fill(BOARD_GREEN)
       
        # 2. Dessin des lignes de la grille 8x8
        for i in range(9): # Il faut 9 lignes pour faire 8 cases
            # Lignes horizontales
            pygame.draw.line(screen, LINE_COLOR, (0, i * self.cell_size), (self.width, i * self.cell_size), 2)
            # Lignes verticales
            pygame.draw.line(screen, LINE_COLOR, (i * self.cell_size, 0), (i * self.cell_size, self.board_height), 2)
 
        # 3. Affichage des coups valides pour le joueur courant (petits ronds verts)
        if not self.game_over:
            valid_moves = self.game_logic.get_valid_moves(self.game_logic.current_player)
            for (row, col) in valid_moves:
                cx = col * self.cell_size + self.cell_size // 2
                cy = row * self.cell_size + self.cell_size // 2
                pygame.draw.circle(screen, HINT_COLOR, (cx, cy), 10)
           
        # 4. Dessin des pions en lisant la grille de la logique de jeu
        for row in range(8):
            for col in range(8):
                cell_value = self.game_logic.board.grid[row][col]
               
                # Calcul du centre de la case pour dessiner le cercle
                center_x = col * self.cell_size + self.cell_size // 2
                center_y = row * self.cell_size + self.cell_size // 2
                radius = self.cell_size // 2 - 5 # Un peu plus petit que la case
               
                if cell_value == 1:
                    # Joueur 1 = Noir
                    pygame.draw.circle(screen, BLACK, (center_x, center_y), radius)
                elif cell_value == 2:
                    # Joueur 2 = Blanc
                    pygame.draw.circle(screen, WHITE, (center_x, center_y), radius)
 
    def draw_score(self, screen):
        # Barre de score en bas de la fenêtre
        pygame.draw.rect(screen, GRAY, (0, self.board_height, self.width, self.score_height))
 
        font = pygame.font.Font(None, 30)
        score_black, score_white = self.game_logic.get_score()
 
        # Texte du score avec le joueur courant
        if self.game_over:
            if score_black > score_white:
                text = f"Noir gagne ! ( Noir: {score_black}  -  Blanc: {score_white} )"
            elif score_white > score_black:
                text = f"Blanc gagne ! ( Noir: {score_black}  -  Blanc: {score_white} )"
            else:
                text = f"Egalite ! ( Noir: {score_black}  -  Blanc: {score_white} )"
        else:
            player_name = "Noir" if self.game_logic.current_player == 1 else "Blanc"
            text = f"Tour: {player_name}   |   Noir: {score_black}  -  Blanc: {score_white}"
 
        score_surface = font.render(text, True, WHITE)
        # On centre le texte dans la barre
        text_x = (self.width - score_surface.get_width()) // 2
        text_y = self.board_height + (self.score_height - score_surface.get_height()) // 2
        screen.blit(score_surface, (text_x, text_y))
 
    def main_loop(self):
        # Initialisation obligatoire de Pygame
        pygame.init()
       
        # Création de la fenêtre (plateau + barre de score)
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Othello - Jeu")
       
        running = True
        # Boucle principale du jeu
        while running:
            # Gestion des événements (clics, clavier, fermeture de fenêtre)
            for event in pygame.event.get():
                # Si le joueur clique sur la croix de la fenêtre
                if event.type == pygame.QUIT:
                    running = False
 
                # Si le joueur clique sur le plateau (et que la partie n'est pas finie)
                elif event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                    mouse_x, mouse_y = event.pos
                    # Conversion des pixels en case (row, col)
                    col = mouse_x // self.cell_size
                    row = mouse_y // self.cell_size
                    # On essaie de jouer le coup (la logique vérifie si c'est valide)
                    self.game_logic.play_move(row, col)
 
                    # Vérifier si la partie est terminée après le coup
                    if self.game_logic.is_game_over():
                        self.game_over = True
           
            # Dessin du plateau, des pions et du score à chaque frame
            self.draw_board(screen)
            self.draw_score(screen)
           
            # Mise à jour de l'écran
            pygame.display.flip()
           
        # Fermeture propre de Pygame
        pygame.quit()
 