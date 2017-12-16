
from solver_core.MCSolverCore import MCSolverCore
from entry_parser.EntryParser import EntryParser


class MCSolverPres:
    '''
    Clase encargada de manejar la logica de la resolucion.

    '''

    def __init__(self, x, y, function):
        parser = EntryParser(function)
        self.functions = parser.getLambdaFunctions()
        self.constants = parser.getConstants()
        self.x = x
        self.y = y
        self.solution = []
        self.completeFunction=None

    def solve(self):
        explanation = "\n________________________SOLUCION________________________\n"

        selSolver = MCSolverCore(self.x, self.y, self.functions, self.constants)

        explanation += "\n----------------------- MATRICES -----------------------\n"

        explanation += selSolver.getSystem()

        explanation += "\n----------------------- PIVOTEO  -----------------------\n"

        explanation += selSolver.pivot("total")

        explanation += "\n--------------------- TRIANGULACION --------------------\n"

        explanation += selSolver.triangulate()

        explanation += "\n---------------------- SUSTITUCION ---------------------\n"

        selSolver.substitution()
        explanation += selSolver.getSolution()
        explanation += selSolver.getError()

        self.solution=selSolver.getSolutionVector()
        self.completeFunction = selSolver.getCompleteFunction()
        return explanation

    def getCompleteFunction(self):
        return self.completeFunction


