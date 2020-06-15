import SudokuConstants as SCS
from Squares import Squares
from Grid import Grid

class SquaresValidator:
    def nrSquaresWithValues(self, squares: Squares):
        result = 0            
        for square in squares.squares:
            if square.value != SCS.INITIAL:
                result += 1
        return result
    def IsValidValues(self, squares: Squares):
        values = []
        for square in squares.squares:
            if square.value != SCS.INITIAL:
                if square.value in values:
                    return False
                values.append(square.value)
        return True
    def IsCompleteValues(self, squares: Squares):
        return self.nrSquaresWithValues(squares) == len(squares.squares)

class GridValidator:
    def __init__(self):
        self._squaresValidator = SquaresValidator()
    def IsValidValues(self, grid: Grid):
        for r in range(SCS.GRIDSIZE):
            if not self._squaresValidator.IsValidValues(grid.Row(r)):
                return False
        for c in range(SCS.GRIDSIZE):
            if not self._squaresValidator.IsValidValues(grid.Column(c)):
                return False
        for brow in range(SCS.BLOCKSIZE):
            for bcol in range(SCS.BLOCKSIZE):
                if not self._squaresValidator.IsValidValues(grid.Block(brow, bcol)):
                    return False
        return True
    def IsCompleteValues(self, grid: Grid):
        for r in range(SCS.GRIDSIZE):
            if not self._squaresValidator.IsCompleteValues(grid.Row(r)):
                return False
        return True
    def nrSquaresWithValues(self, grid: Grid):
        result = 0
        for r in range(SCS.GRIDSIZE):
            result += self._squaresValidator.nrSquaresWithValues(grid.Row(r))
        return result
    def asString(self, grid: Grid):
        return 'Filled: {}/{}  Complete: {}   Valid: {}'.format(self.nrSquaresWithValues(grid), grid.nRows * grid.nCols,
             self.IsCompleteValues(grid), self.IsValidValues(grid))
