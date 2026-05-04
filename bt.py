import pygame
import math
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Neon Heart")

clock = pygame.time.Clock()

BLACK = (10, 10, 20)
PINK = (255, 80, 150)
BLUE = (80, 180, 255)
WHITE = (255, 255, 255)

font = pygame.font.SysFont("Arial", 40)

# создаем точки сердца
points = []

for t in range(0, 360):
    rad = math.radians(t)

    x = 16 * math.sin(rad) ** 3
    y = (
        13 * math.cos(rad)
        - 5 * math.cos(2 * rad)
        - 2 * math.cos(3 * rad)
        - math.cos(4 * rad)
    )

    x = WIDTH // 2 + int(x * 15)
    y = HEIGHT // 2 - int(y * 15)

    points.append((x, y))

progress = 0


def draw_glow_line(color, start, end):
    # эффект свечения
    for i in range(6, 0, -1):
        pygame.draw.line(
            screen,
            color,
            start,
            end,
            i * 2
        )


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    # рисуем сердце постепенно
    for i in range(progress):
        if i < len(points) - 1:

            if i < len(points) // 2:
                color = PINK
            else:
                color = BLUE

            draw_glow_line(
                color,
                points[i],
                points[i + 1]
            )

    # текст в центре
    text = font.render("bizhka", True, WHITE)
    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, rect)

    if progress < len(points) - 1:
        progress += 2

    pygame.display.flip()
    clock.tick(60)