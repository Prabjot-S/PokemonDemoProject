import pygame
import button

pygame.init() #start up pygame


WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH,HEIGHT)) #gives space to draw things
pygame.display.set_caption("Pokemon Game")

#menu background / menu graphics loading
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
pokemon_logo = pygame.image.load("pokemon_logo.png")
pokemon_logo = pygame.transform.scale(pokemon_logo,(350,120))

#import cursor
cursor_image = pygame.image.load('pokeball_cursor.png')
cursor_image = pygame.transform.scale(cursor_image, (75,75))

#hide cursor
pygame.mouse.set_visible(False)

#charizard animation loading
gif_frames = []
for i in range(16):
    frame = pygame.image.load(f'charizard_split/frame_{i:02d}_delay-0.1s.png')
    frame = pygame.transform.scale(frame, (500,226))
    gif_frames.append(frame)

current_frame = 0
frame_counter = 0
frame_speed = 70 #lower is faster (speed)


#load button images
start_button = pygame.image.load('start_btn.png').convert_alpha()
exit_button = pygame.image.load('exit_btn.png').convert_alpha()

#button instances
start_button = button.Button(120,235, start_button, 0.8)
exit_button = button.Button(470,235, exit_button, 0.8)



#game loop
state = 'menu'
running = True
while running:



    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            running = False

    if state == 'menu':

        screen.blit(background, (0,0))
        screen.blit(pokemon_logo, (220,60))

        #animate charizard
        frame_counter += 1
        if frame_counter >= frame_speed:
            current_frame = (current_frame + 1) % len(gif_frames)
            frame_counter = 0

        screen.blit(gif_frames[current_frame], (350, 300))

        if start_button.draw(screen):
            print('START')
        if exit_button.draw(screen):
            running = False

        # mouse position
        cursor_xy = pygame.mouse.get_pos()

        # draw cursor
        screen.blit(cursor_image, cursor_xy)

    pygame.display.flip() #updates the screen



pygame.quit()
