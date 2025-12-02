import random

import pygame
import button
from button import Button

pygame.init() #start up pygame

font = pygame.font.Font('PixeloidSans.ttf', 17)

# BASIC SETUP ----------------------------
WIDTH, HEIGHT = 850, 550
screen = pygame.display.set_mode((WIDTH,HEIGHT)) #gives space to draw things
pygame.display.set_caption("Pokemon Game")
# ----------------------------------------

#FADING
fade_surface = pygame.Surface((WIDTH, HEIGHT))  # Black surface for fading
fade_surface.fill((0, 0, 0))
fade_alpha = 0  # Transparency (0 = invisible, 255 = solid black)
fading = False

# LOADING GRAPHICS (FOR MENU) -------------
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
pokemon_logo = pygame.image.load("pokemon_logo.png")
pokemon_logo = pygame.transform.scale(pokemon_logo,(350,120))

#import cursor
cursor_image = pygame.image.load('graphics/pokedex cursor.png')
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
play_again_button = pygame.image.load('play_again.png').convert_alpha()

#button instances
start_button = button.Button(140,235, start_button, 0.8)
exit_button = button.Button(500,235, exit_button, 0.8)
play_again_button = Button(340,450, play_again_button, 0.6)
# ----------------------------------------

# GRAPHICS (FOR BATTLE FIELD) ------------
battle_background = pygame.image.load("background-hero.png")
battle_background = pygame.transform.scale(battle_background, (WIDTH, HEIGHT))

#blastoise animation loading
gif_frames_blastoise = []
for i in range(46):
    frame_blastoise = pygame.image.load(f'blastoise_split/frame_{i:02d}_delay-0.05s.png')
    frame_blastoise = pygame.transform.scale(frame_blastoise, (180,180))
    gif_frames_blastoise.append(frame_blastoise)

current_frame_blastoise = 0
frame_counter_blastoise = 0
frame_speed_blastoise = 6 #lower is faster (speed)

#giratina animation loading
gif_frames_giratina = []
for i in range(41):
    frame_giratina = pygame.image.load(f'giratina_split/frame_{i:02d}_delay-0.06s.png')
    frame_giratina = pygame.transform.scale(frame_giratina, (230,215))
    gif_frames_giratina.append(frame_giratina)

current_frame_giratina = 0
frame_counter_giratina = 0
frame_speed_giratina = 7 #lower is faster (speed)

#attack menu vars
show_attack_menu_giratina = False
show_attack_menu_blastoise = False
attack_menu_x_giratina, attack_menu_y_giratina = 200,200
attack_menu_x_blastoise, attack_menu_y_blastoise = 480,200

#attack effects loading
gif_frames_water = []
for i in range(23):
    frame_water = pygame.image.load(f'water_attack_split/frame_{i:02d}_delay-0.04s.png')
    frame_water = pygame.transform.scale(frame_water, (250,250))
    gif_frames_water.append(frame_water)

current_frame_water = 0
frame_counter_water = 0
frame_speed_water = 7

gif_frames_slash = []
for i in range(6):
    frame_slash = pygame.image.load(f'slash_attack_split/frame_{i}_delay-0.1s.png')
    frame_slash = pygame.transform.scale(frame_slash, (250,250))
    gif_frames_slash.append(frame_slash)

current_frame_slash = 0
frame_counter_slash = 0
frame_speed_slash = 7

# ----------------------------------------

# LOADING GRAPHICS (FOR WINNER SCREEN) -------------

winner_logo = pygame.image.load('winner_logo.png')
winner_logo = pygame.transform.scale(winner_logo, (350,120))


# --------------------------------------------------

# Health Bar

class HealthBar():
    def __init__(self, x, y, w, h, max_hp):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = max_hp
        self.max_hp = max_hp

    def draw(self, surface):
        # Black border (slightly bigger)
        pygame.draw.rect(surface, 'black', (self.x - 2, self.y - 2, self.w + 4, self.h + 4))

        #calculate the health ratio
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, 'red', (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, '#27a147',(self.x, self.y, self.w * ratio, self.h))

health_bar_giratina = HealthBar(22, 440, 200, 23, 100)
health_bar_blastoise = HealthBar(630, 440, 200, 23, 100)


