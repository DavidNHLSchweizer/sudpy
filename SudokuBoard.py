import SudokuConstants
from observerPattern import SimpleSubject, Observer

class Field(SimpleSubject):
    def __init__(self, value=SudokuConstants.INITIAL):
        super().__init__()
        if not ((value == SudokuConstants.INITIAL) or (value >= 1 and value <= SudokuConstants.BOARDSIZE)):
            raise ValueError(SudokuConstants.INVALIDVALUEEXCEPTION + ' {}'.format(value))
        self._value = value
        self._oldvalue = value

    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, newvalue):
        if (self.value == newvalue):
            return
        self._oldvalue = self._value
        self._value = newvalue
        self.notify()
        
class FieldGroup:
    def __init__(self, nrows, ncols, fields):
        if nrows <= 0 or nrows > SudokuConstants.BOARDSIZE:
            raise ValueError(SudokuConstants.INVALIDROWSEXCEPTION)
        if ncols <= 0 or ncols > SudokuConstants.BOARDSIZE:
            raise ValueError(SudokuConstants.INVALIDCOLSEXCEPTION)
        if nrows * ncols != SudokuConstants.BOARDSIZE:
            raise ValueError(SudokuConstants.INVALIDSIZEEXCEPTION)
        if fields == None:
            raise ValueError(SudokuConstants.INVALIDFIELDSEXCEPTION)
        if len(fields) != nrows:
            raise ValueError(SudokuConstants.INVALIDFIELDSEXCEPTION + ' {}'.format(len(fields)))
        for i in range(len(fields)):
            if len(fields[i]) != ncols:
                raise ValueError(SudokuConstants.INVALIDFIELDSEXCEPTION + ' {}, {}'.format(len(fields), len(fields[i])))
        self.nrows = nrows
        self.ncols = ncols
        self.fields = fields

    def dump(self):
        print('fieldgroup : {} rows by {} cols'.format(self.nrows, self.ncols))
        print('fields: ')
        for i in range(self.nrows):
            str = 'row {}'.format(i)
            for j in range(self.ncols):
                field = self.fields[i][j]
                str = str + (' |' if j else ': ') + '{} ({})'.format(j, field.value)
            print(str)

   
f = Field()
print(f.value)
print(f.observers)
