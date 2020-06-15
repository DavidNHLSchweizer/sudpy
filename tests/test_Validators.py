import SudokuConstants as SCS
from Square import Square
from Squares import Squares
from Grid import Grid
from Validators import SquaresValidator, GridValidator
from GridImporter import GridImporterFromArray

class TestSquaresValidator:
    def _initSquares(self, nCols):
        squares = Squares()
        for _ in range(SCS.GRIDSIZE):
            squares.addSquare(Square())
        squares.nCols = nCols        
        return squares

    def test_initial(self):
        squares = self._initSquares(SCS.GRIDSIZE)
        SqV = SquaresValidator()
        assert SqV.nrSquaresWithValues(squares) == 0
        assert SqV.IsCompleteValues(squares) == False
        assert SqV.IsValidValues(squares) == True
    def test_one_value(self):
        squares = self._initSquares(SCS.GRIDSIZE)
        SqV = SquaresValidator()
        square = squares.squares[0]
        square.value = 1
        assert SqV.nrSquaresWithValues(squares) == 1
        assert SqV.IsCompleteValues(squares) == False
        assert SqV.IsValidValues(squares) == True
    def test_two_values_valid(self):
        squares = self._initSquares(SCS.GRIDSIZE)
        SqV = SquaresValidator()
        squares.squares[0].value = 1
        squares.squares[SCS.GRIDSIZE-1].value = 2
        assert SqV.nrSquaresWithValues(squares) == 2
        assert SqV.IsCompleteValues(squares) == False
        assert SqV.IsValidValues(squares) == True
    def test_two_values_invalid(self):
        squares = self._initSquares(SCS.GRIDSIZE)
        SqV = SquaresValidator()
        squares.squares[0].value = 1
        squares.squares[SCS.GRIDSIZE-1].value = 1
        assert SqV.nrSquaresWithValues(squares) == 2
        assert SqV.IsCompleteValues(squares) == False
        assert SqV.IsValidValues(squares) == False
    def test_full_values_valid(self):
        squares = self._initSquares(SCS.GRIDSIZE)
        SqV = SquaresValidator()
        for i in range(SCS.GRIDSIZE):
            squares.squares[i].value = i+1
        assert SqV.nrSquaresWithValues(squares) == SCS.GRIDSIZE
        assert SqV.IsCompleteValues(squares) == True
        assert SqV.IsValidValues(squares) == True
    def test_full_values_invalid(self):
        squares = self._initSquares(SCS.GRIDSIZE)
        SqV = SquaresValidator()
        for i in range(SCS.GRIDSIZE):
            squares.squares[i].value = 3
        assert SqV.nrSquaresWithValues(squares) == SCS.GRIDSIZE
        assert SqV.IsCompleteValues(squares) == True
        assert SqV.IsValidValues(squares) == False
    def test_full_values_invalid2(self):
        squares = self._initSquares(SCS.GRIDSIZE)
        SqV = SquaresValidator()
        for i in range(SCS.GRIDSIZE):
            squares.squares[i].value = i+1
        squares.squares[3].value = 1
        assert SqV.nrSquaresWithValues(squares) == SCS.GRIDSIZE
        assert SqV.IsCompleteValues(squares) == True
        assert SqV.IsValidValues(squares) == False
    def test_some_values_valid(self):
        squares = self._initSquares(SCS.GRIDSIZE)
        SqV = SquaresValidator()
        for i in range(SCS.GRIDSIZE):
            squares.squares[i].value = i+1
        squares.squares[3].value = SCS.INITIAL
        assert SqV.nrSquaresWithValues(squares) == SCS.GRIDSIZE-1
        assert SqV.IsCompleteValues(squares) == False
        assert SqV.IsValidValues(squares) == True
    def test_some_values_invalid(self):
        squares = self._initSquares(SCS.GRIDSIZE)
        SqV = SquaresValidator()
        for i in range(SCS.GRIDSIZE):
            squares.squares[i].value = i+1
        squares.squares[3].value = SCS.INITIAL
        squares.squares[6].value = squares.squares[4].value
        assert SqV.nrSquaresWithValues(squares) == SCS.GRIDSIZE-1
        assert SqV.IsCompleteValues(squares) == False
        assert SqV.IsValidValues(squares) == False
    def test_block_some_values_invalid(self):
        squares = self._initSquares(SCS.BLOCKSIZE)
        SqV = SquaresValidator()
        squares.squares[3].value = 2
        squares.squares[6].value = 2
        assert SqV.nrSquaresWithValues(squares) == 2
        assert SqV.IsCompleteValues(squares) == False
        assert SqV.IsValidValues(squares) == False

class TestGridsValidator:
    def test_initial(self):
        grid = Grid()
        GV = GridValidator()
        assert GV.nrSquaresWithValues(grid) == 0
        assert GV.IsCompleteValues(grid) == False
        assert GV.IsValidValues(grid) == True
    def test_complete_valid_grid(self):
        grid = GridImporterFromArray([
                            "178 236 495", 
                            "359 174 268", 
                            "264 598 713",
                            "745 612 389", 
                            "813 459 627", 
                            "926 783 154", 
                            "481 325 976", 
                            "532 967 841", 
                            "697 841 532"]).grid
        GV = GridValidator()
        assert GV.nrSquaresWithValues(grid) == SCS.GRIDSIZE * SCS.GRIDSIZE
        assert GV.IsCompleteValues(grid) == True
        assert GV.IsValidValues(grid) == True
    def test_complete_invalid_grid(self):
        grid = GridImporterFromArray([
                            "178 236 495", 
                            "359 174 268", 
                            "264 598 713",
                            "745 612 389", 
                            "813 457 627", 
                            "926 783 154", 
                            "481 325 976", 
                            "532 967 841", 
                            "697 841 532"]).grid
        GV = GridValidator()
        assert GV.nrSquaresWithValues(grid) == SCS.GRIDSIZE * SCS.GRIDSIZE
        assert GV.IsCompleteValues(grid) == True
        assert GV.IsValidValues(grid) == False
    def test_incomplete_valid_grid(self):
        grid = GridImporterFromArray([
                            "178 236 495", 
                            "359 174 268", 
                            "264 598 713",
                            "745 612 389", 
                            "813 450 627", 
                            "926 783 154", 
                            "481 325 976", 
                            "532 967 841", 
                            "697 841 532"]).grid
        GV = GridValidator()
        assert GV.nrSquaresWithValues(grid) == SCS.GRIDSIZE * SCS.GRIDSIZE-1
        assert GV.IsCompleteValues(grid) == False
        assert GV.IsValidValues(grid) == True
    def test_incomplete_valid_grid2(self):
        grid = GridImporterFromArray([
                            "000 006 000",
                            "059 000 008",
                            "200 008 000",
                            "045 000 000",
                            "003 000 000",
                            "006 003 054",
                            "000 325 006",
                            "000 000 000",
                            "000 000 000"]).grid
        GV = GridValidator()
        assert GV.nrSquaresWithValues(grid) == 17
        assert GV.IsCompleteValues(grid) == False
        assert GV.IsValidValues(grid) == True
    def test_incomplete_invalid_block(self):
        grid = GridImporterFromArray([
                            "000 006 000",
                            "059 080 000",
                            "200 008 000",
                            "045 000 000",
                            "003 000 000",
                            "006 003 054",
                            "000 325 006",
                            "000 000 000",
                            "000 000 000"]).grid
        GV = GridValidator()
        assert GV.nrSquaresWithValues(grid) == 17
        assert GV.IsCompleteValues(grid) == False
        assert GV.IsValidValues(grid) == False
                    