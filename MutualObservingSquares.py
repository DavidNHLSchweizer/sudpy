import SudokuConstants as SCS
from Square import Square
from Squares import Squares

class SubGrid(Squares):
    def __init__(self):
        super().__init__()
    def updateDependencies(self):
        for square in self.squares:
            pass