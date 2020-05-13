import SudokuConstants
from Field import Field
from Fields import Fields
from Board import Board
from Validators import FieldsValidator, BoardValidator
from BoardImporter import BoardImporterFromArray

class TestFieldsValidator:
    def _initFields(self, nCols):
        fields = Fields()
        for _ in range(SudokuConstants.BOARDSIZE):
            fields.addField(Field())
        fields.nCols = nCols        
        return fields

    def test_initial(self):
        fields = self._initFields(SudokuConstants.BOARDSIZE)
        FV = FieldsValidator()
        assert FV.nrFieldsWithValues(fields) == 0
        assert FV.IsCompleteValues(fields) == False
        assert FV.IsValidValues(fields) == True
    def test_one_value(self):
        fields = self._initFields(SudokuConstants.BOARDSIZE)
        FV = FieldsValidator()
        field = fields.fields[0]
        field.value = 1
        assert FV.nrFieldsWithValues(fields) == 1
        assert FV.IsCompleteValues(fields) == False
        assert FV.IsValidValues(fields) == True
    def test_two_values_valid(self):
        fields = self._initFields(SudokuConstants.BOARDSIZE)
        FV = FieldsValidator()
        fields.fields[0].value = 1
        fields.fields[SudokuConstants.BOARDSIZE-1].value = 2
        assert FV.nrFieldsWithValues(fields) == 2
        assert FV.IsCompleteValues(fields) == False
        assert FV.IsValidValues(fields) == True
    def test_two_values_invalid(self):
        fields = self._initFields(SudokuConstants.BOARDSIZE)
        FV = FieldsValidator()
        fields.fields[0].value = 1
        fields.fields[SudokuConstants.BOARDSIZE-1].value = 1
        assert FV.nrFieldsWithValues(fields) == 2
        assert FV.IsCompleteValues(fields) == False
        assert FV.IsValidValues(fields) == False
    def test_full_values_valid(self):
        fields = self._initFields(SudokuConstants.BOARDSIZE)
        FV = FieldsValidator()
        for i in range(SudokuConstants.BOARDSIZE):
            fields.fields[i].value = i+1
        assert FV.nrFieldsWithValues(fields) == SudokuConstants.BOARDSIZE
        assert FV.IsCompleteValues(fields) == True
        assert FV.IsValidValues(fields) == True
    def test_full_values_invalid(self):
        fields = self._initFields(SudokuConstants.BOARDSIZE)
        FV = FieldsValidator()
        for i in range(SudokuConstants.BOARDSIZE):
            fields.fields[i].value = 3
        assert FV.nrFieldsWithValues(fields) == SudokuConstants.BOARDSIZE
        assert FV.IsCompleteValues(fields) == True
        assert FV.IsValidValues(fields) == False
    def test_full_values_invalid2(self):
        fields = self._initFields(SudokuConstants.BOARDSIZE)
        FV = FieldsValidator()
        for i in range(SudokuConstants.BOARDSIZE):
            fields.fields[i].value = i+1
        fields.fields[3].value = 1
        assert FV.nrFieldsWithValues(fields) == SudokuConstants.BOARDSIZE
        assert FV.IsCompleteValues(fields) == True
        assert FV.IsValidValues(fields) == False
    def test_some_values_valid(self):
        fields = self._initFields(SudokuConstants.BOARDSIZE)
        FV = FieldsValidator()
        for i in range(SudokuConstants.BOARDSIZE):
            fields.fields[i].value = i+1
        fields.fields[3].value = SudokuConstants.INITIAL
        assert FV.nrFieldsWithValues(fields) == SudokuConstants.BOARDSIZE-1
        assert FV.IsCompleteValues(fields) == False
        assert FV.IsValidValues(fields) == True
    def test_some_values_invalid(self):
        fields = self._initFields(SudokuConstants.BOARDSIZE)
        FV = FieldsValidator()
        for i in range(SudokuConstants.BOARDSIZE):
            fields.fields[i].value = i+1
        fields.fields[3].value = SudokuConstants.INITIAL
        fields.fields[6].value = fields.fields[4].value
        assert FV.nrFieldsWithValues(fields) == SudokuConstants.BOARDSIZE-1
        assert FV.IsCompleteValues(fields) == False
        assert FV.IsValidValues(fields) == False
    def test_block_some_values_invalid(self):
        fields = self._initFields(SudokuConstants.BLOCKSIZE)
        FV = FieldsValidator()
        fields.fields[3].value = 2
        fields.fields[6].value = 2
        assert FV.nrFieldsWithValues(fields) == 2
        assert FV.IsCompleteValues(fields) == False
        assert FV.IsValidValues(fields) == False

class TestBoardsValidator:
    def test_initial(self):
        board = Board()
        BV = BoardValidator()
        assert BV.nrFieldsWithValues(board) == 0
        assert BV.IsCompleteValues(board) == False
        assert BV.IsValidValues(board) == True
    def test_complete_valid_board(self):
        board = BoardImporterFromArray([
                            "178 236 495", 
                            "359 174 268", 
                            "264 598 713",
                            "745 612 389", 
                            "813 459 627", 
                            "926 783 154", 
                            "481 325 976", 
                            "532 967 841", 
                            "697 841 532"]).board
        BV = BoardValidator()
        assert BV.nrFieldsWithValues(board) == SudokuConstants.BOARDSIZE * SudokuConstants.BOARDSIZE
        assert BV.IsCompleteValues(board) == True
        assert BV.IsValidValues(board) == True
    def test_complete_invalid_board(self):
        board = BoardImporterFromArray([
                            "178 236 495", 
                            "359 174 268", 
                            "264 598 713",
                            "745 612 389", 
                            "813 457 627", 
                            "926 783 154", 
                            "481 325 976", 
                            "532 967 841", 
                            "697 841 532"]).board
        BV = BoardValidator()
        assert BV.nrFieldsWithValues(board) == SudokuConstants.BOARDSIZE * SudokuConstants.BOARDSIZE
        assert BV.IsCompleteValues(board) == True
        assert BV.IsValidValues(board) == False
    def test_incomplete_valid_board(self):
        board = BoardImporterFromArray([
                            "178 236 495", 
                            "359 174 268", 
                            "264 598 713",
                            "745 612 389", 
                            "813 450 627", 
                            "926 783 154", 
                            "481 325 976", 
                            "532 967 841", 
                            "697 841 532"]).board
        BV = BoardValidator()
        assert BV.nrFieldsWithValues(board) == SudokuConstants.BOARDSIZE * SudokuConstants.BOARDSIZE-1
        assert BV.IsCompleteValues(board) == False
        assert BV.IsValidValues(board) == True
    def test_incomplete_valid_board2(self):
        board = BoardImporterFromArray([
                            "000 006 000",
                            "059 000 008",
                            "200 008 000",
                            "045 000 000",
                            "003 000 000",
                            "006 003 054",
                            "000 325 006",
                            "000 000 000",
                            "000 000 000"]).board
        BV = BoardValidator()
        assert BV.nrFieldsWithValues(board) == 17
        assert BV.IsCompleteValues(board) == False
        assert BV.IsValidValues(board) == True
    def test_incomplete_invalid_block(self):
        board = BoardImporterFromArray([
                            "000 006 000",
                            "059 080 000",
                            "200 008 000",
                            "045 000 000",
                            "003 000 000",
                            "006 003 054",
                            "000 325 006",
                            "000 000 000",
                            "000 000 000"]).board
        BV = BoardValidator()
        assert BV.nrFieldsWithValues(board) == 17
        assert BV.IsCompleteValues(board) == False
        assert BV.IsValidValues(board) == False
                    