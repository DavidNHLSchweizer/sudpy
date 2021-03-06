import SudokuConstants as SCS
from Squares import Squares
from Grid import Grid

class SquaresValidator:
    def IsValidValues(self, squares: Squares):
        values = []
        for square in squares.squares:
            if square.value != SCS.INITIAL:
                if square.value in values:
                    return False
                values.append(square.value)
        return True
    def IsCompleteValues(self, squares: Squares):
        return squares.nrSquaresWithValues() == squares.nSquares

class GridValidator:
    def __init__(self):
        self._squaresValidator = SquaresValidator()
    def IsValidValues(self, grid: Grid):
        for r in range(grid.nRows):
            if not self._squaresValidator.IsValidValues(grid.Row(r)):
                return False
        for c in range(grid.nCols):
            if not self._squaresValidator.IsValidValues(grid.Column(c)):
                return False
        for brow in range(grid.nBlockRows):
            for bcol in range(grid.nBlockCols):
                if not self._squaresValidator.IsValidValues(grid.Block(brow, bcol)):
                    return False
        return True
    def IsCompleteValues(self, grid: Grid):
        for r in range(grid.nRows):
            if not self._squaresValidator.IsCompleteValues(grid.Row(r)):
                return False
        return True
    def asString(self, grid: Grid):
        return 'Filled: {}/{}  Complete: {}   Valid: {}'.format(grid.nrSquaresWithValues(), grid.nRows * grid.nCols,
             self.IsCompleteValues(grid), self.IsValidValues(grid))
