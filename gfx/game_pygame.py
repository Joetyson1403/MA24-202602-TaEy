# gfx/game_pygame.py
# Eyuel Worku, Taveeporn Matta
# MA_24_Othello
# Fichier pour l'affichage du plateau avec Pygame
 
import pygame
import os
 
# Couleurs de base pour Othello
BOARD_GREEN = (0, 100, 0)
BLACK = (20, 20, 20)
WHITE = (240, 240, 240)
LINE_COLOR = (0, 60, 0)
HINT_COLOR = (50, 200, 50)
HINT_OUTLINE_COLOR = (30, 160, 30)
SHADOW_COLOR = (0, 50, 0)

# Couleurs pour le panneau d'info
PANEL_BG = (30, 30, 30)
TEXT_COLOR = (230, 230, 230)
GRAY = (130, 130, 130)

def apply_theme(theme_name):
    global BOARD_GREEN, BLACK, WHITE, LINE_COLOR, HINT_COLOR, HINT_OUTLINE_COLOR, SHADOW_COLOR
    global PANEL_BG, TEXT_COLOR, GRAY
    if theme_name == "nuit":
        BOARD_GREEN = (40, 44, 52)
        BLACK = (10, 10, 10)
        WHITE = (200, 200, 200)
        LINE_COLOR = (80, 84, 92)
        HINT_COLOR = (100, 150, 255)
        HINT_OUTLINE_COLOR = (70, 100, 200)
        SHADOW_COLOR = (20, 24, 32)
        PANEL_BG = (20, 22, 28)
        TEXT_COLOR = (180, 180, 180)
        GRAY = (80, 80, 80)
    elif theme_name == "neon":
        BOARD_GREEN = (10, 5, 20)
        BLACK = (0, 255, 255)
        WHITE = (255, 0, 255)
        LINE_COLOR = (50, 20, 80)
        HINT_COLOR = (0, 255, 0)
        HINT_OUTLINE_COLOR = (0, 150, 0)
        SHADOW_COLOR = (5, 2, 10)
        PANEL_BG = (5, 0, 10)
        TEXT_COLOR = (255, 255, 0)
        GRAY = (100, 100, 100)
    else: # classique
        BOARD_GREEN = (0, 100, 0)
        BLACK = (20, 20, 20)
        WHITE = (240, 240, 240)
        LINE_COLOR = (0, 60, 0)
        HINT_COLOR = (50, 200, 50)
        HINT_OUTLINE_COLOR = (30, 160, 30)
        SHADOW_COLOR = (0, 50, 0)
        PANEL_BG = (30, 30, 30)
        TEXT_COLOR = (230, 230, 230)
        GRAY = (130, 130, 130)

