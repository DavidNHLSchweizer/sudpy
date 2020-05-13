import pytest
import SudokuConstants
from Field import Field

class TestField:
    def test_Field_initial(self):
        field = Field()
        assert SudokuConstants.IsClear(field.value)

    def test_Field_assign(self):
        for i in range(1, SudokuConstants.BOARDSIZE+1):
            field = Field(i)
            assert field.value == i            
            field.value = i-1
            assert field.value == i-1

    def test_Field_error_negative(self):
        with pytest.raises(ValueError, match=SudokuConstants.INVALIDVALUEEXCEPTION):
            Field(-1)

    def test_Field_error_toohigh(self):
        with pytest.raises(ValueError, match=SudokuConstants.INVALIDVALUEEXCEPTION):
            Field(SudokuConstants.BOARDSIZE+1)

