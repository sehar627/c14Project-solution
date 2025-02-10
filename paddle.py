import pygame

# Constants
WIDTH = 800
HEIGHT = 600
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
BLUE = (0, 0, 255)  # Corrected color

class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 30, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.velocity = 10

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.velocity

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, self.rect)
