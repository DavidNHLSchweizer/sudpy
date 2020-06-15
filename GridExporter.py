import SudokuConstants as SCS

class GridExporter:
    def _getLineFromGrid(self, grid, row):
        line = ''
        for col in range(SCS.GRIDSIZE):
            square = grid.square(row,col)
            line = line + ('0' if square.value == SCS.INITIAL else str(square.value))
            if col % 3 == 2:
                line = line + ' '
        return line

class GridExporterToTextFile(GridExporter):
    def PrintGridAsText(self, grid, filename, mode = "w"):
        with(open(filename, mode)) as fileHandler:
            for row in range(SCS.GRIDSIZE):            
                line = self._getLineFromGrid(grid, row)
                if line:
                    fileHandler.write(line+'\n')
            fileHandler.write('\n')

class GridExporterToString(GridExporter):
    def GridAsString(self, grid):
        result = ''
        for row in range(SCS.GRIDSIZE):            
            result = result + self._getLineFromGrid(grid, row) + '\n'
        return result
