import pygame
from paddle import Paddle  # Import your class

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker")

# Create paddle instance
paddle = Paddle()

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))  # Clear screen (black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle paddle movement
    keys = pygame.key.get_pressed()
    paddle.move(keys)

    # Draw paddle
    paddle.draw(screen)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
