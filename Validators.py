import SudokuConstants as SCS
from Fields import Fields
from Board import Board
from BoardImporter import BoardImporterFromArray

class FieldsValidator:
    def nrFieldsWithValues(self, fields: Fields):
        result = 0            
        for field in fields.fields:
            if field.value != SCS.INITIAL:
                result += 1
        return result
    def IsValidValues(self, fields: Fields):
        values = []
        for field in fields.fields:
            if field.value != SCS.INITIAL:
                if field.value in values:
                    return False
                values.append(field.value)
        return True
    def IsCompleteValues(self, fields: Fields):
        return self.nrFieldsWithValues(fields) == len(fields.fields)

class BoardValidator:
    def __init__(self):
        self._fieldsValidator = FieldsValidator()

    def IsValidValues(self, board: Board):
        for r in range(SCS.BOARDSIZE):
            if not self._fieldsValidator.IsValidValues(board.Row(r)):
                return False
        for c in range(SCS.BOARDSIZE):
            if not self._fieldsValidator.IsValidValues(board.Column(c)):
                return False
        for brow in range(SCS.BLOCKSIZE):
            for bcol in range(SCS.BLOCKSIZE):
                if not self._fieldsValidator.IsValidValues(board.Block(brow, bcol)):
                    return False
        return True
    def IsCompleteValues(self, board: Board):
        for r in range(SCS.BOARDSIZE):
            if not self._fieldsValidator.IsCompleteValues(board.Row(r)):
                return False
        return True
    def nrFieldsWithValues(self, board: Board):
        result = 0
        for r in range(SCS.BOARDSIZE):
            result += self._fieldsValidator.nrFieldsWithValues(board.Row(r))
        return result
    def asString(self, board: Board):
        return 'Filled: {}/{}  Complete: {}   Valid: {}'.format(self.nrFieldsWithValues(board), board.nRows * board.nCols,
             self.IsCompleteValues(board), self.IsValidValues(board))
