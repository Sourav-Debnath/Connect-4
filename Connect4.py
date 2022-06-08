import pygame as pg
import numpy as np
import sys
import math

ROWS = 6
COLUMNS = 7
COLOR_BLUE = (0, 0, 255)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_BLACK = (0, 0, 0)

def create_board():
    board = np.zeros((ROWS,COLUMNS))
    return board

def print_board(game_board):
    print(np.flip(game_board, 0))

def valid_move(game_board, column):
    return game_board[ROWS-1][column] == 0

def get_location(game_board, column):
    for row in range(ROWS):
        if game_board[row][column] == 0:
            return row

def set_piece(game_board, row, column, player):
    game_board[row][column] = player

def get_winner(game_board, player):
    for row in range(ROWS-3):
        for column in range(COLUMNS):
            if game_board[row][column] == player and game_board[row+1][column] == player and game_board[row+2][column] == player and game_board[row+3][column] == player:
                return True

    for row in range(ROWS):
        for column in range(COLUMNS-3):
            if game_board[row][column] == player and game_board[row][column+1] == player and game_board[row][column+2] == player and game_board[row][column+3] == player:
                return True

    for row in range(ROWS-3):
        for column in range(COLUMNS-3):
            if game_board[row][column] == player and game_board[row+1][column+1] == player and game_board[row+2][column+2] == player and game_board[row+3][column+3] == player:
                return True

    for row in range(3, ROWS):
        for column in range(COLUMNS-3):
            if game_board[row][column] == player and game_board[row-1][column+1] == player and game_board[row-2][column+2] == player and game_board[row-3][column+3] == player:
                return True

def draw_board(game_board):
    for row in range(ROWS):
        for column in range(COLUMNS):
            pg.draw.rect(screen, COLOR_BLUE, (column * BOX_SIZE, row * BOX_SIZE + BOX_SIZE, BOX_SIZE, BOX_SIZE))
            pg.draw.circle(screen, COLOR_WHITE, (int(column*BOX_SIZE+BOX_SIZE/2), int(row*BOX_SIZE+BOX_SIZE+BOX_SIZE/2)), RADIOUS)
            
    for row in range(ROWS):
        for column in range(COLUMNS):
            if game_board[row][column] == 1:
                pg.draw.circle(screen, COLOR_RED, (int(column*BOX_SIZE+BOX_SIZE/2), height-int(row*BOX_SIZE+BOX_SIZE/2)), RADIOUS)
            elif game_board[row][column] == 2:
                pg.draw.circle(screen, COLOR_YELLOW, (int(column*BOX_SIZE+BOX_SIZE/2), height-int(row*BOX_SIZE+BOX_SIZE/2)), RADIOUS)
    pg.display.update()

game_board = create_board()

game_finish = False
turn = 1

pg.init()

BOX_SIZE = 120
RADIOUS = int(BOX_SIZE/2 - 10)

height = (ROWS+1) * BOX_SIZE
width = (COLUMNS) * BOX_SIZE

size = (width, height)

screen = pg.display.set_mode(size)
draw_board(game_board)

set_font = pg.font.SysFont("Times New Roman", 75)

while not game_finish:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

        if event.type == pg.MOUSEBUTTONDOWN:
            x_position = event.pos[0]
            column = int(math.floor((x_position)/BOX_SIZE))

            if turn == 1:
                if valid_move(game_board, column):
                    row = get_location(game_board, column)
                    set_piece(game_board, row, column, 1)

                    if get_winner(game_board,1):
                        label = set_font.render("RED WINS", 1, COLOR_BLUE)
                        screen.blit(label, (250,10))
                        game_finish = True
                        break

                turn = 2

            else:
                if valid_move(game_board, column):
                    row = get_location(game_board, column)
                    set_piece(game_board, row, column, 2)

                    if get_winner(game_board,2):
                        label = set_font.render("YELLOW WINS", 1, COLOR_BLUE)
                        screen.blit(label, (200,10))
                        game_finish = True
                        break

                    turn = 1

        if event.type ==pg.MOUSEMOTION:
            pg.draw.rect(screen, COLOR_BLACK, (0,0, width, BOX_SIZE))
            x_position = event.pos[0]
            if turn == 1:
                pg.draw.circle(screen, COLOR_RED, (x_position, int(BOX_SIZE/2)), RADIOUS)
            else:
                pg.draw.circle(screen, COLOR_YELLOW, (x_position, int(BOX_SIZE/2)), RADIOUS)
        pg.display.update()

    draw_board(game_board)

    if game_finish:
        pg.time.wait(4000)