#game loop ------------------------------------------
state = 'menu'
show_water_attack = False
show_slash_attack = False
running = True
blastoise_hp = 100
giratina_hp = 100
blastoise_heals = 3
giratina_heals = 3
turn_count = 1
while running:

    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            running = False

    if state == 'menu':

        screen.blit(background, (0,0))
        screen.blit(pokemon_logo, (245,60))

        #animate charizard
        frame_counter += 1
        # When we hit __ speed, flip to next page
        if frame_counter >= frame_speed:
            current_frame = (current_frame + 1) % len(gif_frames)
            frame_counter = 0

        screen.blit(gif_frames[current_frame], (350, 330))

        if start_button.draw(screen):
            state = 'battle'
            #FADING
            fading = True
            fade_alpha = 255  # Start fully black
        if exit_button.draw(screen):
            running = False

    elif state == 'battle':
        screen.blit(battle_background, (0,0))

        #health bars ---------------------------------------------------

        health_bar_giratina.draw(screen)
        health_bar_blastoise.draw(screen)

        # --------------------------------------------------------------

        #animate blastoise ---------------------------------------------
        frame_counter_blastoise += 1
        # When we hit __ speed, flip to next page
        if frame_counter_blastoise >= frame_speed_blastoise:
            current_frame_blastoise = (current_frame_blastoise + 1) % len(gif_frames_blastoise)
            frame_counter_blastoise = 0

        screen.blit(gif_frames_blastoise[current_frame_blastoise], (650, 235))
        # ----------------------------------------------------------------

        #GIRATINA

        pokemon_name = 'Giratina'
        name_text = font.render(pokemon_name, True, (0,0,0))
        # Draw white rectangle behind text
        pygame.draw.rect(screen, (255, 255, 255), (20, 190, 100, 25))  # white box
        screen.blit(name_text, (36, 192))  # text on top

        #animate giratina
        frame_counter_giratina += 1
        # When we hit __ speed, flip to next page
        if frame_counter_giratina >= frame_speed_giratina:
            current_frame_giratina = (current_frame_giratina + 1) % len(gif_frames_giratina)
            frame_counter_giratina = 0

        screen.blit(gif_frames_giratina[current_frame_giratina], (10, 220))

        #attack menu for giratina
        giratina_rect = gif_frames_giratina[current_frame_giratina].get_rect(topleft=(10, 220))
        # check if giratina was clicked
        if event.type == pygame.MOUSEBUTTONDOWN and turn_count % 2 == 1: #only odd turns
            mouse_pos = pygame.mouse.get_pos()
            if giratina_rect.collidepoint(mouse_pos):
                show_attack_menu_giratina = True

        if show_attack_menu_giratina:
            #white box
            menu_width_giratina, menu_height_giratina = 200, 150
            pygame.draw.rect(screen, (255,255,255), (attack_menu_x_giratina+50, attack_menu_y_giratina, 100, 130))

            #attack names
            attacks = ['Attack', 'Heal', 'Concede']
            attacks_rects = [] #store rectangles for click detection
            for i, attack in enumerate(attacks):
                attack_text = font.render(attack, True, (0,0,0)) #turn the text to image

                #create rectangle around text
                text_rect = attack_text.get_rect(center=((attack_menu_x_giratina) + menu_width_giratina // 2, attack_menu_y_giratina + 30 + i * 35))
                screen.blit(attack_text, text_rect) #draw the text
                attacks_rects.append(text_rect)

            #check for clicked attack
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(attacks_rects):
                    if rect.collidepoint(mouse_pos):
                        if i == 0:
                            print('ATTACK')
                            show_slash_attack = True
                            current_frame_slash = 0
                            frame_counter_slash = 0

                            damage = random.randint(10,30) # random damage
                            health_bar_blastoise.hp -= damage
                            print(f'Hit for {damage} damage!')
                            turn_count += 1

                            #winning condition check
                            if health_bar_blastoise.hp <= 0:
                                print('Giratina won')
                                state = 'winner'

                        elif i == 1:
                            if health_bar_giratina.hp < health_bar_giratina.max_hp and giratina_heals > 0:

                                if 100 > health_bar_giratina.hp > 90:
                                    health_bar_giratina.hp = 100
                                else:
                                    health_bar_giratina.hp += 10

                                giratina_heals -= 1
                                print(f'Giratina healed by 10 | Current HP: {health_bar_giratina.hp}')
                                turn_count += 1
                            else:
                                print('Healing limit reached')
                        elif i == 2:
                            print('CONCEDE')

                        show_attack_menu_giratina = False

        if show_slash_attack:
            frame_counter_slash += 1
            if frame_counter_slash >= frame_speed_slash:
                current_frame_slash = (current_frame_slash + 1) % len(gif_frames_slash)
                frame_counter_slash = 0

                # Stop animation after one loop (23 frames)
                if current_frame_slash == 0 and frame_counter_slash == 0:
                    show_slash_attack = False

            screen.blit(gif_frames_slash[current_frame_slash], (600, 200))

        # ----------------------------------------------------------------

        #BLASTOISE

        pokemon_name = 'Blastoise'
        name_text = font.render(pokemon_name, True, (0,0,0))
        # Draw white rectangle behind text
        pygame.draw.rect(screen, (255, 255, 255), (730, 190, 100, 25))  # white box
        screen.blit(name_text, (738, 192))  # text on top

        # attack menu for blastoise
        blastoise_rect = gif_frames_blastoise[current_frame_blastoise].get_rect(topleft=(650, 235))
        # check if blastoise was clicked
        if event.type == pygame.MOUSEBUTTONDOWN and turn_count % 2 == 0: #only even turns
            mouse_pos = pygame.mouse.get_pos()
            if blastoise_rect.collidepoint(mouse_pos):
                show_attack_menu_blastoise = True

        if show_attack_menu_blastoise:
            # white box
            menu_width_blastoise, menu_height_blastoise = 200, 150
            pygame.draw.rect(screen, (255, 255, 255), (attack_menu_x_blastoise + 50, attack_menu_y_blastoise, 100, 130))

            # attack names
            attacks_blastoise = ['Attack', 'Heal', 'Concede']
            attacks_rects_blastoise = []  # store rectangles for click detection
            for i, attack in enumerate(attacks_blastoise):
                attack_text = font.render(attack, True, (0, 0, 0))  # turn the text to image

                # create rectangle around text
                text_rect = attack_text.get_rect(
                    center=((attack_menu_x_blastoise) + menu_width_blastoise // 2, attack_menu_y_blastoise + 30 + i * 35))
                screen.blit(attack_text, text_rect)  # draw the text
                attacks_rects_blastoise.append(text_rect)

            # check for clicked attack
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(attacks_rects_blastoise):
                    if rect.collidepoint(mouse_pos):
                        if i == 0:
                            print('ATTACK')
                            show_water_attack = True
                            current_frame_water = 0
                            frame_counter_water = 0
                            damage = random.randint(10,30) # random damage
                            health_bar_giratina.hp -= damage
                            print(f'Hit for {damage} damage!')
                            turn_count += 1

                            #winning condition check
                            if health_bar_giratina.hp <= 0:
                                print('Blastoise won')
                                state = 'winner'
                        elif i == 1:
                            if health_bar_blastoise.hp < health_bar_blastoise.max_hp and blastoise_heals > 0:

                                if 100 > health_bar_blastoise.hp > 90:
                                    health_bar_blastoise.hp = 100
                                else:
                                    health_bar_blastoise.hp += 10

                                blastoise_heals -= 1
                                print(f'Blastoise Healed by 10 | Current HP: {health_bar_blastoise.hp}')
                                turn_count += 1
                            else:
                                print('Healing limit reached')
                        elif i == 2:
                            print('CONCEDE')

                        show_attack_menu_blastoise = False

        if show_water_attack:
            frame_counter_water += 1
            if frame_counter_water >= frame_speed_water:
                current_frame_water = (current_frame_water + 1) % len(gif_frames_water)
                frame_counter_water = 0

                # Stop animation after one loop (23 frames)
                if current_frame_water == 0 and frame_counter_water == 0:
                    show_water_attack = False

            screen.blit(gif_frames_water[current_frame_water], (15, 250))


        #FADING
        if fading:
            fade_alpha -= 3  # Fade out (decrease by 5 each frame)
            if fade_alpha <= 0:
                fade_alpha = 0
                fading = False
            fade_surface.set_alpha(fade_alpha)
            screen.blit(fade_surface, (0, 0))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                health_bar_giratina.hp = 100
                health_bar_blastoise.hp = 100
                show_attack_menu_giratina = False
                show_attack_menu_blastoise = False
                state = 'menu'

    elif state == 'winner':
        screen.blit(background, (0, 0))

        #make it dim
        dim_surface = pygame.Surface((WIDTH, HEIGHT))
        dim_surface.fill((0,0,0))
        dim_surface.set_alpha(175)
        screen.blit(dim_surface, (0, 0))

        screen.blit(winner_logo, (245, 60))

        if health_bar_giratina.hp <= 0: #blastoise won

            # animate blastoise ---------------------------------------------
            frame_counter_blastoise += 1
            if frame_counter_blastoise >= frame_speed_blastoise:
                current_frame_blastoise = (current_frame_blastoise + 1) % len(gif_frames_blastoise)
                frame_counter_blastoise = 0

            screen.blit(gif_frames_blastoise[current_frame_blastoise], (350, 235))
            # ----------------------------------------------------------------

        else: #giratina won
            # animate giratina ---------------------------------------------
            frame_counter_giratina += 1
            if frame_counter_giratina >= frame_speed_giratina:
                current_frame_giratina = (current_frame_giratina + 1) % len(gif_frames_giratina)
                frame_counter_giratina = 0

            screen.blit(gif_frames_giratina[current_frame_giratina], (305, 200))
            # ----------------------------------------------------------------

        if play_again_button.draw(screen):
            health_bar_giratina.hp = 100
            health_bar_blastoise.hp = 100
            state = 'menu'




    # mouse position / draw cursor
    cursor_xy = pygame.mouse.get_pos()
    screen.blit(cursor_image, cursor_xy)

    pygame.display.flip() #updates the screen



pygame.quit()

# 1: Pokémon shouldn't be able to heal everytime