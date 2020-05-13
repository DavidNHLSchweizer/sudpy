import random
import SudokuConstants
from Board import Board, BoardValidator
from Fields import FieldsValidator
from BoardImporter import BoardDumper

class RandomBoard:
    def  __init__(self, pctfilled, isValid):
        self.board = Board()
        self.Generate(pctfilled, isValid)
    
    def GenerateFieldValue(self, pctfilled, allowedValues):
        if len(allowedValues) == 0:
            return SudokuConstants.INITIAL
        if random.random() > pctfilled:
            return SudokuConstants.INITIAL
        Try = 0
        while True:
            value = 1 + random.randrange(SudokuConstants.BOARDSIZE)
            if value in allowedValues:
                return value
            elif Try > 42:
                return SudokuConstants.INITIAL
            else:
                Try +=1

    def Generate(self, pctfilled, isValid):
        self.board.clear()
        for r in range(SudokuConstants.BOARDSIZE):
            for c in range(SudokuConstants.BOARDSIZE):
                field = self.board.field(r,c)
                value = self.GenerateFieldValue(pctfilled, field.GetAllowedValues())
                field.value = value

    def dumpFile(self, filename):
        bd = BoardDumper()
        bd.dumpFile(self.board, filename)
    
RB = RandomBoard(0.50, False)
RB.dumpFile("./dumping.dmp")
BV = BoardValidator(RB.board)
print()


