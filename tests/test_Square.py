import pytest
import SudokuConstants as SCS
from Square import Square

class TestSquare:
    def test_Square_initial(self):
        square = Square()
        assert SCS.IsClear(square.value)

    def test_Square_assign(self):
        for i in range(1, SCS.GRIDSIZE+1):
            square = Square(i)
            assert square.value == i            
            square.value = i-1
            assert square.value == i-1

    def test_Square_error_negative(self):
        with pytest.raises(ValueError, match=SCS.INVALIDVALUEEXCEPTION):
            Square(-1)

    def test_Square_error_toohigh(self):
        with pytest.raises(ValueError, match=SCS.INVALIDVALUEEXCEPTION):
            Square(SCS.GRIDSIZE+1)

    def test_Square_value_toggle(self):
        for val in range(SCS.GRIDSIZE):
            square = Square(val)
            assert square.value == val
            square.clear()
            assert SCS.IsClear(square.value)
            square.value = val
            assert square.value == val
            