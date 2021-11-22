# importing the necessary modules
import pygame
import sys
import numpy as np

# initializing the pygame module
pygame.init()

# defining constants
WIDTH = 600
HEIGHT = 600
BACKGROUND_COLOR = (47, 79, 79)
GRIDLINE_COLOR = (67, 99, 99)
GRIDLINE_WIDTH = 15
CROSS_COLOR = (250,128,114)
CROSS_WIDTH = 25
SPACE = 55
CIRCLE_COLOR = (65,105,225)
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15

# creating the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BACKGROUND_COLOR)

# setting up the board
board = np.zeros((3, 3))

# drawing the gridlines
def draw_gridlines():
    # draw first horizontal line
    pygame.draw.line(screen, GRIDLINE_COLOR, (0, 200), (600, 200), GRIDLINE_WIDTH)
    # draw second horizontal line
    pygame.draw.line(screen, GRIDLINE_COLOR, (0, 400), (600, 400), GRIDLINE_WIDTH)
    # draw first vertical line
    pygame.draw.line(screen, GRIDLINE_COLOR, (200, 0), (200, 600), GRIDLINE_WIDTH)
    # draw second vertical line
    pygame.draw.line(screen, GRIDLINE_COLOR, (400, 0), (400, 600), GRIDLINE_WIDTH)

# function to draw the circles and crosses
def draw_pieces():
    # for each row
    for row in range(3):
        # for each column in each row
        for col in range(3):
            # if the square is filled with a 1
            if board[row][col] == 1:
                # draw an X
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH)
            # if the square is filled with a 2
            elif board[row][col] == 2:
                # draw an O
                pygame.draw.circle(screen, CIRCLE_COLOR, (col * 200 + 100, row * 200 + 100), CIRCLE_RADIUS, CIRCLE_WIDTH)


# function to mark a chosen square
def mark_square(row, col, player):
    board[row][col] = player

# function to check if a square is available
def square_available(row, col):
    return board[row][col] == 0

# function to check if the board is full
def board_full():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return False
    return True

# function to check if there is a winner
def check_win(player):
    # vertical win check
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True
    # horizontal win check
    for row in range(3):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True
    # ascending diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_asc_diagonal(player)
        return True
    # descending diagonal win check
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        draw_desc_diagonal(player)
        return True
    
    return False

# function for the computer to check if there is a winning move for itself or the player
def comp_check_win(player):
    # vertical win check
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    # horizontal win check
    for row in range(3):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    # ascending diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    # descending diagonal win check
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

# function to draw the vertical winning line
def draw_vertical_winning_line(col, player):
	posX = col * 200 + 100

	if player == 1:
		color = CROSS_COLOR
	elif player == 2:
		color = CIRCLE_COLOR

	pygame.draw.line( screen, color, (posX, 15), (posX, HEIGHT - 15), 15 )

# function to draw the horizontal winning line
def draw_horizontal_winning_line(row, player):
	posY = row * 200 + 100

	if player == 1:
		color = CROSS_COLOR
	elif player == 2:
		color = CIRCLE_COLOR

	pygame.draw.line( screen, color, (15, posY), (WIDTH - 15, posY), 15 )

# function to draw the descending diagonal winning line
def draw_desc_diagonal(player):
	if player == 1:
		color = CROSS_COLOR
	elif player == 2:
		color = CIRCLE_COLOR

	pygame.draw.line( screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15 )

# function to draw the ascending diagonal winning line
def draw_asc_diagonal(player):
	if player == 1:
		color = CROSS_COLOR
	elif player == 2:
		color = CIRCLE_COLOR
        
	pygame.draw.line( screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15 )

# function to restart the game
def restart_game():
    screen.fill(BACKGROUND_COLOR)
    draw_gridlines()
    player = 1
    for row in range(3):
        for col in range(3):
            board[row][col] = 0

# function to determine the computer's move
def computer_play():
    #if the computer can win, make that move
    for row in range(3):
        for col in range(3):
            if square_available(row, col):
                mark_square(row, col, 2)
                if comp_check_win(2):
                    return row, col
                else:
                    board[row][col] = 0
    #if the player can win, block that move
    for row in range(3):
        for col in range(3):
            if square_available(row, col):
                mark_square(row, col, 1)
                if comp_check_win(1):
                    return row, col
                else:
                    board[row][col] = 0
    #if the center is available, take it
    if square_available(1, 1):
        return 1, 1
    #if the corners are available, take one of them
    else:
        for row in range(3):
            for col in range(3):
                if square_available(row, col):
                    return row, col

# main loop
def main():
    # player initialized as 1
    player = 1
    # game over initialized as False
    game_over = False
    # gridlines are drawn
    draw_gridlines()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart_game()
                    game_over = False
            # check if it is the computer's turn
            if player == 2 and not game_over:
                # computer plays
                row, col = computer_play()
                # mark the square
                mark_square(row, col, player)
                # check if there is a winner
                if check_win(player):
                    game_over = True
                # swap player
                player = 1
                # draw the pieces on the board
                draw_pieces()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                # x coordinate of the mouse
                mouseX = event.pos[0]
                # y coordinate of the mouse
                mouseY = event.pos[1]
                # determines clicked row
                clicked_row = int(mouseY // 200)
                # determines clicked column
                clicked_col = int(mouseX // 200)
                # if the square is available
                if square_available(clicked_row, clicked_col):
                    # if the player is 1
                    if player == 1:
                        # fill the square with a 1
                        mark_square(clicked_row, clicked_col, 1)
                        # check if there is a winner
                        if check_win(player):
                            game_over = True
                        # swap player
                        player = 2
                    draw_pieces()
        # update the screen
        pygame.display.update()

main()