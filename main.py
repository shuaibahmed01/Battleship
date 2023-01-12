'''
This program uses different objects and classes across multiple files to come together and
make and run the game of Battleship!
'''

from battleship import game


def main():
    '''
    Gets the data extracted from the configuration file and runs the program to play Battleship!
    '''
    config_file = input('Please enter the path to the configuration file for this game:')
    with open(config_file) as config_file:
        num_rows = int(config_file.readline())
        num_cols = int(config_file.readline())
        num_ships = int(config_file.readline())
        ships: dict[str, int] = dict()
        ships2: dict[str, int] = dict()
        for line in config_file:
            if line:
                ship_char, ship_length = line.split()
                ships[ship_char] = int(ship_length)
                ships2[ship_char] = int(ship_length)
    game.Game(num_cols, num_rows, ships, ships2).play()


main()



