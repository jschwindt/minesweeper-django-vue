import random

class Board:
    CELL_EMPTY = -1
    CELL_MINE = 1
    def __init__(self, width, heigth, mines):
        self.width = width
        self.heigth = heigth
        self.mines = mines
        self.user_board = [[Board.CELL_EMPTY for j in range(width)] for i in range(heigth)]
        self.board_mines = self.set_mines()

    def set_mines(self):
        random.seed()
        added_mines = 0
        board_mines = [[Board.CELL_EMPTY for j in range(self.width)] for i in range(self.heigth)]
        while added_mines < self.mines:
            row = random.randint(0, self.heigth-1)
            col = random.randint(0, self.width-1)
            if board_mines[row][col] == Board.CELL_EMPTY:
                board_mines[row][col] = Board.CELL_MINE
                added_mines += 1
        return board_mines
