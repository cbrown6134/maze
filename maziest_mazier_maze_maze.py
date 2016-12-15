# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
WIDTH = 1200
HEIGHT = 950
SIZE = (WIDTH, HEIGHT)
TITLE = "Maziest Mazier Maze Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (168, 8, 29)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (33, 138, 140)
GRAY = (198, 175, 192)

#Fonts
MY_FONT = pygame.font.Font(None, 50)

#Images
img = pygame.image.load('splashscreen4.png')
img2 = pygame.image.load('Untitled.png')

#stages
START = 0
PLAYING = 1
END = 2

# Make a player
player = [530, 0, 25, 25] 
player_vx = 0
player_vy = 0
player_speed = 5

# make walls
wall1 = [500, 250, 200, 20]
wall2 = [500, 350, 290, 20]
wall3 = [90, 80, 20, 120]
wall4 = [0, 0, 500, 20]
wall5 = [0, 0, 20, 860]
wall6 = [0, 930, 750, 20]
wall7 = [90, 80, 90, 20]
wall8 = [250, 0, 20, 100]
wall9 = [420, 0, 20, 100]
wall_10 = [600, 0, 650, 20]
wall_11 = [1180, 0, 20, 860]
wall_12 = [850, 930, 370, 20]
wall_13 = [90, 180, 420, 20]
wall_14 = [330, 90, 20, 100]
wall_15 = [500, 100, 20, 160]
wall_16 = [600, 0, 20, 250]
wall_17 = [0, 280, 415, 20]
wall_18 = [395, 280, 20, 450]
wall_19 = [90, 375, 20, 200]
wall_20 = [90, 375, 220, 20]
wall_21 = [290, 375, 20, 100]
wall_22 = [195, 475, 115, 20]
wall_23 = [90, 575, 220, 20]
wall_24 = [90, 680, 20, 150]
wall_25 = [90, 680, 120, 20]
wall_26 = [840, 80, 650, 20]
wall_27 = [720, 80, 20, 115]
wall_28 = [720, 175, 360, 20]
wall_29 = [1000, 275, 80, 20]
wall_30 = [1000, 275, 20, 90]
wall_31 = [790, 175, 20, 195]
wall_32 = [1000, 360, 200, 20]
wall_33 = [1000, 460, 90, 20]
wall_34 = [1000, 460, 20, 200]
wall_35 = [1100, 550, 150, 20]
wall_36 = [850, 860, 20, 150]
wall_37 = [170, 790, 20, 250]
wall_38 = [290, 840, 800, 20]
wall_39 = [290, 575, 20, 280]
wall_40 = [395, 730, 105, 20]
wall_41 = [500, 590, 20, 160]
wall_42 = [500, 350, 20, 140]
wall_43 = [500, 590, 150, 20]
wall_44 = [630, 540, 20, 60]
wall_45 = [630, 540, 285, 20]
wall_46 = [895, 175, 20, 485]
wall_47 = [895, 650, 210, 20]
wall_48 = [730, 460, 20, 210]
wall_49 = [630, 730, 200, 20]
wall_50 = [630, 680, 20, 60]
wall_51 = [810, 650, 20, 90]
wall_52 = [1000, 655, 20, 110]
wall_53 = [720, 730, 20, 110]
wall_54 = [590, 450, 60, 20]


walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall_10,
         wall_11, wall_12, wall_13, wall_14, wall_15, wall_16, wall_17, wall_18,
         wall_19, wall_20, wall_21, wall_22, wall_23, wall_24, wall_25, wall_26,
         wall_27, wall_28, wall_29, wall_30, wall_31, wall_32, wall_33, wall_34,
         wall_35, wall_36, wall_37, wall_38, wall_39, wall_40, wall_41, wall_42,
         wall_43, wall_44, wall_45, wall_46, wall_47, wall_48, wall_49, wall_50,
         wall_51, wall_52, wall_53, wall_54]

