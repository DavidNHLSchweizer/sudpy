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

    def test_grid_rows(self):
        grid = Grid()
        for r in range(SCS.GRIDSIZE):
            for c in range(SCS.GRIDSIZE):
                square = grid.square(r,c)
                row = square.Row
                assert row.nCols == SCS.GRIDSIZE
                assert row.nRows == 1
                assert row._Contains(square)
                for c2 in range(SCS.GRIDSIZE):
                    if c2 != c:
                        assert row._Contains(grid.square(r, c2)) 

    def test_grid_columns(self):
        grid = Grid()        
        for r in range(SCS.GRIDSIZE):
            for c in range(SCS.GRIDSIZE):
                square = grid.square(r,c)
                col = square.Column
                assert col.nRows == SCS.GRIDSIZE
                assert col.nCols == 1
                assert col._Contains(square)
                for r2 in range(SCS.GRIDSIZE):
                    if r2 != r:
                        assert col._Contains(grid.square(r2, c))
    
    def test_grid_block(self):
        grid = Grid()
        for r in range(SCS.GRIDSIZE):
            for c in range(SCS.GRIDSIZE):
                square = grid.square(r,c)
                blk = square.Block
                assert blk.nRows == SCS.BLOCKSIZE
                assert blk.nCols == SCS.BLOCKSIZE
                assert blk._Contains(square)
                assert grid.sqRow(square) == r
                assert grid.sqCol(square) == c                
                r0 = (r // SCS.BLOCKSIZE) * SCS.BLOCKSIZE
                c0 = (c // SCS.BLOCKSIZE) * SCS.BLOCKSIZE
                for r2 in range(r0, r0 + SCS.BLOCKSIZE):
                    for c2 in range(c0, c0 + SCS.BLOCKSIZE):
                        if r2 != r or c2 != c:
                            assert blk._Contains(grid.square(r2, c2))

    def _testing_influencing_squares(self, square, value, assertExpected, squares):
        for f in squares.squares:
            if f != square:
                assert f.IsAllowedValue(value) == assertExpected            

    def test_grid_allowed_values_initial(self):
        grid = Grid()
        for square in grid.squares:
            assert len(square.GetAllowedValues()) == SCS.GRIDSIZE

    def test_grid_allowed_values_rowcolblk(self):
        grid = Grid()
        square = grid.square(3,3)
        square.value = 5
        self._testing_influencing_squares(square, 5, False, square.Row)
        self._testing_influencing_squares(square, 5, False, square.Column)
        self._testing_influencing_squares(square, 5, False, square.Block)
        square.clear()
        self._testing_influencing_squares(square, 5, True, square.Row)
        self._testing_influencing_squares(square, 5, True, square.Column)
        self._testing_influencing_squares(square, 5, True, square.Block)

    def test_grid_allowed_values_rowcolblk2(self):
        grid = Grid()
        square = grid.square(3,3)
        square.value = 5
        self._testing_influencing_squares(square, 5, False, square.Row)
        self._testing_influencing_squares(square, 5, False, square.Column)
        self._testing_influencing_squares(square, 5, False, square.Block)
        self._testing_influencing_squares(square, 1, True, square.Row)
        self._testing_influencing_squares(square, 1, True, square.Column)
        self._testing_influencing_squares(square, 1, True, square.Block)
        square.value = 1
        self._testing_influencing_squares(square, 5, True, square.Row)
        self._testing_influencing_squares(square, 5, True, square.Column)
        self._testing_influencing_squares(square, 5, True, square.Block)
        self._testing_influencing_squares(square, 1, False, square.Row)
        self._testing_influencing_squares(square, 1, False, square.Column)
        self._testing_influencing_squares(square, 1, False, square.Block)

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

