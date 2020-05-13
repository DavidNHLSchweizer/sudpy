import SudokuConstants

class BoardExporter:
    def _getLineFromBoard(self, board, row):
        line = ''
        for col in range(SudokuConstants.BOARDSIZE):
            field = board.field(row,col)
            line = line + ('0' if field.value == SudokuConstants.INITIAL else str(field.value))
            if col % 3 == 2:
                line = line + ' '
        return line
        
    def dumpFile(self, board, filename, mode = "w"):
        with(open(filename, mode)) as fileHandler:
            for row in range(SudokuConstants.BOARDSIZE):            
                line = self._getLineFromBoard(board, row)
                if line:
                    fileHandler.write(line+'\n')
            fileHandler.write('\n')
