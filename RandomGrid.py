import random
import SudokuConstants as SCS
from Grid import Grid
from Validators import FieldsValidator
from GridExporter import GridExporterToTextFile

class RandomGrid:
    def  __init__(self, pctfilled, isValid):
        self.grid = Grid()
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
        self.grid.clear()
        for r in range(SCS.GRIDSIZE):
            for c in range(SCS.GRIDSIZE):
                field = self.grid.square(r,c)
                value = self.GenerateFieldValue(pctfilled, field.GetAllowedValues())
                field.value = value

    def dumpFile(self, filename):
        GridExporterToTextFile().PrintBoardAsText(self.grid, filename)
    
RandomGrid(0.50, False).dumpFile("./dumping.dmp")


