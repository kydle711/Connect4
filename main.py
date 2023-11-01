from gameboard import GameBoard
from gamepiece import GamePiece
from title import Title

# winner flag
four_in_a_row = False

# Initialize gameboard and print opening title
connect4 = GameBoard()
title = Title()
print(title)

# Reference for validating player's color input
available_colors = ['red', 'green', 'yellow', 'white', 'black']
player1_color = ""
player2_color = ""

print("PLAYER 1: Choose your color.")
while player1_color not in available_colors:
    player1_color = input("Please enter red, green, yellow, white, or black: ")

print("PLAYER 2: Choose your color.")
while player2_color not in available_colors or player2_color == player1_color:
    player2_color = input("Please enter red, green, yellow, white, or black: ")

# Initialize player objects with chosen player color and player ID
player1 = GamePiece(player1_color)
player1.set_token_color()

player2 = GamePiece(player2_color)
player2.set_token_color()

# Label players for the sake of turn-based play
active_player = player1
next_player = player2

# Render empty gameboard
connect4.display()

# Main loop
while True:
    connect4.next_turn(active_player)
    four_in_a_row, winner = connect4.check_victory(active_player)
    if four_in_a_row == True:
        break
    active_player, next_player = connect4.switch_players(active_player, next_player)



# When loop breaks, print the winner
print(f"VICTORY!! {winner} has won the game!")