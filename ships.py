
class Ships():
    def __init__(self, ship_type: str, ship_len: str):
        self.ship_type = ship_type
        self.ship_len = ship_len
        self.location = []

    def get_location(self, row, col):
        '''
        gets the location of the users ships
        :param row: the row user shoots at
        :param col: the col user shoots at
        :return: does not return anything
        '''
        self.location.append((row, col))

    def return_location(self):
        '''
        :return: simply returns an updated location list
        '''
        return self.location

    def check_for_ship(self) -> bool:
        '''
        checks is the location list is empty or not, or if any ships remain on the board
        :return: returns True is there are no ships, and False is there are
        '''
        if self.location == []:
            return True
        else:
            return False