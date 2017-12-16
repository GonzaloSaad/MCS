import solver_core.operations.matrixOperations as mt


def applyFunctionToX(f, x):
    '''
    Aplica una funcion "f" a un vector de valores "x".
    :param f: una function.
    :param x: un vector de valores.
    :return: un vector que es "x" con la function "f" aplicada.
    '''

    result = None
    if isinstance(x, list):

        N = len(x)
        result = [None] * N

        for i in range(len(x)):
            result[i] = f(x[i])
    else:
        result = f(x)

    return result


def getIndexOfMaximumOfVector(x):
    '''
    Busca el indice del maximo de un vector.
    :param x: vector a buscar el maximo.
    :return: indice del maximo.
    '''

    maximum, index = 0, 0
    N = len(x)

    for i in range(N):
        if x[i] > maximum:
            maximum = x[i]
            index = i

    return index


def getIndexOfMaximumInMatrix(x):
    '''
    Busca el indice del maximo de una matriz.
    :param x: matriz a buscar el maximo.
    :return: indice del maximo [fila,columna].
    '''

    maximum, imax, jmax = 0, 0, 0
    column = len(x[0])
    rows = len(x)

    for i in range(rows):
        for j in range(column):
            if x[i][j] > maximum:
                maximum = x[i][j]
                imax, jmax = i, j
    return imax, jmax


def needsPivote(x):
    '''
    Analiza si una matriz requiere pivoteo.
    :param x: matriz a analizar.
    :return: true si requiere, false si no.
    '''
    i, j = getIndexOfMaximumInMatrix(x)

    return not ((i == 0) and (i == j))


def partialPivot(A, C, B, F):
    '''
    Pivotea parcialmente una matriz A.
    Acomoda tambien el sistema A . C = B acorde a ello.
    :param A: matriz del sistema A . C = B.
    :param C: vector del sistema A . C = B.
    :param B: vector del sistema A . C = B.
    :param F: vector de functiones del sistema A . C = B.
    :return: string explicativo de los pasos para resolver.
    '''

    resultString = ""  ############################# --E--
    resultString += "\nPivoteo parcial "  ############################# --E--

    # Determinar si se pivoteara filas o se pivoteara columnas
    maximumOfColumn = max(A[:][0])
    maximumOfRow = max(mt.column(A, 0))

    rowPivot = True
    if maximumOfColumn > maximumOfRow:
        rowPivot = False

    # Pivotear segun sea por columna o por fila.
    if rowPivot:
        # Pivoteo por fila.
        # Obtener el indice del maximo.
        indexOfMax = getIndexOfMaximumOfVector(mt.column(A, 0))
        resultString += "por filas."  ############################# --E--
        resultString += "\nSe tiene el maximo en (" + str(indexOfMax + 1) + ",1)."  ############################# --E--
        resultString += "\nSe cambia fila 1 por fila " + str(
            indexOfMax + 1) + ", en A."  ############################# --E--
        resultString += "\nSe cambia elemento 1 por elemento " + str(
            indexOfMax + 1) + ", en B."  ############################# --E--

        # Intercambiar filas en A.
        A[0], A[indexOfMax] = A[indexOfMax], A[0]

        # Intercambiar elementos en B.
        B[0], B[indexOfMax] = B[indexOfMax], B[0]


    else:
        # Pivoteo por columna.
        # Obtener el indice del maximo.

        indexOfMax = getIndexOfMaximumOfVector(A[0][:])
        resultString += "por columnas."  ############################# --E--

        resultString += "\nSe tiene el maximo en (1," + str(indexOfMax + 1) + ")."  ############################# --E--

        resultString += "\nSe cambia columna 1 por columna " + str(
            indexOfMax + 1) + ", en A."  ############################# --E--

        resultString += "\nSe cambia elemento 1 por elemento " + str(
            indexOfMax + 1) + ", en C."  ############################# --E--

        # Intercambiar columnas en A.
        mt.changeColumns(A, 0, indexOfMax)

        # Intercambiar elementos en C y F.
        C[0], C[indexOfMax] = C[indexOfMax], C[0]
        F[0], F[indexOfMax] = F[indexOfMax], F[0]

    return resultString


