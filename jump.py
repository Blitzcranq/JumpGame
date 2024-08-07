# -*- coding: utf-8 -*-
"""
Created on Mon May 27 20:38:22 2024

@author: QureshiHasan
"""

import pygame
import random
import time 


pygame.init()
win = pygame.display.set_mode((1200,820))
pygame.display.set_caption("JUMP GAME")

screen_width = 1200
screen_height = 820

font = pygame.font.SysFont(None,70)
menu_font = pygame.font.SysFont(None,30)
font_3 = pygame.font.SysFont(None,50)
font_4 = pygame.font.SysFont(None,80)
wingding = pygame.font.SysFont('Wingdings',80)

white=(255,255,255,255)

red = (255,0,0)

player_size = 7
rectangle_count = 50
square_width = 31
square_height = 31
blue = (0,0,255)
green = (0,255,0)
yellow = (255,255,0)
black = (0,0,0)
ct = [(255,255,0),(0,255,255)]     
score = [0,0]
level_running=True
gridsize = 10
rectangle_count = 50
square_width = 31
square_height = 31
colors = {"red":(255,0,0,255),
            "green":(0,255,0,255),
            "blue":(0,0,255,255),
            "white":(255,255,255,255),
            "black":(0,0,0,255)
            }
half = 600  


def check_overlap(position, squares):
    for square in squares:
        if position.colliderect(square):
            return True
    return False

