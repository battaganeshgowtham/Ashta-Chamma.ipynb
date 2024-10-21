import random

board = [' '] * 25
player_positions = [0, 0]
players = ['You', 'Computer']

safe_boxes = [4, 12, 20]
other_markings = {5: '*', 8: 'X', 16: 'O', 24: '#'}

def roll_die():
    return random.randint(1, 6)

def move_player(player, steps):
    player_positions[player] += steps
    if player_positions[player] >= len(board):
        player_positions[player] %= len(board)

def display_board():
    for i, player in enumerate(player_positions):
        if board[player] == ' ':
            board[player] = str(i + 1)

    print("+----" * 5 + "+")
    for i in range(0, len(board), 5):
        row = "|"
        for j in range(5):
            cell = board[i + j]
            if cell == ' ':
                if (i + j) in safe_boxes:
                    row += " S  |"
                elif (i + j) in other_markings:
                    row += f" {other_markings[i + j]}  |"
                else:
                    row += "    |"
            else:
                row += f" {cell}  |"
        print(row)
        print("+----" * 5 + "+")

    for i, player in enumerate(player_positions):
        board[player] = ' '

current_player = 0

while True:
    input(f"{players[current_player]}'s turn. Press Enter to roll the die...")

    if current_player == 0:
        steps = roll_die()
        print(f"{players[current_player]} rolled a {steps}")
        move_player(current_player, steps)
        display_board()

    else:
        steps = roll_die()
        print(f"{players[current_player]} rolled a {steps}")
        move_player(current_player, steps)
        display_board()


    if player_positions[current_player] == len(board) - 1:
        print(f"{players[current_player]} has won!")
        break

    user_input = input("Press 'q' to quit the game or any other key to continue: ")
    if user_input.lower() == 'q':
        break

    current_player = 1 - current_player
