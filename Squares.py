import SudokuConstants as SCS
from Square import Square

class Squares:
    def __init__(self):
        self.squares = []
        self._nCols = 0
        self._nRows = 1
    def addSquare(self, square: Square):
        self.squares.append(square)
        self._nCols += 1
    def _GetIndex(self, square):
        if not square in self.squares:
            return SCS.INDEXNOTFOUND        
        return self.squares.index(square)
    def _Contains(self, square):
        return square in self.squares
    def clear(self):
        for sq in self.squares:
            sq.clear()
    @property
    def nCols(self)->int:
        return self._nCols
    @nCols.setter
    def nCols(self, value):
        if value <= 0 or value > len(self.squares) or len(self.squares) % value != 0:
            raise ValueError(SCS.INVALIDCOLSEXCEPTION + ' {}'.format(value))
        self._nCols = value
        self._nRows = len(self.squares) // value
    @property
    def nRows(self)->int:
        return self._nRows
    @nRows.setter
    def nRows(self, value):
        if value <= 0 or value > len(self.squares) or len(self.squares) % value != 0:
            raise ValueError(SCS.INVALIDROWSEXCEPTION + ' {}'.format(value))
        self._nRows = value
        self._nCols = len(self.squares) // value
    def _RowColToIndex(self, row, col):
        return row * self.nCols + col
    def _IndexToRow(self, index):
        return index // self.nCols
    def _IndexToCol(self, index):
        return index % self.nCols
    def _CheckLegalBase(self, row, col, maxRows, maxCols):
        if row < 0 or row >= maxRows:
            ValueError(SCS.INVALIDROWSEXCEPTION + ' {}'.format(row))
        if col < 0 or col >= maxCols:
            ValueError(SCS.INVALIDCOLSEXCEPTION + ' {}'.format(col))
    def _CheckLegal(self, row, col):
        self._CheckLegalBase(row, col, self.nRows, self.nCols)
    def square(self, row, col):
        self._CheckLegal(row, col)
        return self.squares[self._RowColToIndex(row, col)]
    def sqRow(self, square):
        return self._IndexToRow(self._GetIndex(square))
    def sqCol(self, square):
        return self._IndexToCol(self._GetIndex(square))
    @property
    def nSquares(self)->int:
        return len(self.squares)
    def nrSquaresWithValues(self):
        result = 0            
        for square in self.squares:
            if square.value != SCS.INITIAL:
                result += 1
        return result

    def asString(self):
        result = ''
        for r in range(self.nRows):
            for c in range(self.nCols):
                square = self.square(r, c)
                result = result + ('0' if square.value == SCS.INITIAL else str(square.value))
                if c % 3 == 2:
                    result = result + ' '
                if r < self.nRows-1 and c == self.nCols-1:
                    result = result + '\n'
        return result
