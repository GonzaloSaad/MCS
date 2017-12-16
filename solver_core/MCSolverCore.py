import solver_core.operations.solverOperations as op
import solver_core.operations.matrixOperations as mt


class MCSolverCore:
    '''
    Clase encargada de manipular todas las operaciones necesarias para resolver un sistema y mostrar
    su resolucion.

    '''

    def __init__(self, x, y, functions, constants=None):

        self.__A, self.__B, self.__C, self.__F = self.__buildMatrices(x, y, functions, constants)
        self.__X = x
        self.__Y = y
        self.__solution = []
        self.__error = None
        self.__cF = None

    def __buildMatrices(self, x, y, f, C=None):
        '''
        Toma los elementos de X, los de Y, y a las funciones y arma las matrices del
        sistema A.C = B.

        :param x: vector de elementos x.
        :param y: vector de elementos y.
        :param f: vector de funciones lambda.
        :return: matrices A, C y B del sistema A.C = B.
        '''

        N = len(f)  # Numero de funciones, por ende numeros de columnas de la matriz R.
        M = len(x)  # Numero de elementos de x, por ende numero de filas de la matriz

        R = mt.zeroes(M, N)  # Se crea la matriz de resultados R, con ceros.

        for i in range(N):  # Se arma la matriz R, columna por columna.
            columna = op.applyFunctionToX(f[i], x)  # Se aplica cada funcion al vector x.
            mt.copyVectorToColumn(R, i, columna)  # Se guarda cada vector en una columna de R.

        A = mt.zeroes(N)  # Se crea la matriz A, del sistema A.C = B, con ceros.
        B = mt.zeroes(N, 1)  # Se crea la matriz B, del sistema A.C = B, con ceros.

        for i in range(N):
            B[i] = mt.scalarProduct(mt.column(R, i), y)  # Se arma el elemento i de B, con sum(fi(x).*y)
            for j in range(N):
                A[i][j] = mt.scalarProduct(mt.column(R, i), mt.column(R, j))  # Se arma el elemento ij de A.

        if C is None:  # Se crean las constantes si es que no existen.
            C = ["C" + str(e) for e in range(N)]

        return A, B, C, f

    def pivot(self, type='total'):

        '''
        Pivotea la matriz si es necesario en funcion del tipo de pivoteo.

        :param type: indica el tipo de pivoteo ("total" or "partial")
        :return: string explicativo.
        '''

        resultString = ""  ############################# --E--

        if op.needsPivote(self.__A):  # Se evalua si necesita pivoteo.


            totalPivot = True
            if type == 'partial':  # Se determina el tipo de pivoteo.
                totalPivot = False
            elif type != "total":
                raise Exception("no such type of pivot")

            if totalPivot:  # Se realiza el pivoteo.
                resultString += op.totalPivot(self.__A, self.__C, self.__B,
                                              self.__F)  ############################# --E--
            else:
                resultString += op.partialPivot(self.__A, self.__C, self.__B,
                                                self.__F)  ############################# --E--

            resultString += mt.systemToString(self.__A, self.__C, self.__B)
        else:
            resultString += "\nNo requiere Pivoteo\n"

        return resultString

    def triangulate(self):
        '''
        Triangulates the matrices.
        :return:
        '''
        resultString = ""
        resultString += op.triangulate(self.__A, self.__C, self.__B)
        return resultString

    def substitution(self):

        self.solution = op.sustitution(self.__A, self.__B)
        self.completeFunction = op.createFunction(self.solution, self.__F)
        self.error = op.calculateError(self.__X, self.__Y, self.completeFunction)

    def getA(self):
        return mt.matToString(self.__A, "A")

    def getB(self):
        return mt.vectToString(self.__B, "B")

    def getC(self):
        return mt.vectToString(self.__C, "C")

    def getSystem(self):
        return mt.systemToString(self.__A, self.__C, self.__B, "A", "C", "B")

    def getSolution(self):
        return mt.twoEqualedMatricesToString(self.__C, self.solution)

    def getSolutionVector(self):
        return self.solution

    def getError(self):
        return "\nError = \t" + str(self.error)

    def getCompleteFunction(self):
        return self.completeFunction
