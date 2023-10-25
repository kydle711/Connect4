from gamepiece import GamePiece


class GameBoard:
    """ Gameboard class is responsible for displaying an empty board as well as saving position
    of players tokens as the game progresses
    """
    # This represents a blank half tile. A full tile can be rendered from this string.
    # The encoding sets print color of the font to blue
    blank_space = ("\033[34m#########\033[0m\n"
                   "\033[34m###   ###\033[0m\n"
                   "\033[34m##     ##\033[0m")

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

    def place_token(self, player_token: GamePiece, column: int):
        """ Replace lowest available spot in a selected column with a player's token. """
        for i in range(6, 0, -1):
            if self.grid[i - 1][column - 1] == GameBoard.blank_space:
                self.grid[i - 1][column - 1] = player_token.player_token
                self.score_grid[i - 1][column - 1] = player_token.id
                break
            else:
                print("FAILED PLACEMENT")

    def check_victory(self, player_token):
        """Checks for sequences of 4 after every turn"""
        victory = False

        def _check_horizontal():
            sequence = 0
            for row in self.score_grid:
                for space in row:
                    if space == player_token.id:
                        sequence += 1
                        if sequence == 4:
                            victory = True
                            return victory
                        return
                    else:
                        sequence = 0

        _check_horizontal()
        if victory == True:
            return victory