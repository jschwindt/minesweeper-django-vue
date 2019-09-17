class Board:
    def __init__(self, width, heigth, mines):
        self.width = width
        self.heigth = heigth
        self.mines = mines
        print(width)
        self.cells = [[0 for j in range(width)] for i in range(heigth)]