# Make coins
coin1 = [130, 140, 15, 15]
coin2 = [400, 240, 15, 15]
coin3 = [290, 530, 15, 15]
coin4 = [340, 50, 15, 15]
coin5 = [410, 140, 15, 15]
coin6 = [550, 190, 15, 15]
coin7 = [50, 210, 15, 15]
coin8 = [50, 50, 15, 15]
coin9 = [50, 470, 15, 15]
coin10 = [50, 340, 15, 15]
coin11 = [50, 860, 15, 15]
coin12 = [50, 550, 15, 15]
coin13 = [50, 700, 15, 15]
coin14 = [250, 700, 15, 15]
coin16 = [250, 335, 15, 15]
coin17 = [450, 300, 15, 15]
coin18 = [450, 450, 15, 15]
coin19 = [450, 600, 15, 15]
coin20 = [450, 790, 15, 15]
coin21 = [450, 890, 15, 15]
coin22 = [345, 435, 15, 15]
coin23 = [345, 590, 15, 15]
coin24 = [345, 750, 15, 15]
coin25 = [345, 890, 15, 15]
coin26 = [250, 830, 15, 15]
coin27 = [130, 435, 15, 15]
coin28 = [130, 530, 15, 15]
coin29 = [250, 240, 15, 15]
coin30 = [900, 50, 15, 15]
coin31 = [1000, 50, 15, 15]
coin32 = [800, 50, 15, 15]
coin33 = [1100, 50, 15, 15]
coin34 = [670, 50, 15, 15]
coin35 = [1100, 900, 15, 15]
coin36 = [1100, 750, 15, 15]
coin37 = [1100, 500, 15, 15]
coin38 = [1100, 400, 15, 15]
coin39 = [1100, 310, 15, 15]
coin40 = [1100, 200, 15, 15]
coin41 = [800, 130, 15, 15]
coin42 = [800, 400, 15, 15]
coin43 = [800, 480, 15, 15]
coin44 = [800, 590, 15, 15]
coin45 = [800, 790, 15, 15]
coin46 = [670, 190, 15, 15]
coin47 = [670, 300, 15, 15]
coin48 = [670, 500, 15, 15]
coin49 = [670, 400, 15, 15]
coin50 = [670, 590, 15, 15]
coin51 = [670, 690, 15, 15]
coin52 = [670, 890, 15, 15]
coin53 = [550, 400, 15, 15]
coin54 = [550, 500, 15, 15]
coin55 = [550, 630, 15, 15]
coin56 = [550, 770, 15, 15]
coin57 = [550, 890, 15, 15]
coin58 = [950, 130, 15, 15]
coin59 = [950, 300, 15, 15]
coin60 = [950, 450, 15, 15]
coin61 = [950, 560, 15, 15]
coin62 = [950, 700, 15, 15]
coin63 = [950, 890, 15, 15]
coin64 = [950, 810, 15 ,15]
coin65 = [845, 240, 15, 15]
coin66 = [130, 340, 15, 15]
coin67 = [130, 640, 15, 15]
coin68 = [130, 740, 15, 15]
coin69 = [800, 890, 15, 15]

coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10,
        coin11, coin12, coin13, coin14, coin16, coin17, coin18, coin19,
        coin20, coin21, coin22, coin23, coin24, coin25, coin26, coin27, coin28,
        coin29, coin30, coin31, coin32, coin33, coin34, coin35, coin36, coin37,
        coin38, coin39, coin40, coin41, coin42, coin43, coin44, coin45, coin46,
        coin47, coin48, coin49, coin50, coin51, coin52, coin53, coin54, coin55,
        coin56, coin57, coin58, coin59, coin60, coin61, coin62, coin63, coin64,
        coin65, coin66, coin67, coin68, coin69]

# Make doors
black_door1 = [840, 0, 20, 90]
black_door2 = [1070, 840, 20, 200]
black_door3 = [500, 100, 100, 20]

black_doors = [black_door1, black_door2, black_door3]

# Make switch
black_switch = [250, 430, 25, 25]
gray_switch = [840, 200, 25, 25]

# Make collidables
collidables = walls + black_doors


def setup():
    global stage, coins, player, player_vx, player_vy, player_speed, goal, black_doors, collidables, doors_open, background_color, goal_color, black_door_color, black_switch_color, score, time_remaining, ticks, top, bottom, left, right, win 

    win = False

    top = player[1]
    
    bottom = player[1] + player[3]
    
    left = player[0]
    
    right = player[0] + player[2]

    time_remaining = 90
    
    ticks = 0

    score = 0

    background_color = WHITE

    goal_color = WHITE

    black_door_color = WHITE

    black_switch_color = WHITE

    doors_open = False

    black_doors = [black_door1, black_door2, black_door3]

    collidables = walls + black_doors
    
    goal = [750, 930, 100, 20]
    
    player = [530, 0, 25, 25] 
    player_vx = 0
    player_vy = 0
    player_speed = 5
    
    coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10,
            coin11, coin12, coin13, coin14, coin16, coin17, coin18, coin19,
            coin20, coin21, coin22, coin23, coin24, coin25, coin26, coin27, coin28,
            coin29, coin30, coin31, coin32, coin33, coin34, coin35, coin36, coin37,
            coin38, coin39, coin40, coin41, coin42, coin43, coin44, coin45, coin46,
            coin47, coin48, coin49, coin50, coin51, coin52, coin53, coin54, coin55,
            coin56, coin57, coin58, coin59, coin60, coin61, coin62, coin63, coin64,
            coin65, coin66, coin67, coin68, coin69]  
    
    stage = START

# Game loop
setup()
doors_open = False
background_color = WHITE
goal_color = WHITE
black_door_color =  WHITE
black_switch_color = WHITE
score = 0
win = False

