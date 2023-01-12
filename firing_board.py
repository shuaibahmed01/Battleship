
class FiringBoard():
    def __init__(self, cols: int, rows: int):
        self.cols = cols
        self.firing_board = [['*' for i in range(cols)] for i in range(rows)]

    def get_move(self, move):
        '''gets user move from them and adds it to the firing board'''
        row, col = move
        return self.firing_board[row][col]

    def print_firing_board(self, player_name: str):
        '''
        prints out the firing board of the specified user
        :param player_name: the players name
        :return: does not return anything
        '''
        print(f'{player_name}\'s Firing Board')
        print(end='  ')
        for header in range(self.cols):
            print(header, end=' ')
        print()
        for row_index, row in list(enumerate(self.firing_board)):
            print(row_index, ' '.join(row))