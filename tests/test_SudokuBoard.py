import pytest
import SudokuConstants
import SudokuBoard 
from AllowedValues import AllowedValues
from Value import Value
from typing import List 
from Fields import Field, Fields

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
            AV.addValue(v)
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
        pass
        #boardfields = []
        # # test initial state
        # for i in range(1,SudokuConstants.BOARDSIZE+1):
        #     assert fg.IsAllowedValue(i) == True
        # # test adding fields and basic functionality
        # for i in range(1, SudokuConstants.BOARDSIZE):
        #     fg.addField(SudokuBoard.Field())
        # TestAllowedValues.TestFields(fg, fg.fields)

        # # check bulk addition
        # fg2 = SudokuBoard.FieldGroup()
        # fg2.addFields(fg.fields)
        # for i in range(1, SudokuConstants.BOARDSIZE):
        #     assert fg.IsAllowedValue(i) == fg2.IsAllowedValue(i)
        # fg.clear()
        # for i in range(1, SudokuConstants.BOARDSIZE):
        #     assert fg.IsAllowedValue(i) == True
        # fg2.clear()
        # # check references to shared fields
        # fg.fields[0].value = 3
        # assert fg2.fields[0].value == 3
        # #check refcount on non-identical fieldgroups
        # fg.addField(SudokuBoard.Field(3))
        # fg2.fields[0].clear()
        # assert fg2.IsAllowedValue(3)
        # assert not fg.IsAllowedValue(3)


