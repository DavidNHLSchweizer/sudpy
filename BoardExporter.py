import SudokuConstants as SCS

class BoardExporter:
    def _getLineFromBoard(self, board, row):
        line = ''
        for col in range(SCS.BOARDSIZE):
            field = board.field(row,col)
            line = line + ('0' if field.value == SCS.INITIAL else str(field.value))
            if col % 3 == 2:
                line = line + ' '
        return line

class BoardExporterToTextFile(BoardExporter):
    def PrintBoardAsText(self, board, filename, mode = "w"):
        with(open(filename, mode)) as fileHandler:
            for row in range(SCS.BOARDSIZE):            
                line = self._getLineFromBoard(board, row)
                if line:
                    fileHandler.write(line+'\n')
            fileHandler.write('\n')

class BoardExporterToString(BoardExporter):
    def BoardAsString(self, board):
        result = ''
        for row in range(SCS.BOARDSIZE):            
            result = result + self._getLineFromBoard(board, row) + '\n'
        return result
