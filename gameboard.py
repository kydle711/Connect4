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

        """ Score grid allows for quicker checking of win condition. Score grid is updated with player id at
            Corresponding coordinate each time a token is placed."""
        self.score_grid = [[[], [], [], [], [], [], []],
                           [[], [], [], [], [], [], []],
                           [[], [], [], [], [], [], []],
                           [[], [], [], [], [], [], []],
                           [[], [], [], [], [], [], []],
                           [[], [], [], [], [], [], []]]

        """ Available rows list that populates with a number for each column six times. Every turn, the player's
            input num will be removed from this list. If there are six tokens played in a given column, there will
            be no numbers in available list to validate any more selections of that column. 
         """

        self.available_rows = [str(num) for i in range(6) for num in range(1, 8)]

    def _display_column_markers(self):
        print("===============================================================\n"
              "H        H        H        H        H        H        H       H\n"
              "H    1   H    2   H    3   H    4   H    5   H    6   H   7   H\n"
              "H        H        H        H        H        H        H       H\n"
              "==============================================================="
              )

    def display(self):
        """ This converts the grid into a format that can be printed to the console.
            Print sequence allows the 3 line string at Gameboard.blank_space to be
            printed as a 5 line tile. """
        print_sequence = (0, 1, 2, 1, 0)
        print("\n\n\n\n\n\n\n\n\n")      # white space between each board

        self._display_column_markers()

        # Reformat the grid to allow multi-line strings to print horizontally across the console
        for row in self.grid:
            rendered_row = [[], [], []]
            # blank_row = rendered_row
            for board_space in row:
                rendered_line = board_space.split('\n')
                for line in rendered_line:
                    rendered_row[rendered_line.index(line)].append(line)

            for index in print_sequence:
                print("".join(rendered_row[index]))

    def next_turn(self, active_player):
        """ Takes player input and places token """

        # Initialize player input to an invalid value
        player_input = ""

        while player_input not in self.available_rows:
            player_input = (input(f"\n{active_player}, please select a column: "))
            if player_input not in self.available_rows:
                print("\nINVALID INPUT\n")

        self.place_token(active_player, int(player_input))
        self.available_rows.remove(player_input)
        self.display()

    def switch_players(self, active_player, next_player):
        """ Switches each player between active player and next player every turn"""
        placeholder = active_player
        active_player = next_player
        next_player = placeholder
        return active_player, next_player

    def place_token(self, active_player: GamePiece, column: int):
        """ Replace the lowest available spot in a selected column with a player's token. """
        try:
            for i in range(6, 0, -1):
                if self.grid[i - 1][column - 1] == GameBoard.blank_space:
                    self.grid[i - 1][column - 1] = active_player.player_token
                    self.score_grid[i - 1][column - 1] = active_player.id
                    break
        except:
            print("That row is full! Try another one")

    def check_victory(self, active_player: GamePiece):
        """Checks for sequences of 4 after every turn. This function accomplishes this by using several nested
        functions to iterate across the board several different ways.
        """

        # Flag to represent if a victory condition has been met
        victory = False

        def _check_horizontal(active_player=active_player):
            """ This function checks for horizontal sequences."""
            sequence = 0
            for row in self.score_grid:
                for space in row:
                    if space == active_player.id:
                        sequence += 1
                        if sequence == 4:
                            return True
                    else:
                        sequence = 0
            return False

        def _check_vertical(active_player=active_player):
            """ This function checks for vertical sequences."""
            sequence = 0
            for i in range(7):
                for j in range(6, 0, -1):
                    if self.score_grid[j - 1][i - 1] == active_player.id:
                        sequence += 1
                        if sequence == 4:
                            return True
                    else:
                        sequence = 0
            return False

        def _check_diagonal(active_player=active_player):
            """ This function checks for diagonal sequences through more nested functions that target
            specific areas where a diagonal sequence can occur. These functions were nested further to simplify the
            check_victory function.
            """

            def _increment_diagonal(x, y, x_increment, y_increment):
                """ This function increments in different directions across the grid for
                different functions.
                """
                return (x + x_increment, y + y_increment)

            def _traverse_bottom_right(active_player=active_player):
                """ Traverses across the bottom row from left to right. This function only checks the first four
                spaces, as it is impossible to get a sequence of 4 beyond that. It then increments diagonally up
                and to the right from each of the four starting points.
                """
                sequence = 0
                for i in range(4):
                    y, x = 5, i
                    try:
                        for j in range(6):
                            if self.score_grid[y][x] == active_player.id:
                                sequence += 1
                                if sequence == 4:
                                    return True
                            else:
                                sequence = 0
                            x, y = _increment_diagonal(x, y, 1, -1)
                    except IndexError:
                        pass
                return False

            def _traverse_bottom_left(active_player=active_player):
                """ This function is the same as _traverse_bottom_left, except that it starts from the bottom right
                corner and increments up and to the left to check for sequences.
                """
                sequence = 0
                for i in range(6, 3, -1):
                    y, x = 5, i
                    try:
                        for j in range(6):
                            if self.score_grid[y][x] == active_player.id:
                                sequence += 1
                                if sequence == 4:
                                    return True
                            else:
                                sequence = 0
                            x, y = _increment_diagonal(x, y, -1, -1)

                    except IndexError:
                        pass
                return False

            def _traverse_left_side(active_player=active_player):
                """ This function traverses up the left side of the board and checks for sequences. It starts at
                the fourth indexed row and increments up and to the right. It is only necessary to check two rows,
                because many of the possible win positions are covered by the previous functions. This function
                does not check above the third indexed row, because a diagonal sequence above that point is not possible.
                """
                sequence = 0
                for i in range(4, 2, -1):
                    y, x = i, 0
                    try:
                        for j in range(6):
                            if self.score_grid[y][x] == active_player.id:
                                sequence += 1
                                if sequence == 4:
                                    return True
                            else:
                                sequence = 0
                            x, y = _increment_diagonal(x, y, 1, -1)

                    except IndexError:
                        pass
                return False

            def _traverse_right_side(active_player=active_player):
                """ This function is the same as _traverse_left_side, except that it moves up the right side and
                increments up and to the left.
                """
                sequence = 0
                for i in range(4, 2, -1):
                    y, x = i, 6
                    try:
                        for j in range(6):
                            if self.score_grid[y][x] == active_player.id:
                                sequence += 1
                                if sequence == 4:
                                    return True
                            else:
                                sequence = 0
                            x, y = _increment_diagonal(x, y, -1, -1)

                    except IndexError:
                        pass
                return False

            # Within the check diagonal function, set victory flag equal to the return value of each nested func
            diagonal_victory = _traverse_bottom_right()
            if diagonal_victory == False:
                diagonal_victory = _traverse_bottom_left()
            if diagonal_victory == False:
                diagonal_victory = _traverse_left_side()
            if diagonal_victory == False:
                diagonal_victory = _traverse_right_side()
            return diagonal_victory

        # Within the check victory function, set victory flag equal each nested func. return victory status and active
        # player at time of victory
        victory = _check_horizontal()
        if victory == False:
            victory = _check_vertical()
        if victory == False:
            victory = _check_diagonal()
        return victory, active_player
