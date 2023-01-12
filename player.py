
from battleship import firing_board
from battleship import board


class Player:
    def __init__(self, cols: int, rows: int, player_name: str, ships: dict, ships2: dict):
        self.all_ships = ships
        self.all_ships2 = ships2
        self.board = board.Board(cols, rows).make_board()
        self.firing_board = firing_board.FiringBoard(cols, rows)
        self.player_name = player_name
        self.fleet = []
        self.cols = cols
        self.rows = rows
        self.location = []
        self.ship_chars = []

    def valid_start(self, row: int, col: int, orientation: str) -> bool:
        '''
        Goes through if statement to check if user input is valid or not
        :param row: the row user wants to put piece on
        :param col: the column user wants to put piece on
        :param orientation:the directioon user wants ship to go in
        :return: True if user puts in valid input, false if user does not put in valid input
        '''
        if (orientation.lower() not in 'vertical') and (orientation.lower() not in 'horizontal'):
            return False
        if int(row) > self.rows or int(col) > self.cols:
            return False
        if int(row) < 0 or int(col) < 0:
            return False
        if self.board[int(row)][int(col)] != '*':
            return False
        return True

    def valid_direction(self, orientation: str) -> bool:
        '''
        checks if user input for orientation is valid
        :param orientation: direction user wants ships to be in
        :return: whether the orientation is valid
        '''
        if (orientation.lower() not in 'vertically') and (orientation.lower() not in 'horizontally'):
            return False
        return True

    def put_fleet_on_board(self) -> list[list[str]]:
        '''
        Asks for user input and puts ships onto the board
        :return: gives back the updated placement board
        '''
        new_dict = sorted(self.all_ships.items())
        for ship_char, ship_len in new_dict:
            self.ship_chars.append(ship_char)
            board.Board(self.cols, self.rows).print_new_board(self.board, self.player_name)
            orientation = input(f'{self.player_name}, enter the orientation of your {ship_char}, which'
                                f' is {ship_len} long: ')
            user_input = input(f'Enter the starting location for your {ship_char}, which is {ship_len} long,'
                               f' in the form row col: ')
            row, col = user_input.split()
            self.fleet.append(ship_char)
            if orientation.lower() in 'vertically':
                for i in range(ship_len):
                    self.board[int(row)][int(col)] = ship_char
                    v = int(row)
                    self.location.append((row, col))
                    row = v + 1

            if orientation.lower() in 'horizontally':
                for i in range(ship_len):
                    self.board[int(row)][int(col)] = ship_char
                    v = int(col)
                    self.location.append((row, col))
                    col = v + 1

        board.Board(self.cols, self.rows).print_new_board(self.board, self.player_name)
        return(self.board)

    def get_ship_locations(self, player_board: list[list[str]]) -> list:
        '''
        Uses the placement board after ships have been placed to get locations for each ship
        :param player_board: the target players board
        :return: a list of each boats location on the board
        '''
        ship_locations = []
        for ship_char, ship_len in sorted(self.all_ships.items()):
            each_ship = []
            for row in range(len(player_board)):
                for col in range(self.cols):
                    if player_board[row][col] == ship_char:
                        each_ship.append((row, col))
            ship_locations.append(each_ship)
        return ship_locations

    def print_firing_and_placement_board(self) -> None:
        '''
        Prints out updated firing and placement boards
        '''
        self.firing_board.print_firing_board(self.player_name)
        board.Board(self.cols, self.rows).print_new_board(self.board, self.player_name)

    def p1_register_hit(self, target: list[list[str]], target_name: str, all_ships: dict, ship_locations: list,
                        point: str) -> None:
        '''
        registers a hit from player one to player two and checks if the ship was destroyed
        :param target: the targets board
        :param target_name: the targets name
        :param all_ships: the dictionary of ships from con fig file
        :param ship_locations: each ships location on board
        :param point: the ship that was hit
        :return: does not return anything
        '''
        destroyed_ship = False
        dict = all_ships
        new_dict = sorted(dict.items())
        iterations = -1
        iteration = 0
        char_to_del = ''
        for boat in ship_locations:
            count = 0
            iterations += 1
            for row, col in boat:
                if target[row][col] == 'X':
                    count += 1
            if count == len(boat):
                print(f'{self.player_name} destroyed {target_name}\'s {point}!')
                destroyed_ship = True
                char_to_del = point
                iteration = iterations
        if destroyed_ship:
            del dict[char_to_del]
            ship_locations.pop(iteration)


    def p2_register_hit(self, target: list[list[str]], target_name: str, all_ships: dict, ship_locations: list,
                        point: str) -> None:
        '''
        registers a hit from player one to player two and checks if the ship was destroyed
        :param target: the targets board
        :param target_name: the targets name
        :param all_ships: the dictionary of ships from con fig file
        :param ship_locations: each ships location on board
        :param point: the ship that was hit
        :return: does not return anything
        '''
        destroyed_ship = False
        dict = all_ships
        new_dict = sorted(dict.items())
        iterations = -1
        iteration = 0
        char_to_del = ''
        for boat in ship_locations:
            count = 0
            iterations += 1
            for row, col in boat:
                if target[row][col] == 'X':
                    count += 1
            if count == len(boat):
                print(f'{self.player_name} destroyed {target_name}\'s {point}!')
                destroyed_ship = True
                char_to_del = point
                iteration = iterations
        if destroyed_ship:
            del dict[char_to_del]
            ship_locations.pop(iteration)

    def p1_make_move(self, target: list[list[str]], target_name: str, ship_locations: list):
        '''
        Asks where player one would like to attack and makes the move for them
        :param target: the targets board
        :param target_name: the targets name
        :param ship_locations: the location of their ships
        :return: does not return anything
        '''
        self.print_firing_and_placement_board()
        user_input = input(f'{self.player_name}, enter the location you want to fire at in the form row col:')
        row, col = user_input.split()
        row = int(row)
        col = int(col)
        if target[row][col] in self.ship_chars:
            point = target[row][col]
            print(f'{self.player_name} hit {target_name}\'s {target[row][col]}!')
            target[row][col] = 'X'
            self.p1_register_hit(target, target_name, self.all_ships, ship_locations, point)
            self.firing_board.firing_board[row][col] = 'X'
        else:
            print(f'{self.player_name} missed.')
            target[row][col] = 'O'
            self.firing_board.firing_board[row][col] = 'O'

    def p2_make_move(self, target: list[list[str]], target_name: str, ship_locations: list) -> None:
        '''
        Asks where player two would like to attack and makes the move for them
        :param target: the targets board
        :param target_name: the targets name
        :param ship_locations: the location of their ships
        :return: does not return anything
        '''
        self.print_firing_and_placement_board()
        user_input = input(f'{self.player_name}, enter the location you want to fire at in the form row col:')
        row, col = user_input.split()
        row = int(row)
        col = int(col)
        if target[row][col] in self.ship_chars:
            point = target[row][col]
            print(f'{self.player_name} hit {target_name}\'s {target[row][col]}!')
            target[row][col] = 'X'
            self.p2_register_hit(target, target_name, self.all_ships2, ship_locations, point)
            self.firing_board.firing_board[row][col] = 'X'
        else:
            print(f'{self.player_name} missed.')
            target[row][col] = 'O'
            self.firing_board.firing_board[row][col] = 'O'




