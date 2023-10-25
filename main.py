from gameboard import GameBoard
from gamepiece import GamePiece

connect4 = GameBoard()

player_1_token = GamePiece('yellow')
print(player_1_token)

player_2_token = GamePiece('green')
player_2_token.set_token_color()
print(player_2_token)


connect4.place_token(player_1_token, 3)
connect4.place_token(player_1_token, 2)
connect4.place_token(player_2_token, 1)
connect4.place_token(player_2_token, 3)
connect4.place_token(player_2_token, 2)
connect4.place_token(player_2_token, 4)

winner = connect4.check_victory(player_2_token)
print(winner)

print(connect4.score_grid)

#connect4.display()