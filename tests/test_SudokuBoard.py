import pytest
import SudokuConstants
from AllowedValues import AllowedValues
from Value import Value
from typing import List 
from Fields import Field, Fields
from Board import Board

class TestValue:
    def test_value(self):
        # test initializations
        value = Value()
        assert SudokuConstants.IsClear(value.value)        
        for v in range(1,SudokuConstants.BOARDSIZE+1):
            value = Value(v)
            assert value.value == v
            assert SudokuConstants.IsClear(value.oldvalue)        
        # test assignments
        value = Value(2)
        oldvalue = 2
        for v in range(SudokuConstants.BOARDSIZE+1):
            value.value = v
            assert value.value == v
            assert value.oldvalue == oldvalue
            oldvalue = v
        assert not SudokuConstants.IsClear(value.value)
        # test clearing
        value.clear()
        assert SudokuConstants.IsClear(value.value)
        assert SudokuConstants.IsClear(value.oldvalue)
        #test invalid values (initialization and assignment)
        with pytest.raises(ValueError, match=SudokuConstants.INVALIDVALUEEXCEPTION):
            Value(-1)
        with pytest.raises(ValueError, match=SudokuConstants.INVALIDVALUEEXCEPTION):
            value.value = -1
        with pytest.raises(ValueError, match=SudokuConstants.INVALIDVALUEEXCEPTION):
            Value(SudokuConstants.BOARDSIZE+1)
        with pytest.raises(ValueError, match=SudokuConstants.INVALIDVALUEEXCEPTION):
            value.value = SudokuConstants.BOARDSIZE+1

class TestAllowedValues:
    def test_allowedValues(self):
        AV = AllowedValues()
        # test initial state
        for i in range(1,SudokuConstants.BOARDSIZE+1):
            assert AV.IsAllowedValue(i) == True
        # create set of Value objects to observe and add to observer
        values = []
        for i in range(1,SudokuConstants.BOARDSIZE+1):
            values.append(Value(i))
        for v in values:
            assert AV.IsAllowedValue(v.value) == True
            AV.ObserveValue(v)
            assert AV.IsAllowedValue(v.value) == False
        # clear a Value, then assign the value to another Value
        testvalue = values[2].value
        values[2].clear()
        assert AV.IsAllowedValue(testvalue)
        assert testvalue in AV.GetAllowedValues()
        values[0].value = testvalue
        assert not AV.IsAllowedValue(testvalue)
        assert not testvalue in AV.GetAllowedValues()
        # toggling 
        values[0].clear()
        assert AV.IsAllowedValue(testvalue) == True
        values[0].value = testvalue
        assert AV.IsAllowedValue(testvalue) == False
        values[0].clear()
        assert AV.IsAllowedValue(testvalue) == True
        # assigning over multiple values with various scenarios
        for value in values:
            value.clear()
        assert AV.IsAllowedValue(testvalue) == True
        values[0].value = testvalue
        values[1].value = testvalue
        values[2].value = testvalue
        values[0].clear()
        assert AV.IsAllowedValue(testvalue) == False
        values[2].clear()
        assert AV.IsAllowedValue(testvalue) == False
        assert AV.IsAllowedValue(testvalue+1) == True
        values[1].value = testvalue+1
        assert AV.IsAllowedValue(testvalue+1) == False
        assert AV.IsAllowedValue(testvalue) == True
        #checking sort order GetAllowedValues
        av = AV.GetAllowedValues()
        assert len(av) == SudokuConstants.BOARDSIZE - 1
        prev = av[0]
        for i in range(1, len(av)):
            assert av[i] > prev
            prev = av[i]

