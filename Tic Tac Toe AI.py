# Mini project by Avi-Niam Popat: 20042651
import random

# initialising variables
board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}  # dictionary for the board
player1 = 'O'
player2 = 'X'  # can be an actual player or the AI

def draw_board(board):  # function to create the board in the terminal
    print(board[1] + "|" + board[2] + "|" + board[3])  # row one of the board
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])   # row 2 of the board
    print("-+-+-")
    print(board[7] + "|" + board[8] + "|" + board[9])  # row 3 of the board
    print("\n")  # new line


def player1_move():  # function for player 1's move
    pos = int(input("player 1 choose a space for O(between 1 and 9): "))
    check_move(player1, pos)  # check if the move is valid
    return

def player2_move():  # function for player 2's move
    pos = int(input("player 2 choose a space for X (between 1 and 9): "))
    check_move(player2, pos)
    return

def basic_bot():  # function for the bots move
    pos = random.randint(1, 9)
    print("player 2 chose", pos)
    check_move(player2, pos)
    return


def free_space(pos):  # function to check for free spaces on the board
    if board[pos] == ' ':  # checks if the space is free
        return True  # returns true if it is
    else:
        return False  # false if it isn't

def check_win():  # This function checks if there is 3 of the same mark in a row
    if board[1] == board[2] and board[1] == board[3] and board[1] != ' ':
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] != ' ':
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] != ' ':
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] != ' ':
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] != ' ':
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] != ' ':
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] != ' ':
        return True
    elif board[7] == board[5] and board[7] == board[3] and board[7] != ' ':
        return True
    else:
        return False

def check_draw():  # function to check if the game is a draw
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

def check_move(xo, pos):  # function that checks the result of a move
    if free_space(pos):
        board[pos] = xo
        draw_board(board)
        if check_draw():
            print("it's a draw!")
            exit()
        if check_win():  # calls check_win function to check who one by checking what mark it is
            if xo == 'O':  # if the mark is nought player 1 wins
                print("Player 1 wins!")
                exit()
            else:  # if the mark is a cross player 2 wins
                print("Player 2 Wins!")
                exit()
        return
    else:
        print("invalid Position")
        pos = random.randint(1, 9)
        print("player chose", pos, "instead")
        check_move(xo, pos)
        return


def can_win(mark):  # this function checks possible moves to win
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] == mark:
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] == mark:
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] == mark:
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] == mark:
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] == mark:
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] == mark:
        return True
    elif board[7] == board[5] and board[7] == board[3] and board[7] == mark:
        return True
    else:
        return False

def minimaxAI(board, maximizing):  # Minimax function
    if can_win(player2):  # checks if the AI can win
        return 1
    elif can_win(player1):  # checks if the Player can win
        return -1
    elif check_draw():  # Checks if no one can win
        return 0

    if maximizing:
        best_score = -10
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player2
                score = minimaxAI(board, False)  # not maximising
                board[key] = ' '
                if score > best_score:
                    best_score = score
        return best_score

    else:  # not maximising or minimising
        best_score = 10
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player1
                score = minimaxAI(board, True)  # the algorithm is maximising
                board[key] = ' '
                if score < best_score:
                    best_score = score
        return best_score

def unbeatable_bot():  # Minimax AI
    # initialising variables
    best_score = -10
    best_move = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = player2
            score = minimaxAI(board, False)
            board[key] = ' '
            if score > best_score:
                best_score = score
                best_move = key
                print("the bot chose space", best_move)
    check_move(player2, best_move)
    return


# Main program
print("Mini project by Avi-Niam Popat: 20042651")
print("\n")

players = int(input("Enter the number of players, 1 or 2: "))

if players == 1:
    bot_mode = int(input("Enter 1 for basic bot or 2 for the unbeatable bot: "))
    if bot_mode == 1:
        draw_board(board)
        print("Basic bot game: ")
        while not check_win():
            basic_bot()
            player1_move()

    elif bot_mode == 2:
        draw_board(board)
        print("Unbeatable bot game: ")
        while not check_win():
            unbeatable_bot()
            player1_move()

elif players == 2:
    draw_board(board)
    while not check_win():
        player1_move()
        player2_move()
