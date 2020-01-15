import pytest
import SudokuBoard

class TestField:
    def test_Field_errors(self):
        f = SudokuBoard.Field(2,3)
        assert f.row==2 and f.col==3
        f = SudokuBoard.Field(0,0)
        assert f.row==0 and f.col==0
        f = SudokuBoard.Field(SudokuBoard.BOARDSIZE-1,SudokuBoard.BOARDSIZE-1)
        assert f.row==SudokuBoard.BOARDSIZE-1 and f.col==SudokuBoard.BOARDSIZE-1
        with pytest.raises(ValueError, match=SudokuBoard.INVALIDROWEXCEPTION):
            f = SudokuBoard.Field(-1,1)
        with pytest.raises(ValueError, match=SudokuBoard.INVALIDROWEXCEPTION):
            f = SudokuBoard.Field(SudokuBoard.BOARDSIZE,1)
        with pytest.raises(ValueError, match=SudokuBoard.INVALIDCOLEXCEPTION):
            f = SudokuBoard.Field(1,-1)
        with pytest.raises(ValueError, match=SudokuBoard.INVALIDCOLEXCEPTION):
            f = SudokuBoard.Field(1,SudokuBoard.BOARDSIZE)
        with pytest.raises(ValueError, match=SudokuBoard.INVALIDVALUEEXCEPTION):
            f = SudokuBoard.Field(1,2,-1)
        with pytest.raises(ValueError, match=SudokuBoard.INVALIDVALUEEXCEPTION):
            f = SudokuBoard.Field(1,2,SudokuBoard.BOARDSIZE+1)

    def test_Field(self):        
        f = SudokuBoard.Field(2,3)
        assert f.value==SudokuBoard.INITIAL
        f = SudokuBoard.Field(2,3,4)
        assert f.value == 4
        f = SudokuBoard.Field(2,3,1)
        assert f.value == 1
        f = SudokuBoard.Field(2,3,SudokuBoard.BOARDSIZE)
        assert f.value == SudokuBoard.BOARDSIZE
    
class TestFieldGroup:
    def doFieldGroupTest(self, nrows, ncols, fields):
        fg = SudokuBoard.FieldGroup(nrows, ncols, fields)
        assert nrows == fg.nrows
        assert ncols == fg.ncols
        assert len(fg.fields) == fg.nrows
        assert fg.ncols == fg.ncols
        for i in range(fg.nrows):
            assert len(fg.fields[i]) == fg.ncols
        for i in range(len(fields)):
            for j in range(len(fields[i])):
                assert fields[i][j]==fg.fields[i][j]

    def test_fieldgroup(self):
        self.doFieldGroupTest(3, 3, [[SudokuBoard.Field(2,0),SudokuBoard.Field(2,1),SudokuBoard.Field(2,2)],
                                     [SudokuBoard.Field(2,3),SudokuBoard.Field(2,4),SudokuBoard.Field(2,5)],
                                     [SudokuBoard.Field(2,6),SudokuBoard.Field(2,7),SudokuBoard.Field(2,8)]])
        self.doFieldGroupTest(1, 9, [[SudokuBoard.Field(2,0),SudokuBoard.Field(2,1),SudokuBoard.Field(2,2),
                                       SudokuBoard.Field(2,3),SudokuBoard.Field(2,4),SudokuBoard.Field(2,5),
                                       SudokuBoard.Field(2,6),SudokuBoard.Field(2,7),SudokuBoard.Field(2,8)]])
        self.doFieldGroupTest(9, 1, [[SudokuBoard.Field(0,5)],[SudokuBoard.Field(1,5)],[SudokuBoard.Field(2,5)],
                                     [SudokuBoard.Field(3,5)],[SudokuBoard.Field(4,5)],[SudokuBoard.Field(5,5)],
                                     [SudokuBoard.Field(6,5)],[SudokuBoard.Field(7,5)],[SudokuBoard.Field(8,5)]])

    def test_fieldgroup_errors(self):
        with pytest.raises(ValueError, match=SudokuBoard.INVALIDROWSEXCEPTION):
            self.doFieldGroupTest(0, 9, [])
        with pytest.raises(ValueError, match=SudokuBoard.INVALIDROWSEXCEPTION):
            self.doFieldGroupTest(SudokuBoard.BOARDSIZE+1, 9, [])
        with pytest.raises(ValueError, match=SudokuBoard.INVALIDCOLSEXCEPTION):
            self.doFieldGroupTest(9, 0, [])
        with pytest.raises(ValueError, match=SudokuBoard.INVALIDCOLSEXCEPTION):
            self.doFieldGroupTest(9, SudokuBoard.BOARDSIZE+1, [])
        with pytest.raises(ValueError, match=SudokuBoard.INVALIDSIZEEXCEPTION):
            self.doFieldGroupTest(3, 4, [])
        with pytest.raises(ValueError, match=SudokuBoard.INVALIDFIELDSEXCEPTION):
            self.doFieldGroupTest(3, 3, None)
        with pytest.raises(ValueError, match=SudokuBoard.INVALIDFIELDSEXCEPTION):
            self.doFieldGroupTest(3, 3, [])
        with pytest.raises(ValueError, match=SudokuBoard.INVALIDFIELDSEXCEPTION):
            self.doFieldGroupTest(3, 3, [[SudokuBoard.Field(2,0),SudokuBoard.Field(2,1),SudokuBoard.Field(2,2)],
                                         [SudokuBoard.Field(2,3),SudokuBoard.Field(2,4),SudokuBoard.Field(2,5)]])
        with pytest.raises(ValueError, match=SudokuBoard.INVALIDFIELDSEXCEPTION):
            self.doFieldGroupTest(3, 3, [[SudokuBoard.Field(2,0),SudokuBoard.Field(2,1),SudokuBoard.Field(2,2)],
                                         [SudokuBoard.Field(2,3),SudokuBoard.Field(2,4),SudokuBoard.Field(2,5)],
                                         [SudokuBoard.Field(2,3),SudokuBoard.Field(2,4),SudokuBoard.Field(2,5)],
                                         [SudokuBoard.Field(2,6),SudokuBoard.Field(2,7),SudokuBoard.Field(2,8)]])
        with pytest.raises(ValueError, match=SudokuBoard.INVALIDFIELDSEXCEPTION):
            self.doFieldGroupTest(3, 3, [[SudokuBoard.Field(2,0),SudokuBoard.Field(2,1),SudokuBoard.Field(2,2)],
                                         [SudokuBoard.Field(2,4),SudokuBoard.Field(2,5)],
                                         [SudokuBoard.Field(2,6),SudokuBoard.Field(2,7),SudokuBoard.Field(2,8)]])
