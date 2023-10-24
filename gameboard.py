class GameBoard:
    blank_space = ("\033[34m#########\033[0m\n"
                   "\033[34m###   ###\033[0m\n"
                   "\033[34m##     ##\033[0m")


    def __init__(self):
        self.grid = [[[],[],[],[],[],[],[]],
                     [[],[],[],[],[],[],[]],
                     [[],[],[],[],[],[],[]],
                     [[],[],[],[],[],[],[]],
                     [[],[],[],[],[],[],[]],
                     [[],[],[],[],[],[],[]]]
        for row in self.grid:
            for i in range(7):
                row[i-1] = self.blank_space

    def __repr__(self):
        print_sequence = [0,1,2,1,0]

        for row in self.grid:
            rendered_row = [[], [], []]
            blank_row = rendered_row
            for board_space in row:
                rendered_line = board_space.split('\n')
                for line in rendered_line:
                    rendered_row[rendered_line.index(line)].append(line)

            for index in print_sequence:
                print("".join(rendered_row[index]))
            rendered_row = blank_row


