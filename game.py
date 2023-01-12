from battleship import player



class Game():
    def __init__(self, cols: int, rows: int, ships: dict, ships2: dict) -> None:
        self.cols = cols
        self.rows = rows
        self.ships = ships
        self.ships2 = ships2

    def play(self):
        '''
        Runs the overall game using the classes and functions made previously
        :return: does not return anything
        '''
        player_1_name = input('Player 1, please enter your name: ')
        player_2_name = input('Player 2, please enter your name: ')
        p1 = player.Player(self.cols, self.rows, player_1_name, self.ships, self.ships)
        p2 = player.Player(self.cols, self.rows, player_2_name, self.ships, self.ships2)
        p1_board = p1.put_fleet_on_board()
        p1_ship_locations = p1.get_ship_locations(p1_board)
        p2_board = p2.put_fleet_on_board()
        p2_ship_locations = p2.get_ship_locations(p2_board)

        switch = True
        while switch is True:
            p1.p1_make_move(p2_board, player_2_name, p2_ship_locations)
            if self.fleet_sunk(p2_board):
                p1.print_firing_and_placement_board()
                self.victory_message(player_1_name)
                switch = False

            else:
                p2.p2_make_move(p1_board, player_1_name, p1_ship_locations)
                if self.fleet_sunk(p1_board):
                    p2.print_firing_and_placement_board()
                    self.victory_message(player_2_name)
                    switch = False

    def fleet_sunk(self, player_board: list[list[str]]) -> bool:
        '''
        Iterates through the players boards to see if any ship pieces are left, if not it returns True, if there are
        it returns False
        :param player_board: The oppossing players placement
        :return: whether the players board has any ships on it or not
        '''
        ship_chars = ['*', 'X', 'O']
        for row in range(len(player_board)):
            for col in range(self.cols):
                if player_board[row][col] not in ship_chars:
                    return False
        else:
            return True

    def victory_message(self, winner: str) -> None:
        '''
        Prints out who won
        :param winner: takes in who the winner is
        :return: does not return anything
        '''
        print(f'{winner} won!')




