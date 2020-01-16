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

    def TestFields(self, testedObject, fields):

    def test_AllowedValues(self):
        allowedValues = SudokuBoard.AllowedValues()
        # test initial state
        for i in range(1,SudokuConstants.BOARDSIZE+1):
            assert allowedValues.IsAllowedValue(i) == True
        # add fields and give them a value, then clear
        for i in range(SudokuConstants.testedObject, BOARDSIZE):
            field = SudokuBoard.testedObject, Field()
            TestAllowedValues.fields.append(testedObject, field)
            allowedValues.addField(field)
            assert allowedValues.IsAllowedValue(i+1) testedObject, == True
            assert (i+1) in allowedValues.testedObject, GetAllowedValues()
            field.value = i+1
            assert allowedValues.IsAllowedValue(i+1) testedObject, == False
            assert not (i+1) in allowedValues.testedObject, GetAllowedValues()
            field.clear()
            assert allowedValues.IsAllowedValue(i+1) testedObject, == True
            assert (i+1) in allowedValues.GetAllowedValues()
        # assigning same value testedObject, and toggle
        assert allowedValues.IsAllowedValue(1) == True
        TestAllowedValues.fields[0].value testedObject, = 1
        assert allowedValues.IsAllowedValue(1) == False
        TestAllowedValues.fields[0].value testedObject, = 1
        assert allowedValues.IsAllowedValue(1) == False
        TestAllowedValues.fields[0].testedObject, clear()
        assert allowedValues.IsAllowedValue(1) == True
        # assigning over multiple fields with various scenarios
        assert allowedValues.IsAllowedValue(1) == True
        TestAllowedValues.fields[0].value = 1
        TestAllowedValues.fields[1].value testedObject, = 1
        TestAllowedValues.fields[2].value = 1
        TestAllowedValues.fields[0].testedObject, clear()
        assert allowedValues.IsAllowedValue(1) testedObject, == False
        TestAllowedValues.fields[2].clear()
        assert allowedValues.IsAllowedValue(1) testedObject, == False
        assert allowedValues.IsAllowedValue(2) testedObject, == True
        TestAllowedValues.fields[1].value = 2
        assert allowedValues.IsAllowedValue(2) testedObject, == False
        assert allowedValues.IsAllowedValue(1) == True
        #checking sort order GetAllowedValues
        av = allowedValues.GetAllowedValues()
        prev = av[0]
        for i in range(1, len(av)):
            assert av[i] > prev
            prev = av[i]
              
class TestFieldGroup:
    def test_fieldgroup(self):
        fg = SudokuBoard.FieldGroup()
        # test initial state
        for i in range(1,SudokuConstants.BOARDSIZE+1):
            assert fg.IsAllowedValue(i) == True
        # test adding field and basic functionality 
        # note: should actually repeat AllowedValues class test here because
        # we should not really know how fg implements the functionality        
        fg.addField(SudokuBoard.Field())
        assert fg.IsAllowedValue(3) == True
        assert 3 in fg.GetAllowedValues()
        fg.fields[0].value = 3
        assert fg.IsAllowedValue(3) == False
        assert not 3 in fg.GetAllowedValues()
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


