class GamePiece:
    id=1
    def __init__(self, color):
        self.id = GamePiece.id
        self.color = color

        # This string represents half a token. After color selection, $ will be replaced with appropriately
        # colored characters.
        self.player_token = ("\033[34m#########\033[0m\n"
                             "\033[34m##$$$$$##\033[0m\n"
                             "\033[34m#$$$$$$$#\033[0m")

        GamePiece.id += 1

    def __repr__(self):
        return "PLAYER {} - {}".format(self.id, self.color.upper())

    def set_token_color(self):
        """ Make a unique half token string for each player based on color by adding appropriate color code."""
        color_dict = {'red': '31m',
                      'green': '32m',
                      'yellow': '33m',
                      'white': '37m'}
        self.player_token = self.player_token.replace('$',
                                                      '\033[' + color_dict[self.color] + "#" + '\033[34m')