import pygame
import sys

# Initialize all pygame modules
pygame.init()

# Set screen resolution
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Games!")

# Set up colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

LAVENDER = (182, 159, 255)
BUTTER_YELLOW = (251, 231, 164)
SALMON = (255, 135, 160)
TANGERINE = (255, 159, 82)
PURPLE = (98, 59, 190)

GREEN = (27, 255, 105)
RED = (233, 66, 69)
DARK_BLUE = (15, 5, 72)

# Set up player variables
player_size = 25
speed = 3

# Starting position
player_x = 30
player_y = 30

# Exits for each level
exit_rect_1 = pygame.Rect(740, 340, 30, 30)
exit_rect_2 = pygame.Rect(750, 325, 30, 30)
exit_rect_3 = pygame.Rect(750, 50, 30, 30)

# Level 1 Walls
walls_level1 = [
    pygame.Rect(125, 0, 20, 475),
    pygame.Rect(225, 100, 20, 600),
    pygame.Rect(325, 0, 20, 475),
    pygame.Rect(425, 100, 20, 600),
    pygame.Rect(525, 0, 20, 475),
    pygame.Rect(625, 100, 20, 600)
]

# Level 2 Walls
walls_level2 = [
    pygame.Rect(0, 380, 75, 20),
    pygame.Rect(75, 50, 20, 75),
    pygame.Rect(75, 50, 75, 20),
    pygame.Rect(75, 175, 75, 20),
    pygame.Rect(75, 325, 75, 20),
    pygame.Rect(75, 250, 20, 75),
    pygame.Rect(75, 450, 225, 20),
    pygame.Rect(75, 550, 20, 75),
    pygame.Rect(75, 550, 75, 20),
    pygame.Rect(150, 50, 20, 75),
    pygame.Rect(150, 175, 20, 395),
    pygame.Rect(150, 625, 20, 75),
    pygame.Rect(150, 125, 325, 20),
    pygame.Rect(150, 250, 150, 20),
    pygame.Rect(150, 380, 75, 20),
    pygame.Rect(225, 50, 75, 20),
    pygame.Rect(225, 125, 20, 125),
    pygame.Rect(225, 325, 320, 20),
    pygame.Rect(225, 325, 20, 75),
    pygame.Rect(225, 450, 20, 175),
    pygame.Rect(300, 0, 20, 70),
    pygame.Rect(300, 125, 20, 75),
    pygame.Rect(300, 400, 20, 150),
    pygame.Rect(300, 400, 150, 20),
    pygame.Rect(300, 625, 150, 20),
    pygame.Rect(375, 50, 325, 20),
    pygame.Rect(375, 50, 20, 75),
    pygame.Rect(375, 200, 20, 140),
    pygame.Rect(375, 475, 20, 150),
    pygame.Rect(450, 200, 75, 20),
    pygame.Rect(450, 200, 20, 65),
    pygame.Rect(450, 265, 150, 20),
    pygame.Rect(450, 400, 20, 245),
    pygame.Rect(450, 475, 100, 20),
    pygame.Rect(525, 125, 85, 20),
    pygame.Rect(525, 125, 20, 95),
    pygame.Rect(525, 325, 20, 85),
    pygame.Rect(525, 400, 275, 20),
    pygame.Rect(525, 550, 20, 150),
    pygame.Rect(600, 200, 200, 20),
    pygame.Rect(600, 265, 20, 75),
    pygame.Rect(600, 340, 75, 20),
    pygame.Rect(600, 400, 20, 170),
    pygame.Rect(600, 485, 75, 20),
    pygame.Rect(600, 625, 75, 20),
    pygame.Rect(680, 50, 20, 75),
    pygame.Rect(675, 265, 150, 20),
    pygame.Rect(675, 265, 20, 95),
    pygame.Rect(675, 625, 20, 75),
    pygame.Rect(675, 550, 150, 20)
]

