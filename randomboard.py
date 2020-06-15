import random
import SudokuConstants as SCS
from Board import Board
from Validators import FieldsValidator
from BoardExporter import BoardExporterToTextFile

class RandomBoard:
    def  __init__(self, pctfilled, isValid):
        self.board = Board()
        self.Generate(pctfilled, isValid)
    
    def GenerateFieldValue(self, pctfilled, allowedValues):
        if len(allowedValues) == 0:
            return SCS.INITIAL
        if random.random() > pctfilled:
            return SCS.INITIAL
        Try = 0
        while True:
            value = 1 + random.randrange(SCS.GRIDSIZE)
            if value in allowedValues:
                return value
            elif Try > 42:
                return SCS.INITIAL
            else:
                Try +=1

    def Generate(self, pctfilled, isValid):
        self.board.clear()
        for r in range(SCS.GRIDSIZE):
            for c in range(SCS.GRIDSIZE):
                field = self.board.square(r,c)
                value = self.GenerateFieldValue(pctfilled, field.GetAllowedValues())
                field.value = value

    def dumpFile(self, filename):
        bd = BoardExporterToTextFile()
        bd.PrintBoardAsText(self.board, filename)
    
RB = RandomBoard(0.50, False)
RB.dumpFile("./dumping.dmp")