class GameWindow:
    def __init__(self, game_logic, p1_name="Noir", p2_name="Blanc", is_ai=False, theme="classique", volume=0.5):
        self.game_logic = game_logic
        self.p1_name = p1_name
        self.p2_name = p2_name
        self.is_ai = is_ai
        self.volume = volume
        
        apply_theme(theme)
       
        # Dimensions de la fenêtre et des cases
        self.cell_size = 75
        self.board_size = self.cell_size * 8
        self.panel_width = 180
        self.width = self.board_size + self.panel_width
        self.height = self.board_size
        
        # UI controls
        self.btn_menu_rect = pygame.Rect(self.board_size + 20, self.height - 60, 140, 40)
        self.btn_vol_down = pygame.Rect(self.board_size + 20, self.height - 110, 30, 30)
        self.btn_vol_up = pygame.Rect(self.board_size + 130, self.height - 110, 30, 30)
        self.btn_theme_rect = pygame.Rect(self.board_size + 20, self.height - 160, 140, 40)
        self.themes_list = ["classique", "nuit", "neon"]
        self.theme = theme
 
    def draw_board(self, screen):
        # Fond du plateau
        pygame.draw.rect(screen, BOARD_GREEN, (0, 0, self.board_size, self.board_size))
       
        # Dessin des lignes de la grille 8x8
        for i in range(9):
            pygame.draw.line(screen, LINE_COLOR, (0, i * self.cell_size), (self.board_size, i * self.cell_size), 2)
            pygame.draw.line(screen, LINE_COLOR, (i * self.cell_size, 0), (i * self.cell_size, self.board_size), 2)

        # Affichage des coups valides (petits cercles avec contour)
        valid_moves = self.game_logic.get_valid_moves(self.game_logic.current_player)
        for (row, col) in valid_moves:
            cx = col * self.cell_size + self.cell_size // 2
            cy = row * self.cell_size + self.cell_size // 2
            pygame.draw.circle(screen, HINT_COLOR, (cx, cy), 10)
            pygame.draw.circle(screen, HINT_OUTLINE_COLOR, (cx, cy), 10, 2)
           
        # Dessin des pions en lisant la grille
        for row in range(8):
            for col in range(8):
                cell_value = self.game_logic.board.grid[row][col]
               
                center_x = col * self.cell_size + self.cell_size // 2
                center_y = row * self.cell_size + self.cell_size // 2
                radius = self.cell_size // 2 - 5
               
                if cell_value == 1:
                    # Pion noir avec ombre et reflet
                    pygame.draw.circle(screen, SHADOW_COLOR, (center_x + 2, center_y + 2), radius)
                    pygame.draw.circle(screen, BLACK, (center_x, center_y), radius)
                    pygame.draw.circle(screen, (60, 60, 60), (center_x - 8, center_y - 8), 8)
                    
                elif cell_value == 2:
                    # Pion blanc avec ombre, contour et reflet
                    pygame.draw.circle(screen, SHADOW_COLOR, (center_x + 2, center_y + 2), radius)
                    pygame.draw.circle(screen, WHITE, (center_x, center_y), radius)
                    pygame.draw.circle(screen, (180, 180, 180), (center_x, center_y), radius, 2)
                    pygame.draw.circle(screen, (255, 255, 255), (center_x - 8, center_y - 8), 6)

    def draw_panel(self, screen):
        """Dessine le panneau d'info à droite (score + tour)"""
        pygame.draw.rect(screen, PANEL_BG, (self.board_size, 0, self.panel_width, self.height))
        
        font_title = pygame.font.SysFont("Helvetica", 22, bold=True)
        font_normal = pygame.font.SysFont("Helvetica", 16)
        font_big = pygame.font.SysFont("Helvetica", 32, bold=True)
        
        center_x = self.board_size + self.panel_width // 2
        
        # Titre
        titre = font_title.render("OTHELLO", True, TEXT_COLOR)
        screen.blit(titre, titre.get_rect(centerx=center_x, y=20))
        
        # Séparateur
        pygame.draw.line(screen, GRAY, (self.board_size + 15, 55), (self.width - 15, 55), 1)
        
        # Comptage des pions sur le plateau
        nb_noirs = sum(row.count(1) for row in self.game_logic.board.grid)
        nb_blancs = sum(row.count(2) for row in self.game_logic.board.grid)
        
        # Score Noir
        pygame.draw.circle(screen, BLACK, (self.board_size + 30, 90), 12)
        screen.blit(font_normal.render(f"{self.p1_name} :", True, TEXT_COLOR), (self.board_size + 50, 80))
        score_noir = font_big.render(str(nb_noirs), True, TEXT_COLOR)
        screen.blit(score_noir, score_noir.get_rect(centerx=center_x, y=110))
        
        # Score Blanc
        pygame.draw.circle(screen, WHITE, (self.board_size + 30, 175), 12)
        pygame.draw.circle(screen, GRAY, (self.board_size + 30, 175), 12, 1)
        screen.blit(font_normal.render(f"{self.p2_name} :", True, TEXT_COLOR), (self.board_size + 50, 165))
        score_blanc = font_big.render(str(nb_blancs), True, TEXT_COLOR)
        screen.blit(score_blanc, score_blanc.get_rect(centerx=center_x, y=195))
        
        # Séparateur
        pygame.draw.line(screen, GRAY, (self.board_size + 15, 245), (self.width - 15, 245), 1)
        
        # Indicateur du tour
        screen.blit(font_normal.render("Tour de :", True, GRAY), 
                     font_normal.render("Tour de :", True, GRAY).get_rect(centerx=center_x, y=265))
        
        # Pion du joueur courant
        if self.game_logic.current_player == 1:
            pygame.draw.circle(screen, BLACK, (center_x, 315), 20)
            nom = font_normal.render(self.p1_name, True, TEXT_COLOR)
        else:
            pygame.draw.circle(screen, WHITE, (center_x, 315), 20)
            pygame.draw.circle(screen, GRAY, (center_x, 315), 20, 1)
            nom = font_normal.render(self.p2_name, True, TEXT_COLOR)
        
        screen.blit(nom, nom.get_rect(centerx=center_x, y=345))
        
        # Bouton Thème
        pygame.draw.rect(screen, (80, 80, 80), self.btn_theme_rect, border_radius=5)
        btn_theme_text = font_normal.render(f"Thème: {self.theme.capitalize()}", True, (255, 255, 255))
        screen.blit(btn_theme_text, btn_theme_text.get_rect(center=self.btn_theme_rect.center))

        # Contrôle du volume
        pygame.draw.rect(screen, (80, 80, 80), self.btn_vol_down, border_radius=5)
        btn_minus = font_title.render("-", True, (255, 255, 255))
        screen.blit(btn_minus, btn_minus.get_rect(center=self.btn_vol_down.center))
        
        pygame.draw.rect(screen, (80, 80, 80), self.btn_vol_up, border_radius=5)
        btn_plus = font_title.render("+", True, (255, 255, 255))
        screen.blit(btn_plus, btn_plus.get_rect(center=self.btn_vol_up.center))
        
        vol_text = font_normal.render(f"Vol: {int(self.volume * 100)}%", True, TEXT_COLOR)
        screen.blit(vol_text, vol_text.get_rect(center=(self.board_size + 90, self.height - 95)))

        # Bouton Retour Menu
        pygame.draw.rect(screen, (80, 80, 80), self.btn_menu_rect, border_radius=5)
        btn_text = font_normal.render("Retour Menu", True, (255, 255, 255))
        screen.blit(btn_text, btn_text.get_rect(center=self.btn_menu_rect.center))

    def check_game_over(self):
        """Vérifie si la partie est terminée ou si le joueur doit passer son tour"""
        coups_joueur = self.game_logic.get_valid_moves(self.game_logic.current_player)
        adversaire = 2 if self.game_logic.current_player == 1 else 1
        coups_adversaire = self.game_logic.get_valid_moves(adversaire)
        
        if len(coups_joueur) == 0 and len(coups_adversaire) == 0:
            return True  # Fin de partie
        elif len(coups_joueur) == 0:
            self.game_logic.current_player = adversaire  # Passe le tour
        
        return False

    def draw_game_over(self, screen):
        """Affiche le message de fin de partie"""
        # Overlay semi-transparent sur le plateau
        overlay = pygame.Surface((self.board_size, self.height))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))
        
        # Comptage final
        nb_noirs = sum(row.count(1) for row in self.game_logic.board.grid)
        nb_blancs = sum(row.count(2) for row in self.game_logic.board.grid)
        
        # Déterminer le gagnant
        if nb_noirs > nb_blancs:
            message = f"{self.p1_name} gagne !"
        elif nb_blancs > nb_noirs:
            message = f"{self.p2_name} gagne !"
        else:
            message = "Egalite !"
        
        font_big = pygame.font.SysFont("Helvetica", 40, bold=True)
        font_score = pygame.font.SysFont("Helvetica", 24)
        
        # Message de victoire
        texte = font_big.render(message, True, (255, 215, 0))
        screen.blit(texte, texte.get_rect(center=(self.board_size // 2, self.height // 2 - 20)))
        
        # Score final
        score = font_score.render(f"{self.p1_name} {nb_noirs} - {nb_blancs} {self.p2_name}", True, TEXT_COLOR)
        screen.blit(score, score.get_rect(center=(self.board_size // 2, self.height // 2 + 25)))
 
    def main_loop(self):
        pygame.init()
        pygame.mixer.init()
        
        try:
            pygame.mixer.music.load(os.path.join("assets", "music.mp3"))
            pygame.mixer.music.set_volume(self.volume)
            pygame.mixer.music.play(-1)
        except Exception:
            pass
       
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Othello - Jeu")
       
        game_over = False
        running = True
        action = "quit"

        while running:
            # Traitement IA
            if not game_over and self.is_ai and self.game_logic.current_player == 2:
                self.draw_board(screen)
                self.draw_panel(screen)
                pygame.display.flip()
                
                pygame.time.wait(600) # Délai pour l'immersion
                
                ai_move = self.game_logic.get_ai_move(2)
                if ai_move:
                    self.game_logic.play_move(ai_move[0], ai_move[1])
                
                game_over = self.check_game_over()
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    action = "quit"

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    
                    if self.btn_menu_rect.collidepoint(mouse_x, mouse_y):
                        running = False
                        action = "menu"
                        
                    elif self.btn_vol_down.collidepoint(mouse_x, mouse_y):
                        self.volume = max(0.0, self.volume - 0.1)
                        if pygame.mixer.get_init():
                            pygame.mixer.music.set_volume(self.volume)
                            
                    elif self.btn_vol_up.collidepoint(mouse_x, mouse_y):
                        self.volume = min(1.0, self.volume + 0.1)
                        if pygame.mixer.get_init():
                            pygame.mixer.music.set_volume(self.volume)
                            
                    elif self.btn_theme_rect.collidepoint(mouse_x, mouse_y):
                        current_index = self.themes_list.index(self.theme)
                        next_index = (current_index + 1) % len(self.themes_list)
                        self.theme = self.themes_list[next_index]
                        apply_theme(self.theme)
                        
                    elif not game_over:
                        # Ne pas permettre les coups cliqués pendant le tour de l'IA
                        if self.is_ai and self.game_logic.current_player == 2:
                            continue
                            
                        # On vérifie que le clic est sur le plateau (pas le panneau)
                        if mouse_x < self.board_size:
                            col = mouse_x // self.cell_size
                            row = mouse_y // self.cell_size
                            self.game_logic.play_move(row, col)
                            game_over = self.check_game_over()
           
            # Dessin du plateau, du panneau et éventuellement du message de fin
            self.draw_board(screen)
            self.draw_panel(screen)
            
            if game_over:
                self.draw_game_over(screen)
           
            pygame.display.flip()
           
        pygame.quit()
        return action