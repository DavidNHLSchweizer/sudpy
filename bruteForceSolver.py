import SudokuConstants as SCS
from Validators import FieldsValidator, BoardValidator
from Board import Board
from BoardImporter import BoardImporterFromArray, BoardImporterFromFile
from BoardExporter import BoardExporterToString
import logging
from stopwatch import Stopwatch

class BruteForceSolver:
    def __init__(self):
        self._fieldsValidator = FieldsValidator()
        self.stopwatch = Stopwatch()
        self.validator = BoardValidator()

    def findBestFieldToTryNext(self, board):
        # find the open field with the minimum values possible
        result = None
        curBest = SCS.BOARDSIZE + 1
        for r in range(SCS.BOARDSIZE):
            for c in range(SCS.BOARDSIZE):
                field = board.field(r,c)
                if not SCS.IsClear(field.value):
                    continue
                n = field.nrAllowedValues()
                if n == 0:
                    return None # no solution possible in this branch
                elif n == 1: 
                    return field # no reason to search any further
                elif n < curBest:
                    curBest = n
                    result = field
        return result

    def Solve(self, board, depth)->bool:
        logging.info('call to Solve [{}] (filled: {})'.format(depth, self.validator.nrFieldsWithValues(board)))
        if self.validator.IsCompleteValues(board) and self.validator.IsValidValues(board):
            return True
        field = self.findBestFieldToTryNext(board)
        if field == None:
            logging.info('stuck...')
            return False
        values = field.GetAllowedValues()
        for v in values:            
            logging.info('field: ({},{}) possible values: {} try {}'.format(board.fieldRow(field), board.fieldCol(field), field.GetAllowedValues(), v))
            field.value = v
            if self.Solve(board, depth+1):
                return True
            else:
                logging.info('backtrack [{}]'.format(depth))
                field.value = SCS.INITIAL
        return False

    def SolveWithTiming(self, board):
        self.stopwatch.reset()
        self.stopwatch.start()
        result = self.Solve(board, 0)
        self.stopwatch.stop()  
        return result      
    
    def SolveTime(self):
        return str(self.stopwatch)
        
logging.basicConfig(filename='suko.log', filemode = 'w',level =logging.DEBUG, format='%(message)s')
filename = r'.\sudfiles\test10.txt'
board = BoardImporterFromFile(filename).board
# board = BoardImporterFromArray([
#                             "178 236 495", 
#                             "359 174 268", 
#                             "264 000 713",
#                             "745 612 389", 
#                             "813 450 627", 
#                             "926 783 154", 
#                             "001 325 900", 
#                             "532 967 841", 
#                             "697 841 532"]).board
Solver = BruteForceSolver()
print("\nsolving:\n" + BoardExporterToString().BoardAsString(board))
logging.info('\n'+BoardExporterToString().BoardAsString(board))
if Solver.SolveWithTiming(board):
    print('solved! ({})\n\n'.format(Solver.SolveTime())+BoardExporterToString().BoardAsString(board))
    logging.info('solved! ({})'.format(Solver.SolveTime()))
    logging.info('\n'+BoardExporterToString().BoardAsString(board))
else:
    logging.info('NO SOLUTION FOUND ({})'.format(Solver.SolveTime()))