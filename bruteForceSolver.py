import SudokuConstants as SCS
from Validators import SquaresValidator, GridValidator
from Grid import Grid
from Square import Square
from GridImporter import GridImporterFromArray, GridImporterFromFile
from GridExporter import GridExporterToString
from Reporter import Reporter, SimpleReporter

class BruteForceSolver:
    def __init__(self):
        self.validator = GridValidator()
        self.nPass = 0

    def findBestSquareToTryNext(self, grid)->Square:
        # find the open square with the least values possible
        def _NoSolutionPossibleInThisBranch(n):
            return n == 0
        def _SquareHasOneAllowedValue(n):
            return n == 1
        result = None
        LeastNrAllowedValues = SCS.GRIDSIZE + 1
        for square in grid.squares:
            if not SCS.IsClear(square.value):
                continue
            n = square.nrAllowedValues()
            if _NoSolutionPossibleInThisBranch(n):
                return None 
            elif _SquareHasOneAllowedValue(n): 
                return square 
            elif n < LeastNrAllowedValues:
                LeastNrAllowedValues = n
                result = square
        return result

    def Solve(self, grid, depth, reporter=Reporter())->bool:
        self.nPass += 1
        reporter.Report(Reporter.ReportType.STARTSOLVE, nPass=self.nPass, depth=depth, filled=self.validator.nrFieldsWithValues(grid))
        if not self.validator.IsValidValues(grid):
            return False
        if self.validator.IsCompleteValues(grid):
            return True
        square = self.findBestSquareToTryNext(grid)
        if square == None:
            reporter.Report(Reporter.ReportType.STUCK)
            return False
        row, col = grid.squareRow(square), grid.squareCol(square)
        values = square.GetAllowedValues()
        for v in values:            
            reporter.Report(Reporter.ReportType.NEWVALUE, row=row, col=col, values=values, value=v)
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

