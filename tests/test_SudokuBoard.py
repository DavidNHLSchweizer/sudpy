import pytest
import SudokuConstants
import SudokuBoard 
from typing import List 

class TestField:
    def test_Field_errors(self):
        with pytest.raises(ValueError, match=SudokuConstants.INVALIDVALUEEXCEPTION):
            SudokuBoard.Field(-1)
        with pytest.raises(ValueError, match=SudokuConstants.INVALIDVALUEEXCEPTION):
            SudokuBoard.Field(SudokuConstants.BOARDSIZE+1)

    def test_Field(self):        
        f = SudokuBoard.Field()
        assert SudokuBoard.IsClear(f.value)
        for value in range(SudokuConstants.BOARDSIZE):
            f = SudokuBoard.Field(value)
            assert f.value == value

class TestAllowedValues:
    fields = []
    def test_AllowedValues(self):
        keeper = SudokuBoard.AllowedValues()
        # test initial state
        for i in range(1,SudokuConstants.BOARDSIZE+1):
            assert keeper.IsAllowedValue(i) == True
        # add fields and give them a value, then clear
        for i in range(SudokuConstants.BOARDSIZE):
            field = SudokuBoard.Field()
            TestAllowedValues.fields.append(field)
            keeper.addField(field)
            assert keeper.IsAllowedValue(i+1) == True
            assert (i+1) in keeper.GetAllowedValues()
            field.value = i+1
            assert keeper.IsAllowedValue(i+1) == False
            assert not (i+1) in keeper.GetAllowedValues()
            field.clear()
            assert keeper.IsAllowedValue(i+1) == True
            assert (i+1) in keeper.GetAllowedValues()
        # assigning same value and toggle
        assert keeper.IsAllowedValue(1) == True
        TestAllowedValues.fields[0].value = 1
        assert keeper.IsAllowedValue(1) == False
        TestAllowedValues.fields[0].value = 1
        assert keeper.IsAllowedValue(1) == False
        TestAllowedValues.fields[0].clear()
        assert keeper.IsAllowedValue(1) == True
        # assigning over multiple fields with various scenarios
        assert keeper.IsAllowedValue(1) == True
        TestAllowedValues.fields[0].value = 1
        TestAllowedValues.fields[1].value = 1
        TestAllowedValues.fields[2].value = 1
        TestAllowedValues.fields[0].clear()
        assert keeper.IsAllowedValue(1) == False
        TestAllowedValues.fields[2].clear()
        assert keeper.IsAllowedValue(1) == False
        assert keeper.IsAllowedValue(2) == True
        TestAllowedValues.fields[1].value = 2
        assert keeper.IsAllowedValue(2) == False
        assert keeper.IsAllowedValue(1) == True
        #checking sort order GetAllowedValues
        av = keeper.GetAllowedValues()
        prev = av[0]
        for i in range(1, len(av)):
            assert av[i] > prev
            prev = av[i]

            


        
          
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
