import SudokuConstants as SCS
from Validators import FieldsValidator, GridValidator
from Grid import Grid
from GridImporter import GridImporterFromArray, GridImporterFromFile
from GridExporter import GridExporterToString
from Reporter import Reporter, SimpleReporter

class BruteForceSolver:
    def __init__(self):
        self._squaresValidator = FieldsValidator()
        self.validator = GridValidator()
        self.nPass = 0

    def findBestFieldToTryNext(self, grid):
        # find the open square with the minimum values possible
        result = None
        curBest = SCS.GRIDSIZE + 1
        for r in range(SCS.GRIDSIZE):
            for c in range(SCS.GRIDSIZE):
                square = grid.square(r,c)
                if not SCS.IsClear(square.value):
                    continue
                n = square.nrAllowedValues()
                if n == 0:
                    return None # no solution possible in this branch
                elif n == 1: 
                    return square # no reason to search any further
                elif n < curBest:
                    curBest = n
                    result = square
        return result

    def Solve(self, grid, depth, reporter=Reporter())->bool:
        self.nPass += 1
        reporter.Report(Reporter.ReportType.STARTSOLVE, nPass=self.nPass, depth=depth, filled=self.validator.nrFieldsWithValues(grid))
        if self.validator.IsCompleteValues(grid) and self.validator.IsValidValues(grid):
            return True
        square = self.findBestFieldToTryNext(grid)
        if square == None:
            reporter.Report(Reporter.ReportType.STUCK)
            return False
        values = square.GetAllowedValues()
        for v in values:            
            reporter.Report(Reporter.ReportType.NEWVALUE, row=grid.squareRow(square), col=grid.squareCol(square), 
                                         values=square.GetAllowedValues(), value=v)
            square.value = v
            if self.Solve(grid, depth+1, reporter):
                return True
            else:
                reporter.Report(Reporter.ReportType.BACKTRACK, depth=depth)
                square.value = SCS.INITIAL
        return False

    def SolveWithTiming(self, grid, reporter = Reporter()):
        reporter.Start(grid)
        result = self.Solve(grid, 0, reporter)
        reporter.Stop(grid, result)
        return result      
    
def SolveFile(filename, logfilename):
    BruteForceSolver().SolveWithTiming(GridImporterFromFile(filename).grid, SimpleReporter(logfilename))

