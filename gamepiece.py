class GamePiece:
    id=1
    def __init__(self, color):
        self.id = GamePiece.id
        self.color = color
        self.player_token = ("\033[34m#########\033[0m\n"
                             "\033[34m###$$$###\033[0m\n"
                             "\033[34m##$$$$$##\033[0m")

        GamePiece.id += 1

    def __repr__(self):
        return "WELCOME PLAYER {}! YOUR CHOSEN COLOR IS {}".format(self.id, self.color)

    def set_token_color(self):
        color_dict = {'black': '30m',
                      'red': '31m',
                      'green': '32m',
                      'yellow': '33m',
                      'white': '37m'}
        self.player_token = self.player_token.replace('$',
                                                      '\033[' + color_dict[self.color] + "#" + '\033[34m')