done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            
            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
                  
            elif stage == END:
                if event.key == pygame.K_SPACE:
                    setup()

    if stage == PLAYING:
        pressed = pygame.key.get_pressed()

        up = pressed[pygame.K_UP]
        down = pressed[pygame.K_DOWN]
        left = pressed[pygame.K_LEFT]
        right = pressed[pygame.K_RIGHT]

        if up:
            player_vy = -player_speed
        elif down:
            player_vy = player_speed
        else:
            player_vy = 0
            
        if left:
            player_vx = -player_speed
        elif right:
            player_vx = player_speed
        else:
            player_vx = 0

        
    # Game logic (Check for collisions, update points, etc.)
    if stage == PLAYING:
        ''' move the player in horizontal direction '''
        player[0] += player_vx

        ''' resolve collisions horizontally '''
        for c in collidables:
            if intersects.rect_rect(player, c):        
                if player_vx > 0:
                    player[0] = c[0] - player[2]
                elif player_vx < 0:
                    player[0] = c[0] + c[2]

        ''' move the player in vertical direction '''
        player[1] += player_vy
        
        ''' resolve collisions vertically '''
        for c in collidables:
            if intersects.rect_rect(player, c):                    
                if player_vy > 0:
                    player[1] = c[1] - player[3]
                if player_vy < 0:
                    player[1] = c[1] + c[3]


        ''' here is where you should resolve player collisions with screen edges '''
        top = player[1]
        bottom = player[1] + player[3]
        left = player[0]
        right = player[0] + player[2]

        ''' get block edges (makes collision resolution easier to read) '''
        if top < 0:
            player[1] = 0
        elif bottom > HEIGHT:
            player[1] = HEIGHT - player[3]

        ''' if the block is moved completely off of the window, reposition it on the other side '''
        if bottom < 0:
            player[1] = HEIGHT
        elif top > HEIGHT:
            player[1] = 0 - player[3]

        if left > WIDTH:
            player[0] = 0 - player[2]
        elif right < 0:
            player[0] = WIDTH
           
        ''' end game collecting all the coins '''
        if len(coins) == 0 and intersects.rect_rect(player, goal):
            win = True

       
    ''' get the coins '''
    #coins = [c for c in coins if not intersects.rect_rect(player, c)]

    hit_list = [c for c in coins if intersects.rect_rect(player, c)]
    
    for hit in hit_list:
        coins.remove(hit)
        score += 1    


    ''' open door on switch contact '''
    if intersects.rect_rect(player, black_switch):
        doors_open = True

        collidables = [c for c in collidables if c not in black_doors]

    if intersects.rect_rect(player, gray_switch):
        background_color = GRAY
        goal_color = GRAY
        black_door_color = BLACK
        black_switch_color = BLACK

    ''' timer stuff '''
    if stage == PLAYING:
        ticks += 1

        if ticks % refresh_rate == 0:
            time_remaining -= 1

        if time_remaining == 0:
            stage = END

    
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(background_color)

    pygame.draw.rect(screen, goal_color, goal)

    pygame.draw.rect(screen, GRAY, gray_switch)

    screen.blit(img2, (player[0], player[1]))

    if not doors_open:
        for d in black_doors:
            pygame.draw.rect(screen, black_door_color, d)
    
    for w in walls:
        pygame.draw.rect(screen, BLUE, w)
    
    for c in coins:
        pygame.draw.rect(screen, WHITE, c)

    pygame.draw.rect(screen, black_switch_color, black_switch)
    

    ''' begin/end game text '''
    if stage == START:
        screen.blit(img, (0,0))
        text1 = MY_FONT.render("Maziest Mazier Maze Maze", True, BLACK)
        text2 = MY_FONT.render("(Press SPACE to play.)", True, BLACK)
        screen.blit(text1, [375, 400])
        screen.blit(text2, [415, 450])
    elif win == True:
        stage = END
        text1 = MY_FONT.render("You Won!", True, BLACK)
        text2 = MY_FONT.render("Game Over", True, BLACK)
        text3 = MY_FONT.render("(Press SPACE to restart.)", True, BLACK)
        screen.blit(text1, [446, 400])
        screen.blit(text2, [615, 400])
        screen.blit(text3, [415, 450])
    elif win == False and time_remaining == 0:
        text1 = MY_FONT.render("You Lose!", True, BLACK)
        text2 = MY_FONT.render("Game Over", True, BLACK)
        text3 = MY_FONT.render("(Press SPACE to restart.)", True, BLACK)
        screen.blit(text1, [440, 400])
        screen.blit(text2, [615, 400])
        screen.blit(text3, [415, 450])
    elif stage == PLAYING:
        text1 = MY_FONT.render(str(score), True, BLACK)
        screen.blit(text1, [0, 0])
        timer_text = MY_FONT.render(str(time_remaining), True, BLACK)
        screen.blit(timer_text, [1139, 0])
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
