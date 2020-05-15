import pytest
import SudokuConstants
from Field import Field
from Fields import Fields

class TestFields:
    def _buildSingleFields(self):
        self.singleFields = []
        for i in range(1,SudokuConstants.BOARDSIZE+1):
            self.singleFields.append(Field(i))
        return self.singleFields

    def _getFields(self):
        fields = Fields()
        for field in self._buildSingleFields():
            fields.addField(field)
        return fields

    def test_fields_initialize(self):
        fields = self._getFields()
        assert fields.nFields == len(self.singleFields)
    
    def test_fields_value_toggle(self):
        fields = self._getFields()
        for field in fields.fields:
            val = field.value
            field.clear()
            #assert fields.nrAllowedValues() == 1
            field.value = val
            #assert fields.nrAllowedValues() == 0

    def test_fields_asOneColumn(self):
        fields = self._getFields()
        fields.nCols = 1
        assert fields.nRows == SudokuConstants.BOARDSIZE
        assert fields.nCols == 1
        for r in range(SudokuConstants.BOARDSIZE):
            f = fields.field(r, 0)
            assert f.value == r+1

    def test_fields_asOneRow(self):
        fields = self._getFields()
        fields.nCols = SudokuConstants.BOARDSIZE
        assert fields.nRows == 1
        assert fields.nCols == SudokuConstants.BOARDSIZE
        for c in range(SudokuConstants.BOARDSIZE):
            f = fields.field(0, c)
            assert f.value == c+1

    def test_fields_asBlock(self):
        fields = self._getFields()
        x = 1
        fields.nCols = SudokuConstants.BLOCKSIZE
        assert fields.nRows == SudokuConstants.BLOCKSIZE
        assert fields.nCols == SudokuConstants.BLOCKSIZE
        for r in range(SudokuConstants.BLOCKSIZE):
            for c in range(SudokuConstants.BLOCKSIZE):                
                f = fields.field(r, c)
                assert f.value == x
                x += 1

    def test_fields_fieldRow_fieldColumn_asOneRow(self):
        fields = self._getFields()
        fields.nCols = SudokuConstants.BOARDSIZE
        c = 0
        for field in self.singleFields:
            assert fields.fieldRow(field) == 0
            assert fields.fieldCol(field) == c
            c += 1

    def test_fields_fieldRow_fieldColumn_asOneColumn(self):
        fields = self._getFields()
        fields.nCols = 1
        r = 0
        for field in self.singleFields:
            assert fields.fieldRow(field) == r
            assert fields.fieldCol(field) == 0
            r += 1

    def test_fields_fieldRow_fieldColumn_asBlock(self):
        fields = self._getFields()
        fields.nCols = SudokuConstants.BLOCKSIZE
        r = 0
        c = 0
        for field in self.singleFields:
            assert fields.fieldRow(field) == r
            assert fields.fieldCol(field) == c            
            if c < SudokuConstants.BLOCKSIZE-1:
                c += 1
            else:
                c = 0
                r += 1
