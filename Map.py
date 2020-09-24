import pygame, os, sys

pygame.init()
size = width, height = 638, 638
window = pygame.display.set_mode(size)

board_img = os.path.join('board_img.png')
board = pygame.image.load(board_img)
rect = board.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    window.blit(board, rect)
    pygame.display.update()