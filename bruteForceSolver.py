import SudokuConstants
from Fields import FieldsValidator
from Board import Board, BoardValidator
from BoardImporter import BoardImporter, BoardDumper
import logging

NOROWFOUND = -1
class BruteForceSolver:
    def __init__(self):
        self.boardDumper = BoardDumper()
    def findBestRowToDoRecursion(self, board):
        result = NOROWFOUND
        curBest = SudokuConstants.BOARDSIZE+1
        for r in range(SudokuConstants.BOARDSIZE):
            n = FieldsValidator(board.Row(r)).nrFieldValues()
            if n > 0 and n < curBest:
                curBest = n
                result = r        
        return result
    def Solve(self, board, depth)->bool:
        BV = BoardValidator(board)
        logging.info('call to Solve {} (filled: {})'.format(depth, BV.nrFilledValues()))
        self.boardDumper.dumpFile(board, "boards.log", "a")
        if BV.IsCompleteValues():
            return True
        r = self.findBestRowToDoRecursion(board)
        if r == NOROWFOUND:
            return False
        logging.debug('ROW '+str(r))
        for c in range(SudokuConstants.BOARDSIZE):
            field = board.field(r, c)
            logging.debug('col '+str(c))
            if field.value == SudokuConstants.INITIAL:
                values = field.GetAllowedValues()
                for v in values:
                    logging.debug('value '+str(v))
                    field.value = v
                    if self.Solve(board, depth+1):
                        return True
                    logging.info('backtrack ({} {}) - {}'.format(r,c,v))
                    field.value = SudokuConstants.INITIAL
        return False

logging.basicConfig(filename='suko.log', level =logging.DEBUG)
filename = r'.\sudfiles\TEST5.txt'
I = BoardImporter(filename)

Solver = BruteForceSolver()
if Solver.Solve(I.board, 0):
    logging.info('solved!')
    B = BoardDumper()
    B.dumpFile(I.board, filename + '.exp')
else:
    logging.info('no solve')