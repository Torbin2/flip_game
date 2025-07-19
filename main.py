import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("flip_game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(30)
