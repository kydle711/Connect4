from gameboard import GameBoard
from gamepiece import GamePiece
from title import Title

winner = False
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
connect4.display()
while winner == False:
    player1_input = int(input("PLAYER 1- Choose a column :"))
    connect4.place_token(player1, player1_input)
    print(winner)
    connect4.display()
    print(winner)
    connect4.check_victory(player1)
    print(winner)
    player2_input = int(input("PLAYER 2- Choose a column :"))
    connect4.place_token(player2, player2_input)
    connect4.display()
    connect4.check_victory(player2)

