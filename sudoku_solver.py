class Sudoku_Board:
    def __init__(self):
        self.board = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]
        self.rows = len(self.board)
        self.columns = len(self.board[0])

    def print_board(self):
        board_GUI = ''
        z = 0
        for row in self.board:
            if z % 3 == 0 and not z == 0:
                board_GUI += '------------------------\n'
            for i in range(self.rows):

                if i % 3 == 0 and not i == 0:
                    board_GUI += ' | '
                board_GUI += str(row[i]) + ' '
                if i == self.columns - 1:
                    board_GUI = f'{board_GUI}\n'
                    z += 1

        print(board_GUI)

    def empty_spots_finder(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.board[i][j] == 0:
                    return i, j

    def sudoku_solver(self):
        empty_spot = self.empty_spots_finder()
        if not empty_spot:
            return True
        ro, co = empty_spot
        for i in range(1, 10):
            if self.number_is_valid(i, ro, co):
                self.board[ro][co] = i

                if self.sudoku_solver():
                    return True
                self.board[ro][co] = 0
        return False

    def number_is_valid(self, number, ro, co):
        for i in range(self.rows):
            if self.board[ro][i] == number and co != i:
                return False
            # check column
            if self.board[i][co] == number and ro != i:
                return False

            # check boxes
        box_horizontal = (ro // 3) * 3
        box_vertical = (co // 3) * 3
        for i in range(box_horizontal, box_horizontal + 3):
            for j in range(box_vertical, box_vertical + 3):
                if self.board[i][j] == number and (i, j) != (ro, co):
                    return False

        return True
