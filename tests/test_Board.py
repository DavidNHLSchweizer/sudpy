import pytest
import SudokuConstants
from AllowedValues import AllowedValues
from Value import Value
from Field import Field
from Fields import Fields
from Board import Board

class TestBoardInitialization:
    def test_board_size(self):        
        board = Board()
        assert board.nRows == SudokuConstants.BOARDSIZE
        assert board.nCols == SudokuConstants.BOARDSIZE

    def test_board_rows(self):
        board = Board()
        for r in range(SudokuConstants.BOARDSIZE):
            for c in range(SudokuConstants.BOARDSIZE):
                field = board.field(r,c)
                row = field.Row
                assert row.nCols == SudokuConstants.BOARDSIZE
                assert row.nRows == 1
                assert row._Contains(field)
                for c2 in range(SudokuConstants.BOARDSIZE):
                    if c2 != c:
                        assert row._Contains(board.field(r, c2)) 

    def test_board_columns(self):
        board = Board()        
        for r in range(SudokuConstants.BOARDSIZE):
            for c in range(SudokuConstants.BOARDSIZE):
                field = board.field(r,c)
                col = field.Column
                assert col.nRows == SudokuConstants.BOARDSIZE
                assert col.nCols == 1
                assert col._Contains(field)
                for r2 in range(SudokuConstants.BOARDSIZE):
                    if r2 != r:
                        assert col._Contains(board.field(r2, c))
    
    def test_board_block(self):
        board = Board()
        for r in range(SudokuConstants.BOARDSIZE):
            for c in range(SudokuConstants.BOARDSIZE):
                field = board.field(r,c)
                blk = field.Block
                assert blk.nRows == SudokuConstants.BLOCKSIZE
                assert blk.nCols == SudokuConstants.BLOCKSIZE
                assert blk._Contains(field)
                assert board.fieldRow(field) == r
                assert board.fieldCol(field) == c                
                r0 = (r // SudokuConstants.BLOCKSIZE) * SudokuConstants.BLOCKSIZE
                c0 = (c // SudokuConstants.BLOCKSIZE) * SudokuConstants.BLOCKSIZE
                for r2 in range(r0, r0 + SudokuConstants.BLOCKSIZE):
                    for c2 in range(c0, c0 + SudokuConstants.BLOCKSIZE):
                        if r2 != r or c2 != c:
                            assert blk._Contains(board.field(r2, c2))

    def _testing_influencing_fields(self, field, value, assertExpected, fields):
        for f in fields.fields:
            if f != field:
                assert f.IsAllowedValue(value) == assertExpected            

    def test_board_allowed_values_initial(self):
        board = Board()
        for field in board.fields:
            assert len(field.GetAllowedValues()) == SudokuConstants.BOARDSIZE

    def test_board_allowed_values_rowcolblk(self):
        board = Board()
        field = board.field(3,3)
        field.value = 5
        self._testing_influencing_fields(field, 5, False, field.Row)
        self._testing_influencing_fields(field, 5, False, field.Column)
        self._testing_influencing_fields(field, 5, False, field.Block)
        field.clear()
        self._testing_influencing_fields(field, 5, True, field.Row)
        self._testing_influencing_fields(field, 5, True, field.Column)
        self._testing_influencing_fields(field, 5, True, field.Block)

    def test_board_allowed_values_rowcolblk2(self):
        board = Board()
        field = board.field(3,3)
        field.value = 5
        self._testing_influencing_fields(field, 5, False, field.Row)
        self._testing_influencing_fields(field, 5, False, field.Column)
        self._testing_influencing_fields(field, 5, False, field.Block)
        self._testing_influencing_fields(field, 1, True, field.Row)
        self._testing_influencing_fields(field, 1, True, field.Column)
        self._testing_influencing_fields(field, 1, True, field.Block)
        field.value = 1
        self._testing_influencing_fields(field, 5, True, field.Row)
        self._testing_influencing_fields(field, 5, True, field.Column)
        self._testing_influencing_fields(field, 5, True, field.Block)
        self._testing_influencing_fields(field, 1, False, field.Row)
        self._testing_influencing_fields(field, 1, False, field.Column)
        self._testing_influencing_fields(field, 1, False, field.Block)

    def test_board_allowed_values_rowcolblk3(self):
        board = Board()
        field = board.field(3,3)
        field.value = 1
        field2 = board.field(5, 3)
        assert not field2.IsAllowedValue(1)        
        assert field2.IsAllowedValue(5)
        assert field2.IsAllowedValue(6)
        assert field.IsAllowedValue(6)
        field2.value = 6
        assert not field.IsAllowedValue(6)
        field3 = board.field(3, 5)
        field3.value = 6
        assert not field.IsAllowedValue(6)
        field2.clear()
        assert not field.IsAllowedValue(6)
        field3.clear()
        assert field.IsAllowedValue(6)

