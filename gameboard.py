from gamepiece import GamePiece


class GameBoard:
    """ Gameboard class is responsible for displaying an empty board as well as saving position
    of players tokens as the game progresses
    """
    # This represents a blank half tile. A full tile can be rendered from this string.
    # The encoding sets print color of the font to blue
    blank_space = ("\033[34m#########\033[0m\n"
                   "\033[34m##     ##\033[0m\n"
                   "\033[34m#       #\033[0m")

    def __init__(self):
        """ This initializes the game board grid with a 3D list. Each row is represented by the second
        dimension. the columns are represented by the third dimension. After initializing the grid, it is
        populated with blank tiles.
        """
        self.grid = [[[], [], [], [], [], [], []],
                     [[], [], [], [], [], [], []],
                     [[], [], [], [], [], [], []],
                     [[], [], [], [], [], [], []],
                     [[], [], [], [], [], [], []],
                     [[], [], [], [], [], [], []]]
        for row in self.grid:
            for i in range(7):
                row[i - 1] = self.blank_space

        # Score grid allows for quicker checking of win condition. Score grid is updated with player id at
        # Corresponding coordinate each time a token is placed.
        self.score_grid = [[[], [], [], [], [], [], []],
                           [[], [], [], [], [], [], []],
                           [[], [], [], [], [], [], []],
                           [[], [], [], [], [], [], []],
                           [[], [], [], [], [], [], []],
                           [[], [], [], [], [], [], []]]

    def _display_column_markers(self):
        print("===============================================================\n"
              "H        H        H        H        H        H        H       H\n"
              "H    1   H    2   H    3   H    4   H    5   H    6   H   7   H\n"
              "H        H        H        H        H        H        H       H\n"
              "==============================================================="
              )

    def display(self):
        """ This converts the grid into a format that can be printed to the console. """
        print_sequence = (0, 1, 2, 1, 0)  # This sequence allows the 3 line strings to be printed as a 5 line tile

        self._display_column_markers()

        #Reformats the grid to allow multiline strings to print horizontally across the console
        for row in self.grid:
            rendered_row = [[], [], []]
            blank_row = rendered_row
            for board_space in row:
                rendered_line = board_space.split('\n')
                for line in rendered_line:
                    rendered_row[rendered_line.index(line)].append(line)

            for index in print_sequence:
                print("".join(rendered_row[index]))

    def next_turn(self, active_player):
        player_input = int(input(f"{active_player}, please select a column: "))
        self.place_token(active_player, player_input)
        self.display()

    def  switch_players(self, active_player, next_player):
        placeholder = active_player
        active_player = next_player
        next_player = placeholder
        return active_player, next_player

    def place_token(self, active_player: GamePiece, column: int):
        """ Replace lowest available spot in a selected column with a player's token. """
        try:
            for i in range(6, 0, -1):
                if self.grid[i - 1][column - 1] == GameBoard.blank_space:
                    self.grid[i - 1][column - 1] = active_player.player_token
                    self.score_grid[i - 1][column - 1] = active_player.id
                    break
        except:
            print("That row is full! Try another one")

    def check_victory(self, active_player: GamePiece):
        """Checks for sequences of 4 after every turn"""
        victory = False

        def _check_horizontal(active_player = active_player):
            sequence = 0
            for row in self.score_grid:
                for space in row:
                    if space == active_player.id:
                        sequence += 1
                        if sequence == 4:
                            print("HORIZONTAL SEQUENCE")
                            return True
                    else:
                        sequence = 0
            return False

        def _check_vertical(active_player = active_player):
            sequence = 0
            for i in range(7):
                for j in range(6,0,-1):
                    if self.score_grid[j - 1][i - 1] == active_player.id:
                        sequence += 1
                        if sequence == 4:
                            print("VERTICAL SEQUENCE")
                            return True
                    else:
                        sequence = 0
            return False

        def _check_diagonal(active_player = active_player):
            def _increment_diagonal(x, y, x_increment, y_increment):
                return (x + x_increment, y + y_increment)

            def _traverse_bottom_right(active_player = active_player):
                sequence = 0
                for i in range(4):
                    y, x = 5, i
                    try:
                        for j in range(6):
                            if self.score_grid[y][x] == active_player.id:
                                sequence += 1
                                print("X: ", x, "Y: ", y, "       SEQUENCE: ", sequence)
                                if sequence == 4:
                                    print("TRAVERSE BOTTOM RIGHT SEQUENCE")
                                    return True
                            else:
                                sequence = 0
                            x, y = _increment_diagonal(x, y, 1, -1)

                    except Exception as e:
                        pass
                        #print(e)
                return False


            def _traverse_bottom_left(active_player=active_player):
                sequence = 0
                for i in range(6,3,-1):
                    y, x = 5, i
                    try:
                        for j in range(6):
                            if self.score_grid[y][x] == active_player.id:
                                sequence += 1
                                print("X: ", x, "Y: ", y, "    SEQUENCE: ", sequence)
                                if sequence == 4:
                                    print("TRAVERSE BOTTOM LEFT SEQUENCE")
                                    return True
                            else:
                                sequence = 0
                            x, y = _increment_diagonal(x, y, -1, -1)

                    except Exception as e:
                        pass
                        # print(e)
                return False



            def _traverse_left_side(active_player = active_player):
                sequence = 0
                for i in range(4,2,-1):
                    y, x = i, 0
                    try:
                        for j in range(6):
                            if self.score_grid[y][x] == active_player.id:
                                sequence += 1
                                print("X: ", x, "Y: ", y, "    SEQUENCE: ", sequence)
                                if sequence == 4:
                                    print("TRAVERSE LEFT SIDE SEQUENCE")
                                    return True
                            else:
                                sequence = 0
                            x, y = _increment_diagonal(x, y, 1, -1)

                    except Exception as e:
                        pass
                        # print(e)
                return False

            def _traverse_right_side(active_player = active_player):
                sequence = 0
                for i in range(4,2,-1):
                    y, x = i, 6
                    try:
                        for j in range(6):
                            if self.score_grid[y][x] == active_player.id:
                                sequence += 1
                                print("TRAVERSE RIGHT SIDE: X: ", x, "Y: ", y, "    SEQUENCE: ", sequence)
                                if sequence == 4:
                                    print("TRAVERSE RIGHT SIDE SEQUENCE")
                                    return True
                            else:
                                sequence = 0
                            x, y = _increment_diagonal(x, y, -1, -1)

                    except Exception as e:
                        pass
                        # print(e)
                return False


            diagonal_victory = _traverse_bottom_right()
            if diagonal_victory == False:
                diagonal_victory = _traverse_bottom_left()
            if diagonal_victory == False:
                diagonal_victory = _traverse_left_side()
            if diagonal_victory == False:
                diagonal_victory = _traverse_right_side()
            return diagonal_victory


        print("CHECKING HORIZONTAL")
        victory = _check_horizontal()
        if victory == False:
            print("CHECKING VERTICAL")
            victory = _check_vertical()
        if victory == False:
            print("CHECKING DIAGONAL")
            victory = _check_diagonal()
        return victory, active_player
