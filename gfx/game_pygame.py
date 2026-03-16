# gfx/game_pygame.py
# Eyuel Worku, Taveeporn Matta
# MA_24_Othello
# Fichier pour l'affichage du plateau avec Pygame
 
import pygame
import sys
 
# Couleurs de base pour Othello
BOARD_GREEN = (34, 139, 34)  # Vert pour le fond
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0) # Lignes de séparation de la grille
 
class GameWindow:
    def __init__(self, game_logic):
        self.game_logic = game_logic
       
        # Dimensions de la fenêtre et des cases
        self.cell_size = 75 # Pixels par case
        self.width = self.cell_size * 8
        self.height = self.cell_size * 8
 
    def draw_board(self, screen):
        # 1. Remplissage du fond de l'écran
        screen.fill(BOARD_GREEN)
       
        # 2. Dessin des lignes de la grille 8x8
        for i in range(9): # Il faut 9 lignes pour faire 8 cases
            # Lignes horizontales
            pygame.draw.line(screen, LINE_COLOR, (0, i * self.cell_size), (self.width, i * self.cell_size), 2)
            # Lignes verticales
            pygame.draw.line(screen, LINE_COLOR, (i * self.cell_size, 0), (i * self.cell_size, self.height), 2)
           
        # 3. Dessin des pions en lisant la grille de la logique de jeu
        # Pions centraux initiaux
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
 
    def main_loop(self):
        print("Lancement de la boucle Pygame")
        # Initialisation obligatoire de Pygame
        pygame.init()
       
        # Création de la fenêtre
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Othello - Jeu")
       
        running = True
        # Boucle principale du jeu (qui tourne en boucle 60 fois par seconde)
        while running:
            # Gestion des événements (clics, clavier, fermeture de fenêtre)
            for event in pygame.event.get():
                # Si le joueur clique sur la croix de la fenêtre
                if event.type == pygame.QUIT:
                    running = False
           
            # Dessin du plateau et des pions à chaque frame
            self.draw_board(screen)
           
            # Mise à jour de l'écran
            pygame.display.flip()
           
        # Fermeture propre de Pygame
        pygame.quit()
 
 
 