
class Board:
    def __init__(self, cols: int, rows: int):
        self.rows = rows
        self.cols = cols

    def make_board(self) -> list[list[str]]:
        '''
        makes the inital placement board
        :return: returns the made baord
        '''
        blank_char = '*'
        board = []
        for row_num in range(self.rows):
            row = []
            for col_num in range(self.cols):
                row.append(blank_char)
            board.append(row)
        return board

    def print_board(self):
        '''
        prints the very initial board made, without any ships on it
        '''
        print(end='  ')
        for header in range(self.cols):
            print(header, end=' ')
        print()
        for row_index, row in list(enumerate(self.make_board())):
            print(row_index, ' '.join(row))

    def print_new_board(self, board: list[list[str]], player_name):
        '''
        prints out an updated placement board through the game depending on the board inputted
        :param board: the intended users updated board
        :param player_name: the intended users name
        :return: does not return anything
        '''
        print(f'{player_name}\'s Placement Board')
        print(end='  ')
        for header in range(self.cols):
            print(header, end=' ')
        print()
        for row_index, row in list(enumerate(board)):
            print(row_index, ' '.join(row))
