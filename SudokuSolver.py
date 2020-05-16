from bruteForceSolver import SolveFile
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sudoku Solver')
    parser.add_argument('-file', required=True, help='the sudoku file to solve')
    parser.add_argument('-log', default = 'sudoku.solver.log', help='the logfile')
    args = parser.parse_args()
    SolveFile(args.file, args.log)