from gameboard import GameBoard
from gamepiece import GamePiece
from title import Title

four_in_a_row = False
connect4 = GameBoard()
title = Title()
print(title)

print("PLAYER 1: Choose your color.")
player1_color = input("Please enter red, green, yellow, white, or black: ")

print("PLAYER 2: Choose your color.")
player2_color = input("Please enter red, green, yellow, white, or black: ")

player1 = GamePiece(player1_color)
player1.set_token_color()

player2 = GamePiece(player2_color)
player2.set_token_color()

active_player = player1
next_player = player2

connect4.display()

while True:
    connect4.next_turn(active_player)
    four_in_a_row, winner = connect4.check_victory(active_player)
    if four_in_a_row == True:
        break
    active_player, next_player = connect4.switch_players(active_player, next_player)




print(f"VICTORY!! {winner} has won the game!")