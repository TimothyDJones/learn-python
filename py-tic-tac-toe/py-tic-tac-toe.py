# PyGame Tic Tac Toe
# https://techvidvan.com/tutorials/python-game-project-tic-tac-toe/

import pygame as pg, sys
from pygame.locals import *
import time

# initialize global variables
XO = 'x'
winner = None
draw = False
width, height = 400, 400
white = (255, 255, 255)
line_color = (10, 10, 10)

# 3x3 Tic Tac Toe board
TTT = [[None] * 3, [None] * 3, [None] * 3]

# initialize game window
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height + 100), 0, 32)
pg.display.set_caption("Tic Tac Toe")

# load images
opening = pg.image.load('tic tac opening.png')
x_img = pg.image.load('X.png')
o_img = pg.image.load('O.png')

# resizing images
opening = pg.transform.scale(x_img, (width, height + 100))
x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(o_img, (80, 80))

def game_opening():
    # Display splash screen
    screen.blit(opening, (0, 0))
    pg.display.update()
    time.sleep(1)
    screen.fill(white)
    
    # Draw board
    # Vertical lines
    pg.draw.line(screen, line_color, (width/3, 0), (width/3, height), 7)
    pg.draw.line(screen, line_color, (width/3*2, 0), (width/3*2, height), 7)
    # Horizontal lines
    pg.draw.line(screen, line_color, (0, height/3), (width, height/3), 7)
    pg.draw.line(screen, line_color, (0, height/3*2), (width, height/3*2), 7)
    # Display status panel
    draw_status()

def draw_status():
    global draw
    
    if winner is None:
        message = XO.upper() + "'s turn"
    else:
        message = winner.upper() + " won!"
    if draw:
        message = "Game is a draw."
    
    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))
    
    # Display the rendered message on the status panel
    screen.fill((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width/2, 500-50))
    screen.blit(text, text_rect)
    pg.display.update()
    
def check_win():
    global TTT, winner, draw
    
    # check for winner on rows
    for row in range(0, 3):
        if ((TTT[row][0] == TTT[row][1] == TTT[row][2]) and (TTT[row][0] is not None)):
            winner = TTT[row][0]
            pg.draw.line(screen, (250, 0, 0), (0, (row + 1)*height/3 - height/6), \
            (width, (row + 1)*height/3 - height/6), 4)
            break

    # check for winner on columns
    for col in range(0, 3):
        if ((TTT[0][col] == TTT[1][col] == TTT[2][col]) and (TTT[0][col] is not None)):
            winner = TTT[0][col]
            pg.draw.line(screen, (250, 0, 0), ((col + 1)*width/3 - width/6, 0),\
            ((col + 1)*width/3 - width/6, height), 4)
            break

    # check for winner on diagonals
    if ((TTT[0][0] == TTT[1][1] == TTT[2][2]) and (TTT[0][0] is not None)):
        # Game won on left-to-right diagonal
        winner = TTT[0][0]
        pg.draw.line(screen, (250, 70, 70), (50, 50), (350, 350), 4)
    if ((TTT[0][2] == TTT[1][1] == TTT[2][0]) and (TTT[0][2] is not None)):
        # Game won on right-to-left diagonal
        winner = TTT[0][2]
        pg.draw.line(screen, (250, 70, 70), (350, 50), (50, 350), 4)
    
    # check for draw
    if (all([all(row) for row in TTT]) and winner is None):
        draw = True
    draw_status()

def drawXO(row, col):
    global TTT, XO
    
    posx = 30 + width/3*(row - 1)
    posy = 30 + height/3*(col - 1)
    TTT[row-1][col-1] = XO
    if (XO == 'x'):
        screen.blit(x_img, (posy, posx))
        XO = 'o'
    else:
        screen.blit(o_img, (posy, posx))
        XO = 'x'
    pg.display.update()
    
def userClick():
    # Get coordinates of user click
    x, y = pg.mouse.get_pos()
    print(x, y)
    
    # get column (1-3) of mouse click
    if (x < width/3):
        col = 1
    elif (x < width/3*2):
        col = 2
    elif (x < width):
        col = 3
    else:
        col = None

    # get row (1-3) of mouse click
    if (y < height/3):
        row = 1
    elif (y < height/3*2):
        row = 2
    elif (y < height):
        row = 3
    else:
        row = None
    
    if (row and col and TTT[row-1][col-1] is None):
        global XO
        
        drawXO(row, col)
        check_win()
        
def reset_game():
    global TTT, winner, XO, draw
    time.sleep(3)
    XO = 'x'
    draw = False
    winner = None
    game_opening()
    TTT = [[None] * 3, [None] * 3, [None] * 3]

# Run game
game_opening()

# Main game loop
while (True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type is MOUSEBUTTONDOWN:
            # mouse button clicked
            userClick()
            if (winner or draw):
                reset_game()
                
    pg.display.update()
    CLOCK.tick(fps)