# Level 3 Walls
walls_level3 = [
    pygame.Rect(0, 50, 95, 20),
    pygame.Rect(0, 200, 95, 20),
    pygame.Rect(95, 200, 20, 75),
    pygame.Rect(95, 275, 75, 20),
    pygame.Rect(95, 125, 375, 20),
    pygame.Rect(95, 350, 20, 75),
    pygame.Rect(95, 350, 150, 20),
    pygame.Rect(95, 500, 20, 150),
    pygame.Rect(95, 650, 150, 20),
    pygame.Rect(170, 0, 20, 200),
    pygame.Rect(170, 350, 75, 20),
    pygame.Rect(170, 425, 75, 20),
    pygame.Rect(170, 500, 150, 20),
    pygame.Rect(170, 575, 650, 20),
    pygame.Rect(245, 50, 75, 20),
    pygame.Rect(245, 125, 20, 320),
    pygame.Rect(245, 650, 20, 75),
    pygame.Rect(320, 0, 20, 70),
    pygame.Rect(320, 200, 75, 20),
    pygame.Rect(320, 200, 20, 150),
    pygame.Rect(320, 350, 75, 20),
    pygame.Rect(320, 425, 20, 225),
    pygame.Rect(395, 50, 20, 75),
    pygame.Rect(395, 275, 20, 225),
    pygame.Rect(395, 500, 75, 20),
    pygame.Rect(395, 275, 300, 20),
    pygame.Rect(395, 650, 75, 20),
    pygame.Rect(395, 650, 20, 75),
    pygame.Rect(470, 0, 20, 70),
    pygame.Rect(470, 125, 20, 150),
    pygame.Rect(470, 350, 150, 20),
    pygame.Rect(470, 350, 20, 75),
    pygame.Rect(470, 425, 75, 20),
    pygame.Rect(545, 50, 20, 150),
    pygame.Rect(545, 200, 75, 20),
    pygame.Rect(545, 425, 20, 75),
    pygame.Rect(545, 650, 75, 20),
    pygame.Rect(545, 650, 20, 75),
    pygame.Rect(620, 0, 20, 220),
    pygame.Rect(620, 350, 20, 225),
    pygame.Rect(695, 50, 20, 300),
    pygame.Rect(695, 425, 150, 20),
    pygame.Rect(695, 425, 20, 75),
    pygame.Rect(695, 650, 150, 20)
]

# Game state
clock = pygame.time.Clock()
running = True
current_level = 1
game_won = False

# Font initialization
font = pygame.font.SysFont(None, 48)

def check_collision(player_rect, wall_list):
    for wall in wall_list:
        if player_rect.colliderect(wall):
            return True
    return False

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if current_level == 1:
        active_walls = walls_level1
        active_exit = exit_rect_1
    elif current_level == 2:
        active_walls = walls_level2  # Fixed: added missing underscore
        active_exit = exit_rect_2
    elif current_level == 3:
        active_walls = walls_level3
        active_exit = exit_rect_3

    if game_won == False:
        if keys[pygame.K_LEFT]:
            player_x -= speed
            player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
            if check_collision(player_rect, active_walls):
                player_x += speed

        if keys[pygame.K_RIGHT]:
            player_x += speed
            player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
            if check_collision(player_rect, active_walls):
                player_x -= speed

        if keys[pygame.K_UP]:
            player_y -= speed
            player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
            if check_collision(player_rect, active_walls):
                player_y += speed

        if keys[pygame.K_DOWN]:
            player_y += speed
            player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
            if check_collision(player_rect, active_walls):
                player_y -= speed

        if player_x < 0:
            player_x = 0
        elif player_x > SCREEN_WIDTH - player_size:
            player_x = SCREEN_WIDTH - player_size

        if player_y < 0:
            player_y = 0
        elif player_y > SCREEN_HEIGHT - player_size:
            player_y = SCREEN_HEIGHT - player_size

        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        if player_rect.colliderect(active_exit):
            if current_level == 1:
                current_level = 2
                player_x = 20
                player_y = 350
            elif current_level == 2:
                current_level = 3
                player_x = 20
                player_y = 350
            else:
                game_won = True

    screen.fill(WHITE)
    
    if current_level == 1: 
        wall_color = PURPLE
    elif current_level == 2:
        wall_color = LAVENDER
    elif current_level == 3:
        wall_color = TANGERINE

    for wall in active_walls:
        pygame.draw.rect(screen, wall_color, wall)

    # Draw exit
    pygame.draw.rect(screen, GREEN, active_exit)

    # Draw player
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    pygame.draw.rect(screen, DARK_BLUE, player_rect)

    if game_won:
        message = font.render("YOU WIN ALL LEVELS!", True, BLACK)
        screen.blit(message, (220, 300))

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
