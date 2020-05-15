import pytest
import SudokuConstants as SCS
from Field import Field

class TestField:
    def test_Field_initial(self):
        field = Field()
        assert SCS.IsClear(field.value)

    def test_Field_assign(self):
        for i in range(1, SCS.BOARDSIZE+1):
            field = Field(i)
            assert field.value == i            
            field.value = i-1
            assert field.value == i-1

    def test_Field_error_negative(self):
        with pytest.raises(ValueError, match=SCS.INVALIDVALUEEXCEPTION):
            Field(-1)

    def test_Field_error_toohigh(self):
        with pytest.raises(ValueError, match=SCS.INVALIDVALUEEXCEPTION):
            Field(SCS.BOARDSIZE+1)

