import pytest
import SudokuConstants
from Value import Value

class TestValue:
    def test_value_initialization(self):
        # test initializations
        value = Value()
        assert SudokuConstants.IsClear(value.value)

    def test_value_assignment_initial(self):
        for v in range(1,SudokuConstants.BOARDSIZE+1):
            value = Value(v)
            assert value.value == v
            assert SudokuConstants.IsClear(value.oldvalue)

    def test_value_assignment_newvalue(self):
        value = Value(2)
        oldvalue = 2
        for v in range(SudokuConstants.BOARDSIZE+1):
            value.value = v
            assert value.value == v
            assert value.oldvalue == oldvalue
            oldvalue = v
        assert not SudokuConstants.IsClear(value.value)
    
    def test_clear(self):
        value = Value(3)
        assert value.value == 3
        value.clear()
        assert SudokuConstants.IsClear(value.value)

    def test_clear_oldvalue(self):
        value = Value(3)
        value.value = 4
        assert value.value == 4
        assert value.oldvalue == 3
        value.clear()
        assert SudokuConstants.IsClear(value.value)
        assert SudokuConstants.IsClear(value.oldvalue)

    def test_invalid_value_negative(self):
        with pytest.raises(ValueError, match=SudokuConstants.INVALIDVALUEEXCEPTION):
            Value(-1)
    def test_invalid_value_negative2(self):
        with pytest.raises(ValueError, match=SudokuConstants.INVALIDVALUEEXCEPTION):
            Value().value = -1
    def test_invalid_value_toohigh(self):
        with pytest.raises(ValueError, match=SudokuConstants.INVALIDVALUEEXCEPTION):
            Value(SudokuConstants.BOARDSIZE+1)
    def test_invalid_value_toohigh2(self):
        with pytest.raises(ValueError, match=SudokuConstants.INVALIDVALUEEXCEPTION):
            Value().value = SudokuConstants.BOARDSIZE+1
