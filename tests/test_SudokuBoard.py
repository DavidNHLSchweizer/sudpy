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

def _TestFieldsAndAllowedValues(testedObject, fields):
    # clear and test initial state
    testedObject.clear()
    for i in range(1,SudokuConstants.BOARDSIZE+1):
        assert testedObject.IsAllowedValue(i) == True
    # add fields and give them a value, then clear
    value = 1
    for field in fields:
        testedObject.addField(field)
        assert testedObject.IsAllowedValue(value) == True
        assert value in testedObject.GetAllowedValues()
        field.value = value
        assert testedObject.IsAllowedValue(value) == False
        assert not value in testedObject.GetAllowedValues()
        field.clear()
        assert testedObject.IsAllowedValue(value) == True
        assert value in testedObject.GetAllowedValues()
        value += 1
    # assigning same value and toggle
    assert testedObject.IsAllowedValue(1) == True
    fields[0].value = 1
    assert testedObject.IsAllowedValue(1) == False
    fields[0].value = 1
    assert testedObject.IsAllowedValue(1) == False
    fields[0].clear()
    assert testedObject.IsAllowedValue(1) == True
    # assigning over multiple fields with various scenarios
    assert testedObject.IsAllowedValue(1) == True
    fields[0].value = 1
    fields[1].value = 1
    fields[2].value = 1
    fields[0].clear()
    assert testedObject.IsAllowedValue(1) == False
    fields[2].clear()
    assert testedObject.IsAllowedValue(1) == False
    assert testedObject.IsAllowedValue(2) == True
    fields[1].value = 2
    assert testedObject.IsAllowedValue(2) == False
    assert testedObject.IsAllowedValue(1) == True
    #checking sort order GetAllowedValues
    av = testedObject.GetAllowedValues()
    prev = av[0]
    for i in range(1, len(av)):
        assert av[i] > prev
        prev = av[i]

class TestAllowedValues:
    def test_AllowedValues(self):
        allowedValues = SudokuBoard.AllowedValues()
        fields = []
        # add some fields 
        for i in range(1, SudokuConstants.BOARDSIZE):
            fields.append(SudokuBoard.Field())
        _TestFieldsAndAllowedValues(allowedValues, fields)
               
class TestFieldGroup:
    def test_fieldgroup(self):
        fg = SudokuBoard.FieldGroup()
        # test initial state
        for i in range(1,SudokuConstants.BOARDSIZE+1):
            assert fg.IsAllowedValue(i) == True
        # test adding fields and basic functionality
        for i in range(1, SudokuConstants.BOARDSIZE):
            fg.addField(SudokuBoard.Field())
        TestAllowedValues.TestFields(fg, fg.fields)

        # check bulk addition
        fg2 = SudokuBoard.FieldGroup()
        fg2.addFields(fg.fields)
        for i in range(1, SudokuConstants.BOARDSIZE):
            assert fg.IsAllowedValue(i) == fg2.IsAllowedValue(i)
        fg.clear()
        for i in range(1, SudokuConstants.BOARDSIZE):
            assert fg.IsAllowedValue(i) == True
        fg2.clear()
        # check references to shared fields
        fg.fields[0].value = 3
        assert fg2.fields[0].value == 3
        #check refcount on non-identical fieldgroups
        fg.addField(SudokuBoard.Field(3))
        fg2.fields[0].clear()
        assert fg2.IsAllowedValue(3)
        assert not fg.IsAllowedValue(3)


