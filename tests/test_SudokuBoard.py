import pytest
import SudokuConstants
import SudokuBoard 

class TestField:
    def test_Field_errors(self):
        with pytest.raises(ValueError, match=SudokuConstants.INVALIDVALUEEXCEPTION):
            SudokuBoard.Field(-1)
        with pytest.raises(ValueError, match=SudokuConstants.INVALIDVALUEEXCEPTION):
            SudokuBoard.Field(SudokuConstants.BOARDSIZE+1)

    def test_Field(self):        
        f = SudokuBoard.Field()
        assert f.value == SudokuConstants.INITIAL
        for value in range(SudokuConstants.BOARDSIZE):
            f = SudokuBoard.Field(value)
            assert f.value == value
    
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
        self.doFieldGroupTest(3, 3, [[SudokuBoard.Field(),SudokuBoard.Field(),SudokuBoard.Field()],
                                     [SudokuBoard.Field(),SudokuBoard.Field(),SudokuBoard.Field()],
                                     [SudokuBoard.Field(),SudokuBoard.Field(),SudokuBoard.Field()]])
        self.doFieldGroupTest(1, 9, [[SudokuBoard.Field(),SudokuBoard.Field(),SudokuBoard.Field(),
                                       SudokuBoard.Field(),SudokuBoard.Field(),SudokuBoard.Field(),
                                       SudokuBoard.Field(),SudokuBoard.Field(),SudokuBoard.Field()]])
        self.doFieldGroupTest(9, 1, [[SudokuBoard.Field()],[SudokuBoard.Field()],[SudokuBoard.Field()],
                                     [SudokuBoard.Field()],[SudokuBoard.Field()],[SudokuBoard.Field()],
                                     [SudokuBoard.Field()],[SudokuBoard.Field()],[SudokuBoard.Field()]])

    def test_fieldgroup_errors(self):
        with pytest.raises(ValueError, match=SudokuConstants.INVALIDROWSEXCEPTION):
            self.doFieldGroupTest(0, 9, [])
        with pytest.raises(ValueError, match=SudokuConstants.INVALIDROWSEXCEPTION):
            self.doFieldGroupTest(SudokuConstants.BOARDSIZE+1, 9, [])
        with pytest.raises(ValueError, match=SudokuConstants.INVALIDCOLSEXCEPTION):
            self.doFieldGroupTest(9, 0, [])
        with pytest.raises(ValueError, match=SudokuConstants.INVALIDCOLSEXCEPTION):
            self.doFieldGroupTest(9, SudokuConstants.BOARDSIZE+1, [])
        with pytest.raises(ValueError, match=SudokuConstants.INVALIDSIZEEXCEPTION):
            self.doFieldGroupTest(3, 4, [])
        with pytest.raises(ValueError, match=SudokuConstants.INVALIDFIELDSEXCEPTION):
            self.doFieldGroupTest(3, 3, None)
        with pytest.raises(ValueError, match=SudokuConstants.INVALIDFIELDSEXCEPTION):
            self.doFieldGroupTest(3, 3, [])
        with pytest.raises(ValueError, match=SudokuConstants.INVALIDFIELDSEXCEPTION):
            self.doFieldGroupTest(3, 3, [[SudokuBoard.Field(),SudokuBoard.Field(),SudokuBoard.Field()],
                                         [SudokuBoard.Field(),SudokuBoard.Field(),SudokuBoard.Field()]])
        with pytest.raises(ValueError, match=SudokuConstants.INVALIDFIELDSEXCEPTION):
            self.doFieldGroupTest(3, 3, [[SudokuBoard.Field(),SudokuBoard.Field(),SudokuBoard.Field()],
                                         [SudokuBoard.Field(),SudokuBoard.Field(),SudokuBoard.Field()],
                                         [SudokuBoard.Field(),SudokuBoard.Field(),SudokuBoard.Field()],
                                         [SudokuBoard.Field(),SudokuBoard.Field(),SudokuBoard.Field()]])
        with pytest.raises(ValueError, match=SudokuConstants.INVALIDFIELDSEXCEPTION):
            self.doFieldGroupTest(3, 3, [[SudokuBoard.Field(),SudokuBoard.Field(),SudokuBoard.Field()],
                                         [SudokuBoard.Field(),SudokuBoard.Field()],
                                         [SudokuBoard.Field(),SudokuBoard.Field(),SudokuBoard.Field()]])
