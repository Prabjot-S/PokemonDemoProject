import pygame

pygame.init() #start up pygame


WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH,HEIGHT)) #gives space to draw things
pygame.display.set_caption("Pokemon Game")

#menu background
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))


state = 'menu'
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if state == 'menu':
        screen.blit(background, (0,0))

    pygame.display.flip() #updates the screen



pygame.quit()
