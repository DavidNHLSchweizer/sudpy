import pytest
INVALIDROWEXCEPTION = 'invalid row'
INVALIDCOLEXCEPTION = 'invalid col'
INVALIDVALUEEXCEPTION = 'invalid value'
INITIAL   = 0
BOARDSIZE = 9

class Field:
    def __init__(self, row, col, value=INITIAL):
        if row < 0 or row >= BOARDSIZE:
            raise ValueError(INVALIDROWEXCEPTION)
        if col < 0 or col >= BOARDSIZE:
            raise ValueError(INVALIDCOLEXCEPTION)
        if not ((value == INITIAL) or (value >= 1 and value <= BOARDSIZE)):
            raise ValueError(INVALIDVALUEEXCEPTION + ' {}'.format(value))        
        self.row = row
        self.col = col
        self.value = value


class TestField:
    def test_range(self):
        f = Field(2,3)
        assert(f.row==2 and f.col==3)
        f = Field(0,0)
        assert(f.row==0 and f.col==0)
        f = Field(BOARDSIZE-1,BOARDSIZE-1)
        assert(f.row==BOARDSIZE-1 and f.col==BOARDSIZE-1)
        with pytest.raises(ValueError, match=INVALIDROWEXCEPTION):
            f = Field(-1,1)
        with pytest.raises(ValueError, match=INVALIDROWEXCEPTION):
            f = Field(BOARDSIZE,1)
        with pytest.raises(ValueError, match=INVALIDCOLEXCEPTION):
            f = Field(1,-1)
        with pytest.raises(ValueError, match=INVALIDCOLEXCEPTION):
            f = Field(1,BOARDSIZE)

    def test_value(self):        
        f = Field(2,3)
        assert(f.value==INITIAL)        
        f = Field(2,3,4)
        assert(f.value == 4)
        f = Field(2,3,1)
        assert(f.value == 1)
        f = Field(2,3,BOARDSIZE)
        assert(f.value == BOARDSIZE)
        with pytest.raises(ValueError, match=INVALIDVALUEEXCEPTION):
            f = Field(1,2,-1)
        with pytest.raises(ValueError, match=INVALIDVALUEEXCEPTION):
            f = Field(1,2,BOARDSIZE+1)
    