def generate_position(squares):
    while True:
            grid_x = random.randint(0, (screen_width // gridsize) - 1) * gridsize
            grid_y = random.randint(0, (600 // gridsize) - 1) * gridsize
            position = pygame.Rect(
                grid_x - player_size // 2,
                grid_y - player_size // 2,
                player_size,
                player_size
            )
            if not check_overlap(position, squares):
                return position
       

def initialze_players():
    global players, player_marker, player2_marker, blue_square, green_square, squares, x_pos, y_pos, x_vel, y_vel, old_x_vel, old_y_vel, turn, score, colors, blue_flag, red_flag, green_flag, pot, gridsize
    x_vel = [0, 0]
    y_vel = [0, 0]
    old_x_vel = [0, 0]
    old_y_vel = [0, 0]
    x_pos = [0,0]
    y_pos = [0,0]
    blue_flag = [False,False]
    red_flag = [False,False]
    green_flag = [False,False]
    turn = 0
    pot = 0

def running_game(fixed="false"):
    initialze_players()
    global players, player_marker, player2_marker, blue_square, green_square, squares, x_pos, y_pos, x_vel, y_vel, old_x_vel, old_y_vel, turn, score, colors, blue_flag, red_flag, green_flag, pot, gridsize

    if fixed == "true":
        for x in range(10, 1200, gridsize):
            for y in range(10, 600, gridsize):
                win.set_at((x, y), white)
        blue_square = pygame.Rect(100,50,square_height,square_width)
        green_square = pygame.Rect(100,290,square_height,square_width)
        red_square = pygame.Rect(200,290,square_height,square_width)
        player_marker = pygame.Rect(100 - player_size // 2,570 - player_size // 2,player_size,player_size)
        player2_marker = pygame.Rect(100 - player_size // 2,530 - player_size // 2,player_size,player_size)
        pygame.draw.rect(win,black,(10,400,1200-100,95))
        pygame.draw.rect(win,black,(10,120,1200-100,95))
        pygame.draw.rect(win,black,(600,340,300,95))
        pygame.draw.rect(win,black,(600,175,300,95))
        pygame.draw.rect(win,red,red_square)
    else:
        blue_square = pygame.Rect(random.randint(0, screen_width-square_width) // gridsize * gridsize,random.randint(0, 600-square_height) // gridsize * gridsize,square_height,square_width)
        green_square = pygame.Rect(random.randint(0, screen_width-square_width) // gridsize * gridsize,random.randint(0, 600-square_height) // gridsize * gridsize,square_height,square_width)
        squares = []
        for _ in range(rectangle_count):
            x_position = random.randint(0, screen_width-square_width) // gridsize * gridsize
            y_position = random.randint(0, 600-square_height) // gridsize * gridsize
            squares.append(pygame.Rect(x_position,y_position,square_height,square_width))
        
        for x in range(10, 1200, gridsize):
            for y in range(10, 600, gridsize):
                win.set_at((x, y), white)
            
        for rect in squares:
            pygame.draw.rect(win, red, rect)  
        player_marker = generate_position(squares)
        player2_marker = generate_position(squares)

    pygame.draw.rect(win,blue,blue_square)
    pygame.draw.rect(win,green,green_square)
    
    # Generate initial positions for players without overlapping obstacles
    
    players = [player_marker, player2_marker]
    x_pos = [player_marker.x, player2_marker.x]
    y_pos = [player_marker.y, player2_marker.y]

def explosion(x,y):
    explosion_shades = [
        (255, 0, 0),       # Red
        (255, 69, 0),      # Red-Orange
        (255, 99, 71),     # Tomato
        (255, 127, 80),    # Coral
        (255, 140, 0),     # Dark Orange
        (255, 165, 0),     # Orange
        (255, 179, 71),    # Orange-Yellow
        (255, 215, 0),     # Gold
        (255, 223, 0),     # Golden Yellow
        (255, 239, 0),     # Yellow-Gold
        (255, 255, 0),     # Yellow
        (255, 255, 102),   # Light Yellow
        (255, 255, 153),   # Very Light Yellow
        (255, 69, 0),      # Orange Red
        (255, 0, 102),     # Deep Red
        (255, 99, 71)      # Tomato (Red-Orange)
        ]
    delay = 0.01 
    max_length = 60  
    num_steps = 20  

    for step in range(num_steps):

        for _ in range(30):  
            length = random.uniform(0, max_length)
            x2 = x + length * random.uniform(-1, 1)
            y2 = y + length * random.uniform(-1, 1)
            
            pygame.draw.line(win, random.choice(explosion_shades), (x, y), (x2, y2), 2)

        pygame.draw.circle(win, black, (x, y), 30) 
        pygame.time.delay(int(delay * 500))
        pygame.display.update()

def instructions():

    text = font.render("Welcome to Jump", True, (0,255,255))
    text_2 = menu_font.render("- The object of this game is to navigate from the starting position to the blue and green squares,", True, (0,255,255))
    text_3 = menu_font.render("before your opponent does.", True, (0,255,255))
    text_4 = menu_font.render("- You may change your velocity by one increment (up or down) each time you make a move. You must increase", True, (0,255,255))
    text_5 = menu_font.render("velocity, (up/down/left/right) by only enough to get you to the goal and not go crashing past it.", True, (0,255,255))
    text_6 = menu_font.render("- The first player to navigate from the start to the blue to the green will get the points equivalent to the number of", True, (0,255,255))
    text_7 = menu_font.render("moves the game lasts.", True, (0,255,255))
    text_8 = menu_font.render("- If you go over a boundary, or crash into a red rectangle, you will lose 10 points, and your opponent will win", True, (0,255,255))
    text_9 = menu_font.render("that round", True, (0,255,255))
    text_12 = menu_font.render("- Once game has begun, press 'n' to generate new track", True, (0,255,255))
    text_10 = font_4.render("- Press 1 for random track.", True, (0,255,255))
    text_11 = font_4.render("- Press 2 for fixed track", True, (0,255,255))

    #that round
    textRect = text.get_rect()
    textRect.center = (screen_width // 5, screen_height // 20)
    text_2Rect = text.get_rect()
    text_2Rect.center = (screen_width // 5, screen_height // 4)
    text_3Rect = text.get_rect()
    text_3Rect.center = (screen_width // 5, screen_height // 3.5)
    text_4Rect = text.get_rect()
    text_4Rect.center = (screen_width // 5, screen_height // 3)
    text_5Rect = text.get_rect()
    text_5Rect.center = (screen_width // 5, screen_height // 2.7)
    text_6Rect = text.get_rect()
    text_6Rect.center = (screen_width // 5, screen_height // 2.4)
    text_7Rect = text.get_rect()
    text_7Rect.center = (screen_width // 5, screen_height // 2.2)
    text_8Rect = text.get_rect()
    text_8Rect.center = (screen_width // 5, screen_height // 2)
    text_9Rect = text.get_rect()
    text_9Rect.center = (screen_width // 5, screen_height // 1.85)
    text_12Rect = text.get_rect()
    text_12Rect.center = (screen_width // 5, screen_height // 1.7)
    text_10Rect = text.get_rect()
    text_10Rect.center = (screen_width // 5, screen_height // 1.5)
    text_11Rect = text.get_rect()
    text_11Rect.center = (screen_width // 5, screen_height // 1.35)
    return text, textRect, text_2, text_2Rect, text_3, text_3Rect, text_4, text_4Rect, text_5, text_5Rect, text_6, text_6Rect, text_7, text_7Rect, text_8, text_8Rect, text_9, text_9Rect, text_12, text_12Rect, text_10, text_10Rect, text_11, text_11Rect

def movement(player, key):
    global x_vel, y_vel, old_x_vel, old_y_vel, key_pressed

    if key == pygame.K_UP:
        y_vel[player] = max(y_vel[player] - 1, old_y_vel[player]-1)
    elif key == pygame.K_DOWN:
        y_vel[player] = min(y_vel[player] + 1, old_y_vel[player]+1)
    elif key == pygame.K_LEFT:
        x_vel[player] = max(x_vel[player] - 1, old_x_vel[player]-1)
    elif key == pygame.K_RIGHT:
        x_vel[player] = min(x_vel[player] + 1, old_x_vel[player]+1)

    
def consequences (x,y,turn):
    x = x + player_size // 2
    y = y + player_size // 2
    if x < 0 or x >= screen_width or y < 0 or y >= screen_height:
        red_flag[turn] = True
        explosion(x, y)
        score[turn] -= 10
        score[1 - turn] += pot
    else:
        color = win.get_at((x,y))
        if color == colors["white"] :
            print("grey")
        elif color == colors["blue"] :
            print("blue")
            blue_flag[turn] = True
        elif color == colors["green"] :
            print("green")
            if blue_flag[turn] == True:
                green_flag[turn] = True
                score[turn] += pot
        elif color == colors["red"] or color == colors["black"]:
            print("red")
            explosion(x, y)
            red_flag[turn] = True
            score[turn] -= 10
            score[1 - turn] += pot
            

def run_level(fixed="false"):
    global level_running, run, turn, pot
    while level_running:
            
            # Quit the game if the close button is clicked
            for event in pygame.event.get():
                # uses the "pygame.QUIT" function to close the box
                if event.type == pygame.QUIT:
                    level_running = False
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        win.fill((0,0,0))
                        running_game(fixed)
                    if event.key == pygame.K_RETURN:  # Update player position and switch turn if 'ENTER' is pressed
                        if green_flag[turn] == True or red_flag[turn] == True :
                            win.fill((0,0,0))
                            running_game(fixed)
                        else:
                            pot += 1
                            # Updates player position based on current velocity
                            # *gridsize makes the marker stay on the gridpoints
                            x_pos[turn] += (x_vel[turn] * gridsize)
                            y_pos[turn] += (y_vel[turn] * gridsize)
                            consequences(x_pos[turn],y_pos[turn],turn)
                            # Updating player marker positon
                            players[turn].x = x_pos[turn]
                            players[turn].y = y_pos[turn]
                            # stores the current velocity and setting it to old velocity
                            # then switches the turn of the players
                            old_x_vel[turn] = x_vel[turn]
                            old_y_vel[turn] = y_vel[turn]
                            if not green_flag[turn] and not red_flag[turn]: 
                                turn = 1 - turn
                        
                    elif event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                        movement(turn, event.key)
            pygame.display.update() 

                
            for player in [0, 1]:
                pygame.draw.rect(win, black, (player * half + 330, 700, 100, 100))
                pygame.draw.rect(win, black, (player * half + 120, 700, 100, 100))
                
                pygame.draw.rect(win, black, (player * half + 490, 700, 100, 100))
                
                score_num =  font_3.render(str(int(score[player])), True, ct[player], black)
                win.blit(score_num, (player * half + 490, 700))

                # Draws player markers
                pygame.draw.rect(win, ct[player], players[player])

                # Draws player boxes
                # if its the players turn, it will draw the player box around it
                # ct[player] makes it so that the color of the box matches the player

                if player == turn:
                    pygame.draw.rect(win, ct[player], (player * half + 10, 600 + 10, 580, 200), 2)

                # When not the players turn, sets the player box to black, i.e, erasing it
                else:
                    pygame.draw.rect(win, black, (player * half + 10, 600 + 10, 580, 200), 2)
                
                # draws blug flag if player lands on blue square
                if blue_flag[player] == True:
                    pygame.draw.rect(win,blue,(player * half + 250, 625, 30, 30))
                    
                # draws green flag if player lands on green square after blue square
                if green_flag[player] == True:
                    pygame.draw.rect(win,green,(player * half + 250, 625, 30, 30))
                    score[player] += pot
                    score_num =  font_3.render(str(int(score[player])), True, ct[player], black)
                    win.blit(score_num, (player * half + 490, 700))
                   
                if red_flag[player] == True:
                    pygame.draw.rect(win,red,(player * half + 250, 625, 30, 30))
                    pygame.draw.rect(win, black, players[player])
                    # explosion

                    
                # Draw control arrows and player labels
                
                if y_vel[player] <= 0:
                    arrow_y = wingding.render(chr(0xE9), True, ct[player], black)
                else:
                    arrow_y = wingding.render(chr(0xEA),True,ct[player],black)
                win.blit(arrow_y, (player * half + 40, 670))
                
                if x_vel[player] <= 0 :
                    arrow_x = wingding.render(chr(0xE7), True, ct[player], black)
                else:
                    arrow_x = wingding.render(chr(0xE8),True,ct[player],black)
                win.blit(arrow_x, (player * half + 235, 670))

                
                player_text = font.render("Player " + str(player + 1), True, ct[player], black)
                win.blit(player_text, (player * half + 25, 625))

                score_text = font.render("Score", True, ct[player], (0, 0, 0))
                win.blit(score_text, (player * half + 440, 625))

                # Display player velocities
                velleft_text = font_3.render(str(abs(int(x_vel[player]))), True, ct[player], black)
                win.blit(velleft_text, (player * half + 330, 700))

                velup_text = font_3.render(str(abs(int(y_vel[player]))), True, ct[player], black)
                win.blit(velup_text, (player * half + 120, 700))
                

run = True
while run:
    # Quit the game if the close button is clicked
    for event in pygame.event.get():
        # uses the "pygame.QUIT" function to close the box
        if event.type == pygame.QUIT:
            run = False 
    win.fill((0,0,0))
    
   # Display instructions using a for loop
    text, textRect, text_2, text_2Rect, text_3, text_3Rect, text_4, text_4Rect, text_5, text_5Rect, text_6, text_6Rect, text_7, text_7Rect, text_8, text_8Rect, text_9, text_9Rect, text_12, text_12Rect, text_10, text_10Rect, text_11, text_11Rect = instructions()
    win.blit(text, textRect)
    win.blit(text_2, text_2Rect)
    win.blit(text_3, text_3Rect)
    win.blit(text_4, text_4Rect)
    win.blit(text_5, text_5Rect)
    win.blit(text_6, text_6Rect)
    win.blit(text_7, text_7Rect)
    win.blit(text_8, text_8Rect)
    win.blit(text_9, text_9Rect)
    win.blit(text_12, text_12Rect)
    win.blit(text_10, text_10Rect)
    win.blit(text_11, text_11Rect)


    pygame.display.update() 
    keys = pygame.key.get_pressed()

    if keys[pygame.K_1]:
        win.fill((0,0,0))
        running_game("false")
        run_level()
    if keys[pygame.K_2]:
        win.fill((0,0,0))
        running_game("true")
        run_level("true")   
        
pygame.display.update()    
print ('done')
pygame.quit()