class TestField:
    def test_Field(self):
        field = Field()
        assert SudokuConstants.IsClear(field.value)
        for i in range(1, SudokuConstants.BOARDSIZE+1):
            field = Field(i)
            assert field.value == i
            field.value = i-1
            assert field.value == i-1
        with pytest.raises(ValueError, match=SudokuConstants.INVALIDVALUEEXCEPTION):
            Field(-1)
        with pytest.raises(ValueError, match=SudokuConstants.INVALIDVALUEEXCEPTION):
            Field(SudokuConstants.BOARDSIZE+1)

class TestFields:
    def test_fields(self):
        singleFields = []
        for i in range(1,SudokuConstants.BOARDSIZE+1):
            singleFields.append(Field(i))
    # test on values
        fields = Fields()
        for field in singleFields:
            fields.addField(field)
        assert len(fields.GetAllowedValues()) == 0
        val = singleFields[0].value
        singleFields[0].clear()
        assert len(fields.GetAllowedValues()) == 1
        singleFields[0].value = val
    # testing the fields property
        #one column configuration
        fields.nCols = 1
        for r in range(SudokuConstants.BOARDSIZE):
            f = fields.field(r, 0)
            assert f.value == r+1
        #one row configuration
        fields.nCols = SudokuConstants.BOARDSIZE
        for c in range(SudokuConstants.BOARDSIZE):
            f = fields.field(0, c)
            assert f.value == c+1
        #block configuration
        x = 1
        fields.nCols = SudokuConstants.BLOCKSIZE
        for r in range(SudokuConstants.BLOCKSIZE):
            for c in range(SudokuConstants.BLOCKSIZE):                
                f = fields.field(r, c)
                assert f.value == x
                x += 1
    # testing the fieldRow and fieldColumn properties
        #one row configuration
        fields.nCols = SudokuConstants.BOARDSIZE
        assert fields.nRows == 1
        assert fields.nCols == SudokuConstants.BOARDSIZE
        c = 0
        for field in singleFields:
            assert fields.fieldRow(field) == 0
            assert fields.fieldCol(field) == c
            c += 1
        #one column configuration
        fields.nCols = 1
        assert fields.nCols == 1
        assert fields.nRows == SudokuConstants.BOARDSIZE
        r = 0
        for field in singleFields:
            assert fields.fieldRow(field) == r
            assert fields.fieldCol(field) == 0
            r += 1
        #block configuration
        fields.nCols = SudokuConstants.BLOCKSIZE
        assert fields.nCols == SudokuConstants.BLOCKSIZE
        assert fields.nRows == SudokuConstants.BLOCKSIZE
        r = 0
        c = 0
        for field in singleFields:
            assert fields.fieldRow(field) == r
            assert fields.fieldCol(field) == c            
            if c < SudokuConstants.BLOCKSIZE-1:
                c += 1
            else:
                c = 0
                r += 1

    def test_fields_for_board(self):        
        board = Board()
        #basic sanity check
        assert board.nRows == SudokuConstants.BOARDSIZE
        assert board.nCols == SudokuConstants.BOARDSIZE
        #check row for each field
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
        #check column for each field
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
        #check block for each field
        for r in range(SudokuConstants.BOARDSIZE):
            for c in range(SudokuConstants.BOARDSIZE):
                field = board.field(r,c)
                blk = field.Block
                assert blk.nRows == SudokuConstants.BLOCKSIZE
                assert blk.nCols == SudokuConstants.BLOCKSIZE
                assert blk._Contains(field)
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

    def test_board_allowed_values(self):
        board = Board()
        for field in board.fields:
            assert len(field.GetAllowedValues()) == SudokuConstants.BOARDSIZE
        field = board.field(3,3)
        field.value = 5
        self._testing_influencing_fields(field, 5, False, field.Row)
        self._testing_influencing_fields(field, 5, False, field.Column)
        self._testing_influencing_fields(field, 5, False, field.Block)
        field.clear()
        self._testing_influencing_fields(field, 5, True, field.Row)
        self._testing_influencing_fields(field, 5, True, field.Column)
        self._testing_influencing_fields(field, 5, True, field.Block)
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
