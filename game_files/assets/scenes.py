from assets.game_parameters import *

def draw_start(surf):
    start_png = pygame.image.load("images\start_tile.png").convert()
    start_png.set_colorkey((0,0,0))
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            surf.blit(start_png, (x,y))
    font1 = pygame.font.Font("fonts\main_font.ttf", size=80)
    font1_sub = pygame.font.Font("fonts\main_font.ttf", size=50)
    main_txt_1 = font1.render("SOCIAL CREDIT THE GAME", True, (255, 29, 0))
    main_txt_2 = font1_sub.render("Made by Sam Chon", True, (255, 29, 0))
    surf.blit(main_txt_1, (SCREEN_WIDTH/2-main_txt_1.get_width()/2, SCREEN_HEIGHT/2-300))
    surf.blit(main_txt_2, (SCREEN_WID   TH/2-main_txt_2.get_width()/2, SCREEN_HEIGHT/2-220))

def home_draw(surf,backing):
    font_button = pygame.font.Font("fonts\main_font.ttf", size=40)
    quit_button_txt = font_button.render("QUIT", True, (0, 0, 0))
    srt_button_txt = font_button.render("START", True, (0, 0, 0))
    quit_button_txt_2 = font_button.render("QUIT", True, (255,255,255))
    srt_button_txt_2 = font_button.render("START", True, (255,255,255))
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if SCREEN_WIDTH/2-125 <= mouse[0] <= SCREEN_WIDTH/2+125 and SCREEN_HEIGHT/2+150 <= mouse[1] <= SCREEN_HEIGHT/2+210:
                pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if SCREEN_WIDTH/2-125 <= mouse[0] <= SCREEN_WIDTH/2+125 and SCREEN_HEIGHT/2+70 <= mouse[1] <= SCREEN_HEIGHT/2+130:
                home_running = False
                instructions_running = True


    surf.blit(backing, (0, 0))
    if SCREEN_WIDTH/2-125 <= mouse[0] <= SCREEN_WIDTH/2+125 and SCREEN_HEIGHT/2+150 <= mouse[1] <= SCREEN_HEIGHT/2+210:
        pygame.draw.rect(surf,(0,0,0), [SCREEN_WIDTH/2-125,SCREEN_HEIGHT/2+150,250,60])
        surf.blit(quit_button_txt_2, (SCREEN_WIDTH / 2 -40, SCREEN_HEIGHT / 2 +150))
        pygame.draw.rect(surf, (255,255,255),[SCREEN_WIDTH/2-125,SCREEN_HEIGHT/2+70,250,60])
        surf.blit(srt_button_txt, (SCREEN_WIDTH/2 -55, SCREEN_HEIGHT/2 +70))

    elif SCREEN_WIDTH/2-125 <= mouse[0] <= SCREEN_WIDTH/2+125 and SCREEN_HEIGHT/2+70 <= mouse[1] <= SCREEN_HEIGHT/2+130:
        pygame.draw.rect(surf, (255,255,255),[SCREEN_WIDTH/2-125,SCREEN_HEIGHT/2+150,250,60])
        surf.blit(quit_button_txt, (SCREEN_WIDTH/2 -40, SCREEN_HEIGHT/2 +150))
        pygame.draw.rect(surf, (0,0,0),[SCREEN_WIDTH/2-125,SCREEN_HEIGHT/2+70,250,60])
        surf.blit(srt_button_txt_2, (SCREEN_WIDTH/2 -55, SCREEN_HEIGHT/2 +70))
    else:
        pygame.draw.rect(surf, (255,255,255),[SCREEN_WIDTH/2-125,SCREEN_HEIGHT/2+150,250,60])
        surf.blit(quit_button_txt, (SCREEN_WIDTH/2 -40, SCREEN_HEIGHT/2 +150))
        pygame.draw.rect(surf, (255,255,255),[SCREEN_WIDTH/2-125,SCREEN_HEIGHT/2+70,250,60])
        surf.blit(srt_button_txt, (SCREEN_WIDTH/2 -55, SCREEN_HEIGHT/2 +70))


def draw_background(surf):
    walls = pygame.image.load("images/bg_tile_up.png").convert()
    floor = pygame.image.load("images/bg_tile.png").convert()

    #make PNGs transparent
    walls.set_colorkey((0,0,0))
    floor.set_colorkey((0, 0, 0))


    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            surf.blit(walls, (x,y))


    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, int(SCREEN_HEIGHT/3)):
            surf.blit(floor, (x, y))
