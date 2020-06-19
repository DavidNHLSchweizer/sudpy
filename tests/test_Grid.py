import pytest
import SudokuConstants as SCS
from AllowedValues import AllowedValues
from Value import Value
from Square import Square
from Squares import Squares
from Grid import Grid

class TestGridInitialization:
    def test_grid_size(self):        
        grid = Grid()
        assert grid.nRows == SCS.GRIDSIZE
        assert grid.nCols == SCS.GRIDSIZE
        assert grid.nrSquaresWithValues() == 0

    def test_grid_rows(self):
        grid = Grid()
        for r in range(SCS.GRIDSIZE):
            for c in range(SCS.GRIDSIZE):
                square = grid.square(r,c)
                row = grid.Row(r)
                assert row._Contains(square)
                for c2 in range(SCS.GRIDSIZE):
                    if c2 != c:
                        assert row._Contains(grid.square(r, c2)) 

    def test_grid_columns(self):
        grid = Grid()        
        for r in range(SCS.GRIDSIZE):
            for c in range(SCS.GRIDSIZE):
                square = grid.square(r,c)
                col = grid.Column(c)
                assert col._Contains(square)
                for r2 in range(SCS.GRIDSIZE):
                    if r2 != r:
                        assert col._Contains(grid.square(r2, c))
    
    def test_grid_block(self):
        grid = Grid()
        for r in range(SCS.GRIDSIZE):
            for c in range(SCS.GRIDSIZE):
                square = grid.square(r,c)
                blk = grid.BlockFromSquare(r,c)
                assert blk._Contains(square)
                assert grid.sqRow(square) == r
                assert grid.sqCol(square) == c
                assert grid.sqBlock(square) == blk                
                r0 = (r // SCS.BLOCKSIZE) * SCS.BLOCKSIZE
                c0 = (c // SCS.BLOCKSIZE) * SCS.BLOCKSIZE
                for r2 in range(r0, r0 + SCS.BLOCKSIZE):
                    for c2 in range(c0, c0 + SCS.BLOCKSIZE):
                        if r2 != r or c2 != c:
                            assert blk._Contains(grid.square(r2, c2))

    def _testing_influencing_squares(self, square, value, assertExpected, subGrid):
        for square2 in subGrid.squares:
            if square2 != square:
                assert square2.IsAllowedValue(value) == assertExpected            
        
    def test_grid_allowed_values_initial(self):
        grid = Grid()
        for square in grid.squares:
            assert len(square.GetAllowedValues()) == SCS.GRIDSIZE

    def test_grid_allowed_values_rowcolblk(self):
        grid = Grid()
        square = grid.square(2,3)
        square.value = 5
        self._testing_influencing_squares(square, 5, False, grid.Row(2))
        self._testing_influencing_squares(square, 5, False, grid.Column(3))
        self._testing_influencing_squares(square, 5, False, grid.BlockFromSquare(2, 3))
        square.clear()
        self._testing_influencing_squares(square, 5, True, grid.Row(2))
        self._testing_influencing_squares(square, 5, True, grid.Column(3))
        self._testing_influencing_squares(square, 5, True, grid.BlockFromSquare(2, 3))

    def test_grid_allowed_values_rowcolblk2(self):
        grid = Grid()
        square = grid.square(2,3)
        square.value = 5
        self._testing_influencing_squares(square, 5, False, grid.Row(2))
        self._testing_influencing_squares(square, 5, False, grid.Column(3))
        self._testing_influencing_squares(square, 5, False, grid.BlockFromSquare(2, 3))
        self._testing_influencing_squares(square, 1, True, grid.Row(2))
        self._testing_influencing_squares(square, 1, True, grid.Column(3))
        self._testing_influencing_squares(square, 1, True, grid.BlockFromSquare(2, 3))
        square.value = 1
        self._testing_influencing_squares(square, 5, True, grid.Row(2))
        self._testing_influencing_squares(square, 5, True, grid.Column(3))
        self._testing_influencing_squares(square, 5, True, grid.BlockFromSquare(2, 3))
        self._testing_influencing_squares(square, 1, False, grid.Row(2))
        self._testing_influencing_squares(square, 1, False, grid.Column(3))
        self._testing_influencing_squares(square, 1, False, grid.BlockFromSquare(2, 3))

    def test_grid_allowed_values_rowcolblk3(self):
        grid = Grid()
        square = grid.square(3,3)
        square.value = 1
        square2 = grid.square(5, 3)
        assert not square2.IsAllowedValue(1)        
        assert square2.IsAllowedValue(5)
        assert square2.IsAllowedValue(6)
        assert square.IsAllowedValue(6)
        square2.value = 6
        assert not square.IsAllowedValue(6)
        square3 = grid.square(3, 5)
        square3.value = 6
        assert not square.IsAllowedValue(6)
        square2.clear()
        assert not square.IsAllowedValue(6)
        square3.clear()
        assert square.IsAllowedValue(6)

