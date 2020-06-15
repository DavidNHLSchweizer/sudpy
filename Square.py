import SudokuConstants as SCS
from Value import Value
from AllowedValues import ContainsAllowedValues
 
class Square(ContainsAllowedValues):
    def __init__(self, value = SCS.INITIAL):
        super().__init__()
        self._value = Value(value)
        self._row    = None
        self._column = None
        self._block  = None
    @property
    def value(self):
        return self._value.value
    @value.setter
    def value(self, newvalue):
        self._value.value = newvalue
    def _validateSquares(self, squares):
        if not squares:
            return False
        if len(squares) != SCS.GRIDSIZE:
            raise SCS.INVALIDSQUARESEXCEPTION
        if not self in squares:
            raise SCS.INVALIDSQUARESEXCEPTION2
        return True
    def _removeInfluencingSquares(self, squares):
        if not self._validateSquares(squares):
            return
        for square in squares:
            if square != self:
                self.StopObserveValue(square._value)
    def _addInfluencingSquares(self, squares):        
        if not self._validateSquares(squares):
            return
        for square in squares:
            if square != self:
                self.ObserveValue(square._value)
    @property
    def Row(self):
        return self._row
    @Row.setter
    def Row(self, rowSquares):
        if self._row:
            self._removeInfluencingSquares(self._row.squares)            
        self._row = rowSquares
        self._addInfluencingSquares(rowSquares.squares)        
    @property
    def Column(self):
        return self._column
    @Column.setter
    def Column(self, columnSquares):
        if self._column:
            self._removeInfluencingSquares(self._column.squares)
        self._column = columnSquares
        self._addInfluencingSquares(columnSquares.squares)        
    @property
    def Block(self):
        return self._block
    @Block.setter
    def Block(self, blockSquares):
        if self._block:
            self._removeInfluencingSquares(self._block.squares)
        self._block = blockSquares
        self._addInfluencingSquares(blockSquares.squares)
    def fixValue(self):
        self._value._fixedValue = True        
    def unfixValue(self):
        self._value._fixedValue = False        
    def clear(self):
        self._value.clear()
        