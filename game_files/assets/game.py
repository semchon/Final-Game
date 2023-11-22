import pygame
from scenes import draw_start, draw_background
from game_parameters import *


#init pygame and basics
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Social Credit: The Game")
clock = pygame.time.Clock()


#Main Loop for Home Screen
home_running = True
instructions_running = False
y = 0
game_running = False
background = screen.copy()
draw_start(background)
left_hand = pygame.image.load("images/hands/clap_left.png").convert()
right_hand = pygame.image.load("images/hands/clap_right.png").convert()
both_hands = pygame.image.load("images/hands/clap_together.png").convert()
right_hand.set_colorkey((255, 255, 255))
left_hand.set_colorkey((255, 255, 255))
both_hands.set_colorkey((255, 255, 255))
font_button = pygame.font.Font("fonts\main_font.ttf", size=40)
quit_button_txt = font_button.render("QUIT", True, (0, 0, 0))
srt_button_txt = font_button.render("START", True, (0, 0, 0))
quit_button_txt_2 = font_button.render("QUIT", True, (255, 255, 255))
srt_button_txt_2 = font_button.render("START", True, (255, 255, 255))

clap = pygame.mixer.Sound("sounds/the_clap.wav")
start_clap = pygame.mixer.Sound("sounds/start_clap.wav")
pygame.mixer.music.load("sounds/start_music.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(loops = 100)
while home_running:
    surf = screen

    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if SCREEN_WIDTH / 2 - 125 <= mouse[0] <= SCREEN_WIDTH / 2 + 125 and SCREEN_HEIGHT / 2 + 150 <= mouse[1] <= SCREEN_HEIGHT / 2 + 210:
                pygame.quit()


        if event.type == pygame.MOUSEBUTTONDOWN:
            if SCREEN_WIDTH / 2 - 125 <= mouse[0] <= SCREEN_WIDTH / 2 + 125 and SCREEN_HEIGHT / 2 + 70 <= mouse[1] <= SCREEN_HEIGHT / 2 + 130:
                home_running = False
                instructions_running = True
                pygame.mixer.Sound.play(start_clap)
            else:
                pygame.mixer.Sound.play(clap)

    surf.blit(background, (0, 0))
    if SCREEN_WIDTH / 2 - 125 <= mouse[0] <= SCREEN_WIDTH / 2 + 125 and SCREEN_HEIGHT / 2 + 150 <= mouse[1] <= SCREEN_HEIGHT / 2 + 210:
        pygame.draw.rect(surf, (0, 0, 0), [SCREEN_WIDTH / 2 - 125, SCREEN_HEIGHT / 2 + 150, 250, 60])
        surf.blit(quit_button_txt_2, (SCREEN_WIDTH / 2 - 40, SCREEN_HEIGHT / 2 + 150))
        pygame.draw.rect(surf, (255, 255, 255), [SCREEN_WIDTH / 2 - 125, SCREEN_HEIGHT / 2 + 70, 250, 60])
        surf.blit(srt_button_txt, (SCREEN_WIDTH / 2 - 55, SCREEN_HEIGHT / 2 + 70))

    elif SCREEN_WIDTH / 2 - 125 <= mouse[0] <= SCREEN_WIDTH / 2 + 125 and SCREEN_HEIGHT / 2 + 70 <= mouse[1] <= SCREEN_HEIGHT / 2 + 130:
        pygame.draw.rect(surf, (255, 255, 255), [SCREEN_WIDTH / 2 - 125, SCREEN_HEIGHT / 2 + 150, 250, 60])
        surf.blit(quit_button_txt, (SCREEN_WIDTH / 2 - 40, SCREEN_HEIGHT / 2 + 150))
        pygame.draw.rect(surf, (0, 0, 0), [SCREEN_WIDTH / 2 - 125, SCREEN_HEIGHT / 2 + 70, 250, 60])
        surf.blit(srt_button_txt_2, (SCREEN_WIDTH / 2 - 55, SCREEN_HEIGHT / 2 + 70))
    else:
        pygame.draw.rect(surf, (255, 255, 255), [SCREEN_WIDTH / 2 - 125, SCREEN_HEIGHT / 2 + 150, 250, 60])
        surf.blit(quit_button_txt, (SCREEN_WIDTH / 2 - 40, SCREEN_HEIGHT / 2 + 150))
        pygame.draw.rect(surf, (255, 255, 255), [SCREEN_WIDTH / 2 - 125, SCREEN_HEIGHT / 2 + 70, 250, 60])
        surf.blit(srt_button_txt, (SCREEN_WIDTH / 2 - 55, SCREEN_HEIGHT / 2 + 70))

    pygame.display.flip()

while instructions_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mixer.Sound.play(start_clap)
            instructions_running = False
            game_running = True
            pygame.mixer.music.stop()
    else:
        instr_img = pygame.image.load("images\instructions_bg.png").convert()
        screen.blit(instr_img, (0,0))
    pygame.display.flip()
draw_background(screen)
screen.blit(left_hand, (int(SCREEN_WIDTH / 4.5), int(SCREEN_HEIGHT / 2.2)))
screen.blit(right_hand, (int(2.1*SCREEN_WIDTH / 4.5), int(SCREEN_HEIGHT / 4)))
score = 0
while game_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                score += 1
                draw_background(screen)
                screen.blit(both_hands, (int(SCREEN_WIDTH / 2.3), int(SCREEN_HEIGHT / 2.4)))
                pygame.mixer.Sound.play(clap)
                print(score)
        if event.type == pygame.KEYUP:
            draw_background(screen)
            screen.blit(left_hand, (int(SCREEN_WIDTH / 4.5), int(SCREEN_HEIGHT / 2.2)))
            screen.blit(right_hand, (int(2.1 * SCREEN_WIDTH / 4.5), int(SCREEN_HEIGHT / 4)))
        text = font_button.render(f"Score: {score}", True, (255, 29, 0))
        screen.blit(text, (text.get_width() / 10, SCREEN_HEIGHT / 2 - 320))
    pygame.display.flip()




pygame.quit()