def totalPivot(A, C, B, F):
    '''
    Pivotea totalmente una matriz A.
    Acomoda tambien el sistema A . C = B acorde a ello.
    :param A: matriz del sistema A . C = B.
    :param C: vector del sistema A . C = B.
    :param B: vector del sistema A . C = B.
    :param F: vector de functiones del sistema A . C = B.
    :return: string explicativo de los pasos para resolver.
    '''

    imax, jmax = getIndexOfMaximumInMatrix(A)

    resultString = ""  ############################# --E--

    resultString += "\nPivoteo total."  ############################# --E--

    resultString += "\nMaximo en (" + str(imax+1) + "," + str(jmax+1) + ")."  ############################# --E--

    resultString += "\nSe intercambia fila 1 por fila " + str(imax+1) + ", en A."  ############################# --E--

    resultString += "\nSe intercambia elemento 1 por elemento " + str(
        imax + 1) + ", en B."  ############################# --E--

    resultString += "\nse intercambia columna 1 por columna " + str(
        jmax+1) + ", en A."  ############################# --E--

    resultString += "\nSe intercambia elemento 1 por elemento" + str(
        jmax+1) + ", en C."  ############################# --E--

    # Intercambiar filas en A.
    A[0], A[imax] = A[imax], A[0]

    # Intercambiar columnas en A.
    mt.changeColumns(A, 0, jmax)

    # Intercambiar elementos en B.
    B[0], B[imax] = B[imax], B[0]

    # Intercambiar elementos en C.
    C[0], C[jmax] = C[jmax], C[0]
    F[0], F[jmax] = F[jmax], F[0]

    return resultString


def triangulate(A, C, B):
    '''
    Triangula una matriz A.
    Acomoda tambien el sistema A . C = B acorde a ello.
    :param A: matriz del sistema A . C = B.
    :param C: vector del sistema A . C = B.
    :param B: vector del sistema A . C = B.
    :return: string explicativo.
    '''

    resultString = ""  ############################# --E--

    N = len(A)

    for k in range(N - 1):
        resultString += "\n\nVuelta " + str(k+1) + ". Columna " + str(k+1) + "."  ############################# --E--

        for i in range(k + 1, N):

            # calcular m.
            m = -(A[i][k] / A[k][k])

            resultString += "\n\n\tFila " + str(i+1) + ". Coeficiente m = " + str(m)  ############################# --E--

            # modificar B.
            B[i] += B[k] * m

            # modificar A.
            mt.addScaledVector(A[i], A[k], m)

            resultString += mt.systemToString(A, C, B)  ############################# --E--

        resultString += "\n\t %% Fin Triangulacion %% \n\n "  ############################# --E--
    return resultString


def sustitution(A, B):
    '''
    Realiza la sustitucion en el sistema A . C = B, para calcular
    el vector C.
    :param A: matriz del sistema A . C = B.
    :param B: vector del sistema A . C = B.
    :return: vector de valores de C.
    '''

    N = len(A)
    result = [0] * N

    for i in range(1, N + 1):
        sum = 0
        for j in range(1, N):
            sum += A[N - i][N - j] * result[N - j]
        result[N - i] = (B[N - i] - sum) / A[N - i][N - i]
    return result


def calculateError(x, y, f):
    '''
    Calcula el error de la funcion "f" segun minimos cuadrados.
    :param x: vector de valores x.
    :param y: vector de valores y.
    :param f: function aproximada.
    :return: valor del error.
    '''


    error = 0
    tam = len(x)

    for i in range(tam):
        error += (y[i] - f(x[i])) ** 2

    return error


def createFunction(C, F):
    '''
    Toma un vector de functiones y un vector de constantes y los combina.
    :param C: vector de constantes.
    :param F: vector de functiones.
    :return: function lambda compelta.
    '''
    if len(C) == 1:
        return lambda x: C[0] * F[0](x)
    else:
        return lambda x: (C[0] * F[0](x) + createFunction(C[1:], F[1:])(x))
