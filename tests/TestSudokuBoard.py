import pytest
import SudokuBoard

class TestField:
    def test_range(self):
        f = SudokuBoard.Field(2,3)
        assert(f.row==2 and f.col==3)
        f = SudokuBoard.Field(0,0)
        assert(f.row==0 and f.col==0)
        f = SudokuBoard.Field(SudokuBoard.BOARDSIZE-1,SudokuBoard.BOARDSIZE-1)
        assert(f.row==SudokuBoard.BOARDSIZE-1 and f.col==SudokuBoard.BOARDSIZE-1)
        with pytest.raises(ValueError, match=SudokuBoard.INVALIDROWEXCEPTION):
            f = SudokuBoard.Field(-1,1)
        with pytest.raises(ValueError, match=SudokuBoard.INVALIDROWEXCEPTION):
            f = SudokuBoard.Field(SudokuBoard.BOARDSIZE,1)
        with pytest.raises(ValueError, match=SudokuBoard.INVALIDCOLEXCEPTION):
            f = SudokuBoard.Field(1,-1)
        with pytest.raises(ValueError, match=SudokuBoard.INVALIDCOLEXCEPTION):
            f = SudokuBoard.Field(1,SudokuBoard.BOARDSIZE)

    def test_value(self):        
        f = SudokuBoard.Field(2,3)
        assert(f.value==SudokuBoard.INITIAL)        
        f = SudokuBoard.Field(2,3,4)
        assert(f.value == 4)
        f = SudokuBoard.Field(2,3,1)
        assert(f.value == 1)
        f = SudokuBoard.Field(2,3,SudokuBoard.BOARDSIZE)
        assert(f.value == SudokuBoard.BOARDSIZE)
        with pytest.raises(ValueError, match=SudokuBoard.INVALIDVALUEEXCEPTION):
            f = SudokuBoard.Field(1,2,-1)
        with pytest.raises(ValueError, match=SudokuBoard.INVALIDVALUEEXCEPTION):
            f = SudokuBoard.Field(1,2,SudokuBoard.BOARDSIZE+1)
    


