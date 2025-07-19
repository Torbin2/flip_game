#settings
TILE_SIZE = 200
GRID_SIZE = (12, 6) #(x,y)
SCRAMBLE_TIMES = 15
SHOW_SCRAMBLE = True
BORDERS = True

import pygame
from random import randint

pygame.init()

screen = pygame.display.set_mode((GRID_SIZE[0] * TILE_SIZE + 2 * TILE_SIZE , GRID_SIZE[1] * TILE_SIZE + 2 * TILE_SIZE))
pygame.display.set_caption("flip_game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

class Tile:
    def __init__(self, tile_num):
        self.rect = pygame.Rect(((tile_num[0]+1) * TILE_SIZE, (tile_num[1]+1)* TILE_SIZE), (TILE_SIZE, TILE_SIZE)) 
        self.side = True 

    def render(self):
        color = ["#0b3804", "#040b38"][self.side]
        pygame.draw.rect(screen, color, self.rect)
        if BORDERS:
            pygame.draw.rect(screen, "black", self.rect, width=10)
#tile_creation
tiles = {}
for x in range(GRID_SIZE[0]):
    for y in range(GRID_SIZE[1]):
        tiles[x, y] = Tile((x,y))

def click(tile):
    for x_off, y_off in [(-1, 0), (0, -1), (0,0), (1,0), (0, 1)]:
            if (tile[0] + x_off, tile[1] + y_off) in tiles:
                tiles[(tile[0] + x_off, tile[1] + y_off)].side = not tiles[(tile[0] + x_off, tile[1] + y_off)].side

def setboard():
    for _ in range(SCRAMBLE_TIMES):
        chosen_tile = (randint(0, GRID_SIZE[0] - 1), randint(0, GRID_SIZE[1] - 1 ))
        click(chosen_tile)
        if SHOW_SCRAMBLE: print(chosen_tile)
setboard()

def checkwin(side_):
    for tile in tiles:
        if tiles[tile].side != side_:
            return
    else: 
        print("win")
        setboard()

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            selected = (pygame.mouse.get_pos()[0] // TILE_SIZE - 1, pygame.mouse.get_pos()[1] // TILE_SIZE -1 ) 
            click(selected)
            if selected in tiles: checkwin(tiles[selected].side)

    screen.fill("#310438")

    for tile in tiles:
        tiles[tile].render()

    pygame.display.update()
    clock.tick(30)
