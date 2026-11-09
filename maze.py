import pygame

pygame.init()

# Set screen resolution
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Game!")

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
player_x = 20
player_y = 350
player_size = 25
speed = 3

# Create the exit
exit_rect = pygame.Rect(750, 50, 30, 30)

# Create the maze walls
walls = [
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



# Set up the game
clock = pygame.time.Clock()
running = True
won = False

def check_collision(player, walls):
    
    for wall in walls:
        if player.colliderect(wall):
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

    # Display the winning message
    if won:
        font = pygame.font.SysFont(None, 48)
        message = font.render("LEVEL 2 COMPLETE!", True, BLACK)
        screen.blit(message, (250, 300))

    # Update the display
    pygame.display.flip()

    # Limit the game to 60 FPS
    clock.tick(60)

# Close Pygame
pygame.quit()