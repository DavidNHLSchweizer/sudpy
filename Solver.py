from __future__ import annotations
from abc import ABC, abstractmethod
import SudokuConstants as SCS
from Grid import Grid
from stopwatch import Stopwatch

class SolveStrategy(ABC):
    @abstractmethod
    def Solve(self, grid: Grid)->bool:
        pass
    

class Solver:
    def __init__(self):
        self.stopwatch = Stopwatch()

    def SolveTime(self):
        return str(self.stopwatch)

    def NotEnoughFilledSquaresToSolve(self, grid: Grid):
        return grid.nrSquaresWithValues() < SCS.MINIMUMFILLEDSQUARES

    def Solve(self, grid: Grid, strategy: SolveStrategy)->bool:
        if self.NotEnoughFilledSquaresToSolve(grid):
            return False
        self.stopwatch.reset()
        self.stopwatch.start()        
        return strategy.Solve(grid)
        self.stopwatch.stop()  
