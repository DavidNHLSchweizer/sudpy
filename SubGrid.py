import SudokuConstants as SCS
from Squares import Squares

class _SubGrid(Squares):
    def __init__(self, squaresArray):
        super().__init__()
        self._addSquares(squaresArray)
        if not len(squaresArray) == SCS.GRIDSIZE:
            ValueError(SCS.INVALIDSQUARESEXCEPTION + ' {}'.format(len(squaresArray)))
    def _addSquares(self, squaresArray):
        for square in squaresArray: 
            self.addSquare(square)
        self._updateDependencies()
    def _crossObserve(self, square1, square2):
        square1.ObserveValue(square2._value)
        square2.ObserveValue(square1._value)
    def _updateDependencies(self):
        for i in range(self.nSquares):
            for j in range(i+1, self.nSquares):
                self._crossObserve(self.squares[i], self.squares[j])

class Row(_SubGrid):
    def __init__(self, squaresArray):
        super().__init__(squaresArray)        
        self.nRows = 1

class Column(_SubGrid):
    def __init__(self, squaresArray):
        super().__init__(squaresArray)
        self.nCols = 1

class Block(_SubGrid):
    def __init__(self, squaresArray):
        super().__init__(squaresArray)
        self.nCols = SCS.BLOCKSIZE
