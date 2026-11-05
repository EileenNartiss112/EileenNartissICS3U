import pygame

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




# Set up the player
player_x = 30
player_y = 30
player_size = 25
speed = 3

player_x2 = 20
player_y2 = 350

# Create the exit
exit_rect = pygame.Rect(740, 340, 30, 30)
exit_rect2 = pygame.Rect(750, 325, 30, 30)

# Create the maze walls
walls = [
    pygame.Rect(125, 0, 20, 475),
    pygame.Rect(225, 100, 20, 600),
    pygame.Rect(325, 0, 20, 475),
    pygame.Rect(425, 100, 20, 600),
    pygame.Rect(525, 0, 20, 475),
    pygame.Rect(625, 100, 20, 600)
]

walls2 = [
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


# Set up the game
clock = pygame.time.Clock()
running = True
won = False
won2 = False

def check_collision(player, walls):
     for wall in walls:
        if player.colliderect(wall):
            return True
     return False


def check_collision2(player2, walls2):
     for wall in walls2:
        if player2.colliderect(wall):
            return True
     return False

# Main game loop
while running:

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keys being pressed
    keys = pygame.key.get_pressed()

    if not won:

        # Move left
        if keys[pygame.K_LEFT]:
            player_x -= speed
            player = pygame.Rect(player_x, player_y, player_size, player_size)

            if check_collision(player,walls) == True:
                player_x += speed


        # Move right
        if keys[pygame.K_RIGHT]:
            player_x += speed
            player = pygame.Rect(player_x, player_y, player_size, player_size)

            if check_collision(player,walls) == True:
                player_x -= speed


        # Move up
        if keys[pygame.K_UP]:
            player_y -= speed
            player = pygame.Rect(player_x, player_y, player_size, player_size)

            if check_collision(player,walls) == True:
                player_y += speed

        # Move down
        if keys[pygame.K_DOWN]:
            player_y += speed
            player = pygame.Rect(player_x, player_y, player_size, player_size)

            if check_collision(player,walls) == True:
                player_y -= speed

        # Keep the player inside the screen
        if player_x < 0:
            player_x = 0

        if player_x > SCREEN_WIDTH - player_size:
            player_x = SCREEN_WIDTH - player_size

        if player_y < 0:
            player_y = 0

        if player_y > SCREEN_HEIGHT - player_size:
            player_y = SCREEN_HEIGHT - player_size

        # Update the player rectangle
        player = pygame.Rect(player_x, player_y, player_size, player_size)

        # Check if the player reaches the exit
        if player.colliderect(exit_rect):
            won = True
            font = pygame.font.SysFont(None, 48)
            message = font.render("LEVEL 1 COMPLETE!", True, BLACK)
            screen.blit(message, (250, 300))

        if not won2:
            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys2 = pygame.key.get_pressed()

            if keys2[pygame.K_LEFT]:
                player_x2 -= speed
                player2 = pygame.Rect(player_x2, player_y2, player_size, player_size)
            
                if check_collision2(player,walls) == True:
                    player_x2 += speed


            if keys2[pygame.K_RIGHT]:
                player_x2 += speed
                player2 = pygame.Rect(player_x2, player_y2, player_size, player_size)
        
                if check_collision2(player,walls) == True:
                    player_x2-= speed


            if keys2[pygame.K_UP]:
                player_y2 -= speed
                player2 = pygame.Rect(player_x2, player_y2, player_size, player_size)
            
                if check_collision2(player,walls) == True:
                    player_y2 += speed


            if keys2[pygame.K_DOWN]:
                player_y2 += speed
                player2 = pygame.Rect(player_x2, player_y2, player_size, player_size)
        
                if check_collision2(player,walls) == True:
                    player_y2 -= speed


            if player_x2 < 0:
                player_x2 = 0
                
            if player_x2 > SCREEN_WIDTH - player_size:
                player_x2 = SCREEN_WIDTH - player_size
        
            if player_y2 < 0:
                player_y2 = 0
                
            if player_y2 > SCREEN_HEIGHT - player_size:
                player_y2 = SCREEN_HEIGHT - player_size
                
            # Update the player rectangle
            player2 = pygame.Rect(player_x2, player_y2, player_size, player_size)
                
            # Check if the player reaches the exit
            if player2.colliderect(exit_rect2):
                won2 = True
                font = pygame.font.SysFont(None, 48)
                message = font.render("LEVEL 2 COMPLETE!", True, BLACK)
                screen.blit(message, (250, 300))

        screen.fill(WHITE)
                
        for wall in walls2:
            pygame.draw.rect(screen, LAVENDER, wall)
                
        pygame.draw.rect(screen, GREEN, exit_rect2)
                
        player2 = pygame.Rect(player_x2, player_y2, player_size, player_size)
        pygame.draw.rect(screen, DARK_BLUE, player)

        # Update the display
        pygame.display.flip()
                
        # Limit the game to 60 FPS
        clock.tick(60)

     # Draw the background
    screen.fill(WHITE)
    
    # Draw the maze walls
    for wall in walls:
        pygame.draw.rect(screen, PURPLE, wall)
    
    # Draw the exit
    pygame.draw.rect(screen, GREEN, exit_rect)
    
    # Draw the player
    player = pygame.Rect(player_x, player_y, player_size, player_size)
    pygame.draw.rect(screen, DARK_BLUE, player)
    
    
    # Update the display
    pygame.display.flip()
    
    # Limit the game to 60 FPS
    clock.tick(60)

                

# Close Pygame
pygame.quit()