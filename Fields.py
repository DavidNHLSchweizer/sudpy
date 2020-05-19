import SudokuConstants as SCS
from Field import Field

class Fields:
    def __init__(self):
        self.fields = []
        self._nCols = 0
    def addField(self, field: Field):
        self.fields.append(field)
        self._nCols += 1
    def addFields(self, fields):
        for field in fields: 
            self.addField(field)
    def _GetIndex(self, field):
        if not field in self.fields:
            return SCS.INDEXNOTFOUND        
        return self.fields.index(field)
    def _Contains(self, field):
        return field in self.fields
    def _RowColToIndex(self, row, col):
        return row * self.nCols + col
    def _IndexToRow(self, index):
        return index // self.nCols
    def _IndexToCol(self, index):
        return index % self.nCols
    def _CheckLegalBase(self, row, col, maxRows, maxCols):
        if row < 0 or row >= maxRows:
            ValueError(SCS.INVALIDROWSEXCEPTION + ' {}'.format(row))
        if col < 0 or col >= maxCols:
            ValueError(SCS.INVALIDCOLSEXCEPTION + ' {}'.format(col))
    def _CheckLegal(self, row, col):
        self._CheckLegalBase(row, col, self.nRows, self.nCols)
    def field(self, row, col):
        self._CheckLegal(row, col)
        return self.fields[self._RowColToIndex(row, col)]
    def clear(self):
        for f in self.fields:
            f.clear()
    def fieldRow(self, field):
        return self._IndexToRow(self._GetIndex(field))
    def fieldCol(self, field):
        return self._IndexToCol(self._GetIndex(field))
    @property
    def nCols(self)->int:
        return self._nCols
    @nCols.setter
    def nCols(self, value):
        if value <= 0 or value > len(self.fields) or len(self.fields) % value != 0:
            raise ValueError(SCS.INVALIDCOLSEXCEPTION + ' {}'.format(value))
        self._nCols = value
    @property
    def nRows(self)->int:
        return len(self.fields) // self.nCols
    @property
    def nFields(self)->int:
        return len(self.fields)
    def asString(self):
        result = ''
        for r in range(self.nRows):
            for c in range(self.nCols):
                field = self.field(r, c)
                result = result + ('0' if field.value == SCS.INITIAL else str(field.value))
                if c % 3 == 2:
                    result = result + ' '
                if r < self.nRows-1 and c == self.nCols-1:
                    result = result + '\n'
        return result
    