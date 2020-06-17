import SudokuConstants as SCS
from Square import Square
from Squares import Squares

class DependingSquares(Squares):
    def __init__(self):
        super().__init__()
        self._init_squares()
    def _init_squares(self):
        for _ in range(SCS.GRIDSIZE):            
            for _ in range(SCS.GRIDSIZE):
                self.addSquare(Square())
        self.nCols = SCS.GRIDSIZE
