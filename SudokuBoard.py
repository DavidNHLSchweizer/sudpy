INVALIDROWEXCEPTION = 'invalid row'
INVALIDCOLEXCEPTION = 'invalid col'
INVALIDROWSEXCEPTION = 'invalid nr of rows'
INVALIDCOLSEXCEPTION = 'invalid nr of cols'
INVALIDVALUEEXCEPTION = 'invalid value'
INVALIDFIELDSEXCEPTION = 'invalid dimension of fields'
INVALIDSIZEEXCEPTION = 'invalid size'
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

class FieldGroup:
    def __init__(self, nrows, ncols, fields):
        if nrows <= 0 or nrows > BOARDSIZE:
            raise ValueError(INVALIDROWSEXCEPTION)
        if ncols <= 0 or ncols > BOARDSIZE:
            raise ValueError(INVALIDCOLSEXCEPTION)
        if nrows * ncols != BOARDSIZE:
            raise ValueError(INVALIDSIZEEXCEPTION)
        if fields == None:
            raise ValueError(INVALIDFIELDSEXCEPTION)
        if len(fields) != nrows:
            raise ValueError(INVALIDFIELDSEXCEPTION + ' {}'.format(len(fields)))
        for i in range(len(fields)):
            if len(fields[i]) != ncols:
                raise ValueError(INVALIDFIELDSEXCEPTION + ' {}, {}'.format(len(fields), len(fields[i])))
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
                str = str + (' |' if j else ': ') + '{} ({},{},{})'.format(j, field.row, field.col, field.value)
            print(str)
    
