import pygame
from scenes import draw_start, draw_background, semi_draw_background
from game_parameters import *
from crowd import Crowd, crowd
import random
import os

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
quit_screen = False
background = screen.copy()
draw_start(background)
left_hand = pygame.image.load("images/hands/clap_left.png").convert()
right_hand = pygame.image.load("images/hands/clap_right.png").convert()
both_hands = pygame.image.load("images/hands/clap_together.png").convert()
both_hands_bad = pygame.image.load("images/hands/clap_together_bad.png").convert()
right_hand.set_colorkey((255, 255, 255))
left_hand.set_colorkey((255, 255, 255))
both_hands.set_colorkey((255, 255, 255))
both_hands_bad.set_colorkey((255, 255, 255))
font_button = pygame.font.Font("fonts\main_font.ttf", size=40)
quit_button_txt = font_button.render("QUIT", True, (0, 0, 0))
srt_button_txt = font_button.render("START", True, (0, 0, 0))
quit_button_txt_2 = font_button.render("QUIT", True, (255, 255, 255))
srt_button_txt_2 = font_button.render("START", True, (255, 255, 255))
crowd1_srt = pygame.image.load("images/crowd_sprites/crowd1_2.png").convert()
crowd12_srt = pygame.image.load("images/crowd_sprites/crowd1_3.png").convert()
crowd2_srt = pygame.image.load("images/crowd_sprites/crowd5_2.png").convert()
crowd22_srt = pygame.image.load("images/crowd_sprites/crowd5_3.png").convert()
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
crowd = Crowd(0,0)

bottom_mask_large = pygame.image.load("images/crowd_sprites/coverup.png")
bottom_mask = pygame.transform.scale(bottom_mask_large, (1279,255))
game_tick_bookmark =clock.get_time()
current_time = 0
hand_state = left_hand
hand_state2 = right_hand
hand_state1_rect = (int(SCREEN_WIDTH / 2.3), int(SCREEN_HEIGHT / 2.4))
hand_state2_rect = (int(SCREEN_WIDTH / 2.3), int(SCREEN_HEIGHT / 2.4))
crowdstate = True

while game_running:
    clock.tick(1000)
    game_current_tick = clock.get_time()
    current_time += game_current_tick
    time_left = int(60-(current_time/1000))
    time_txt= font_button.render(f"Time Left: {time_left}", True, (255, 29, 0))
    draw_background(screen)
    screen.blit(time_txt, (20, SCREEN_HEIGHT / 2 - 280))
    text = font_button.render(f"Score: {score}", True, (255, 29, 0))
    screen.blit(text, (20, SCREEN_HEIGHT / 2 - 320))
    if crowdstate == False:
        for k in range(4):
            for i in range(15):
                crowd.draw_crowd(screen, i * 137 + 69 * k - 400, k * 40 + 50)
    elif crowdstate == True:
        for k in range(4):
            for i in range(15):
                crowd.draw_crowd_clapping(screen, i * 137 + 69 * k - 400, k * 40 + 50)
    screen.blit(bottom_mask,(-1,555))

    screen.blit(hand_state, hand_state1_rect)

    screen.blit(hand_state2, hand_state2_rect)

    if 55<time_left<57 or 51<time_left<53 or 44<time_left<46 or 41<time_left<42 or 37<time_left<39 or 30<time_left<32 or 25<time_left<27 or 20<time_left<22 or 16<time_left<19 or 10<time_left<12 or 7<time_left<9 or 4<time_left<6 or time_left<2:
        crowdstate=True
        random_clap = random.choice(os.listdir("sounds/applauses"))
        pygame.mixer.music.load(f"sounds/applauses/{random_clap}")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.Sound.play(clap)
                    random_shush = random.choice(os.listdir("sounds/shushes"))
                    shush = pygame.mixer.Sound(f"sounds/shushes/{random_shush}")
                    pygame.mixer.Sound.play(shush)
                    score -= 1
                    hand_state = both_hands_bad
                    hand_state2 = both_hands_bad
                    hand_state1_rect = (int(SCREEN_WIDTH / 2.3), int(SCREEN_HEIGHT / 2.4))
                    hand_state2_rect = (int(SCREEN_WIDTH / 2.3), int(SCREEN_HEIGHT / 2.4))

            if event.type == pygame.KEYUP:
                hand_state=left_hand
                hand_state2= right_hand
                hand_state1_rect = (int(SCREEN_WIDTH / 4.5), int(SCREEN_HEIGHT / 2.2))
                hand_state2_rect = (int(2.1 * SCREEN_WIDTH / 4.5), int(SCREEN_HEIGHT / 4))

    else:
        crowdstate = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.Sound.play(clap)
                    score += 1
                    hand_state = both_hands
                    hand_state2 = both_hands
                    hand_state1_rect = (int(SCREEN_WIDTH / 2.3), int(SCREEN_HEIGHT / 2.4))
                    hand_state2_rect = (int(SCREEN_WIDTH / 2.3), int(SCREEN_HEIGHT / 2.4))


            if event.type == pygame.KEYUP:
                hand_state = left_hand
                hand_state2 = right_hand
                hand_state1_rect = (int(SCREEN_WIDTH / 4.5), int(SCREEN_HEIGHT / 2.2))
                hand_state2_rect = (int(2.1 * SCREEN_WIDTH / 4.5), int(SCREEN_HEIGHT / 4))


    if time_left == 0:
        game_running = False
        quit_screen = True
    pygame.display.flip()

pygame.mixer.music.pause()
with open('highscore.txt','r') as score_file:
    e = score_file.readlines()
    highscore = int(e[0])
    print(score)
    if score > highscore:
        with open('highscore.txt','w') as sco_file:
            sco_file.write(f"{score}")
            highscore = score

while quit_screen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        else:
            pygame.display.flip()
            for x in range(0, SCREEN_WIDTH, TILE_SIZE):
                for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
                    screen.blit(pygame.image.load("images/bg_tile_up.png").convert(), (x, y))
            font1 = pygame.font.Font("fonts\main_font.ttf", size=80)
            game_over = font1.render("GAME OVER", True, (255, 29, 0))
            final_score = font1.render(f"Score-{score}", True, (255, 29, 0))
            screen.blit(game_over, (SCREEN_WIDTH/2-game_over.get_width()/2, SCREEN_HEIGHT/2-300))
            screen.blit(final_score, (SCREEN_WIDTH/2-final_score.get_width()/2, SCREEN_HEIGHT/2-230))
            clock.tick(10)


pygame.quit()
