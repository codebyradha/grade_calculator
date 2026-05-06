import pygame
import random
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (41, 128, 185)
RED = (231, 76, 60)
GREEN = (46, 204, 113)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball")
clock = pygame.time.Clock()

class Ball:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 4
        self.radius = 15
        self.speed_x = random.choice([-4, -3, 3, 4])
        self.speed_y = random.choice([-4, -3, 3, 4])
    
    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.speed_x *= -1
        if self.y - self.radius <= 0:
            self.speed_y *= -1
    
    def display(self):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), self.radius)
    
    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 4
        self.speed_x = random.choice([-4, -3, 3, 4])
        self.speed_y = random.choice([-4, -3, 3, 4])

class Paddle:
    def __init__(self):
        self.width = 100
        self.height = 20
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - 50
        self.speed = 7
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
            self.x += self.speed
    
    def display(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height), 2)
    
    def catches(self, ball):
        if (ball.y + ball.radius >= self.y and 
            ball.y + ball.radius <= self.y + self.height and
            ball.x >= self.x and 
            ball.x <= self.x + self.width):
            return True
        return False

def draw_text(text, size, x, y, color=WHITE):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

ball = Ball()
paddle = Paddle()
score = 0
game_over = False

running = True
while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_over:
                ball.reset()
                score = 0
                game_over = False
    
    if not game_over:
        ball.update()
        paddle.update()
        
        if paddle.catches(ball):
            ball.speed_y *= -1
            ball.y = paddle.y - ball.radius - 1
            score += 1
        
        if ball.y - ball.radius > HEIGHT:
            game_over = True
    
    screen.fill(BLACK)
    
    ball.display()
    paddle.display()
    
    draw_text(f"Score: {score}", 36, WIDTH // 2, 10)
    
    if game_over:
        draw_text("GAME OVER!", 64, WIDTH // 2, HEIGHT // 2 - 50, RED)
        draw_text(f"Final Score: {score}", 48, WIDTH // 2, HEIGHT // 2 + 20, GREEN)
        draw_text("Press SPACE to play again", 32, WIDTH // 2, HEIGHT // 2 + 80)
    
    pygame.display.flip()

pygame.quit()
sys.exit()