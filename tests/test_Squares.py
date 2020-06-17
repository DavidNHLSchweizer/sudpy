import pytest
import SudokuConstants as SCS
from Square import Square
from Squares import Squares

class TestSquares:
    def _buildSingleSquares(self):
        self.singleSquares = []
        for i in range(1,SCS.GRIDSIZE+1):
            self.singleSquares.append(Square(i))
        return self.singleSquares

    def _getSquares(self):
        squares = Squares()
        for square in self._buildSingleSquares():
            squares.addSquare(square)
        return squares

    def test_squares_initialize(self):
        squares = self._getSquares()
        assert squares.nSquares == len(self.singleSquares)
        assert squares.nCols == squares.nSquares
        assert squares.nRows == 1
    
    def test_squares_clear(self):
        squares = self._getSquares()
        for square in squares.squares:
            assert not SCS.IsClear(square.value)
        squares.clear()
        for square in squares.squares:
            assert SCS.IsClear(square.value)

    def test_squares_asOneColumn(self):
        squares = self._getSquares()
        squares.nCols = 1
        assert squares.nRows == squares.nSquares
        assert squares.nCols == 1
        for r in range(squares.nRows):
            sq = squares.square(r, 0)
            assert sq.value == r+1

    def test_squares_asOneRow(self):
        squares = self._getSquares()
        squares.nRows = 1
        assert squares.nRows == 1
        assert squares.nCols == squares.nSquares
        for c in range(squares.nCols):
            sq = squares.square(0, c)
            assert sq.value == c+1
            
    def _test_squares_asBlock(self, squares):
        assert squares.nRows == SCS.BLOCKSIZE
        assert squares.nCols == SCS.BLOCKSIZE
        x = 1
        for r in range(squares.nRows):
            for c in range(squares.nCols):                
                sq = squares.square(r, c)
                assert sq.value == x
                x += 1
    
    def test_squares_asBlock1(self):
        squares = self._getSquares()
        squares.nCols = SCS.BLOCKSIZE
        self._test_squares_asBlock(squares)
    def test_squares_asBlock2(self):
        squares = self._getSquares()
        squares.nRows = SCS.BLOCKSIZE
        self._test_squares_asBlock(squares)

    def test_squares_squareRow_squareColumn_asOneRow(self):
        squares = self._getSquares()
        squares.nRows = 1
        c = 0
        for square in self.singleSquares:
            assert squares.sqRow(square) == 0
            assert squares.sqCol(square) == c
            c += 1

    def test_squares_squareRow_squareColumn_asOneColumn(self):
        squares = self._getSquares()
        squares.nCols = 1
        r = 0
        for square in self.singleSquares:
            assert squares.sqRow(square) == r
            assert squares.sqCol(square) == 0
            r += 1

    def test_squares_squareRow_squareColumn_asBlock(self):
        squares = self._getSquares()
        squares.nCols = SCS.BLOCKSIZE
        r = 0
        c = 0
        for square in self.singleSquares:
            assert squares.sqRow(square) == r
            assert squares.sqCol(square) == c            
            if c < SCS.BLOCKSIZE-1:
                c += 1
            else:
                c = 0
                r += 1


