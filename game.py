import pygame
pygame.init()
screen = pygame.display.set_mode((500,400))
pygame.display.set_caption("Hello World")

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.quit():
            running=False
    screen.fill((30,30,30))
    pygame.draw.rect(screen,(200,200,200),(230,170,40,60))
    pygame.display.flip()
pygame.quit()