import numpy as np
import pygame
import sys
import math
from random import randint

NUM_ROWS = 6
NUM_COLS = 7

BLUE = (0, 0, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (255, 255, 255)


def create_board():
    board = np.zeros((NUM_ROWS, NUM_COLS))
    return board


def play_stone(board, row, cols, stone):
    board[row][cols] = stone


def is_valid_pos(board, cols):
    return board[NUM_ROWS - 1][cols] == 0


def get_open_row(board, cols):
    for row in range(NUM_ROWS):
        if board[row][cols] == 0:
            return row


def print_reverse(board):
    print(np.flip(board, 0))


def Wins(board, stone):
    for c in range(NUM_COLS):
        for r in range(NUM_ROWS - 3):
            if board[r][c] == stone and board[r + 1][c] == stone and board[r + 2][c] == stone and board[r + 3][
                c] == stone:
                return c, r, c, r + 3, True

    for c in range(NUM_COLS - 3):
        for r in range(NUM_ROWS):
            if board[r][c] == stone and board[r][c + 1] == stone and board[r][c + 2] == stone and board[r][
                c + 3] == stone:
                return c, r, c + 3, r, True

    for c in range(NUM_COLS - 3):
        for r in range(NUM_ROWS - 3):
            if board[r][c] == stone and board[r + 1][c + 1] == stone and board[r + 2][c + 2] == stone and board[r + 3][
                c + 3] == stone:
                return c, r, c + 3, r + 3, True

    for c in range(NUM_COLS - 3):
        for r in range(NUM_ROWS):
            if board[r][c] == stone and board[r - 1][c + 1] == stone and board[r - 2][c + 2] == stone and board[r - 3][
                c + 3] == stone:
                return c, r, c + 3, r - 3, True
    return 0, 0, 0, 0, False


def draw_board(board):
    for c in range(NUM_COLS):
        for r in range(NUM_ROWS):
            pygame.draw.rect(screen, YELLOW, (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, BLACK, (
            int(c * SQUARE_SIZE + SQUARE_SIZE / 2), int(r * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)

    for c in range(NUM_COLS):
        for r in range(NUM_ROWS):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (
                int(c * SQUARE_SIZE + SQUARE_SIZE / 2), height - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, BLUE, (
                    int(c * SQUARE_SIZE + SQUARE_SIZE / 2), height - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)

    pygame.display.update()


board = create_board()
game_over = False
turn = 0

pygame.init()
SQUARE_SIZE = 100

width = NUM_COLS * SQUARE_SIZE
height = (NUM_ROWS + 1) * SQUARE_SIZE

size = (width, height)

RADIUS = int(SQUARE_SIZE / 2 - 5)

screen = pygame.display.set_mode(size)

draw_board(board)
pygame.display.update()

fontDisplay = pygame.font.SysFont("monospace", 65)

while not game_over:
    # pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        draw_board(board)
        pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))
        if turn == 0:
            cols = randint(0, 6)
            while (not is_valid_pos(board, cols)):
                print
                cols
                cols = randint(0, 6)
            row = get_open_row(board, cols)
            play_stone(board, row, cols, 1)
            label = fontDisplay.render("Player 1 Moves", 1, RED)
            screen.blit(label, (40, 15))
            x1, y1, x2, y2, win = Wins(board, 1)
            if (win == True):
                screen.fill((0, 0, 0))
                label = fontDisplay.render("Player 1 Won!!", 1, RED)
                screen.blit(label, (40, 15))
                draw_board(board)
                pygame.draw.line(screen, GREEN, (
                int(x1 * SQUARE_SIZE + SQUARE_SIZE / 2), height - int(y1 * SQUARE_SIZE + SQUARE_SIZE / 2)), ((
                int(x2 * SQUARE_SIZE + SQUARE_SIZE / 2), height - int(y2 * SQUARE_SIZE + SQUARE_SIZE / 2))), 10)
                pygame.display.update()
                game_over = True
        else:
            cols = randint(0, 6)
            while (not is_valid_pos(board, cols)):
                print
                cols
                cols = randint(0, 6)
            row = get_open_row(board, cols)
            play_stone(board, row, cols, 2)
            label = fontDisplay.render("Player 2 Moves", 1, BLUE)
            screen.blit(label, (40, 15))
            x1, y1, x2, y2, win = Wins(board, 2)
            if (win == True):
                label = fontDisplay.render("Player 2 Won!!", 1, BLUE)
                screen.fill((0, 0, 0))
                screen.blit(label, (40, 15))
                draw_board(board)
                pygame.draw.line(screen, GREEN, (
                int(x1 * SQUARE_SIZE + SQUARE_SIZE / 2), height - int(y1 * SQUARE_SIZE + SQUARE_SIZE / 2)), ((
                int(x2 * SQUARE_SIZE + SQUARE_SIZE / 2), height - int(y2 * SQUARE_SIZE + SQUARE_SIZE / 2))), 10)
                pygame.display.update()
                game_over = True
        pygame.time.wait(1000)
        turn += 1
        turn = turn % 2
pygame.time.wait(5000)
