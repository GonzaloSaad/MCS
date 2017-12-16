##################################
###### METODOS PARA CREACION #####
##################################

def createMatrix(rows, columns, elem=None):
    '''
    Crea una matriz de tamaño (rows x columns) y con elementos "elem"
    :param rows: cantidad de filas.
    :param columns: cantidad de columnas.
    :param elem: elemento con el que se crea la matriz. (i.e. None,0,1,etc.)
    :return: una matriz.
    '''
    return [[elem for i in range(columns)] for j in range(rows)]


def zeroes(rows, columns=None):
    '''
    Crea una matriz de tamaño (rows x columns) de elementos 0. Si
    columna es None, entonces crea una matriz cuadrada de tamaño
    (rows x rows).
    :param rows: cantidad de filas.
    :param columns: cantidad de columnas.
    :return: una matriz de ceros.
    '''
    if columns is None:
        return createMatrix(rows, rows, 0)
    else:
        return createMatrix(rows, columns, 0)


def ones(rows, columns=None):
    '''
    Crea una matriz de tamaño (rows x columns) de elementos 1. Si
    columna es None, entonces crea una matriz cuadrada de tamaño
    (rows x rows).
    :param rows: cantidad de filas.
    :param columns: cantidad de columnas.
    :return: una matriz de unos.
    '''
    if columns is None:
        return createMatrix(rows, rows, 1)
    else:
        return createMatrix(rows, columns, 1)


##################################
#### OPERACIONES DE MATRICES #####
##################################


def changeColumns(mat, col1, col2):
    '''
    Cambia una columna (col1) por otra (col2).
    :param mat: matriz para hacer el cambio.
    :param col1: numero de columna 1.
    :param col2: numero de columna 2.
    :return: void.
    '''
    rows = len(mat)
    for i in range(rows):
        mat[i][col2], mat[i][col1] = mat[i][col1], mat[i][col2]


def changeRows(mat, fil1, fil2):
    '''
    Cambia una fila (fil1) por otra (fil2).
    :param mat: matriz para hacer el cambio.
    :param fil1: numero de fila 1.
    :param fil2: numero de fila 2.
    :return: void.
    '''

    mat[fil1], mat[fil2] = mat[fil2], mat[fil1]


def column(mat, j):
    '''
    Devuelve la columna "j" de una matriz.
    :param mat: matriz para extraer la columna.
    :param j: numero de columna a extraer.
    :return: el vector columna.
    '''
    columns = len(mat)
    result = [None] * columns
    for i in range(columns):
        result[i] = mat[i][j]
    return result


def rowsElementalOperation(mat, fil1, fil2=None, num=None):
    '''
    Realiza operaciones elementales por filas a una matriz.
    Si num=None; realiza intercambio de filas.
    Si fil2=None; realiza una fila por un escalar.
    Si no; suma a una fila, otra multiplicada por un escalar.
    :param mat: matriz sobre la cual hacer la operacion.
    :param fil1: numero de la fila 1.
    :param fil2: numero de la fila 2.
    :param num: escalar.
    :return: void
    '''
    if fil2 is None and num is None:
        raise Exception("no such elemental operation.")

    if num is None:
        changeRows(mat, fil1, fil2)
        return

    if fil2 is None:
        scaleVector(mat[fil1], num)
        return

    addScaledVector(mat[fil1], mat[fil2], num)


def scaleVector(vector, scalar):
    '''
    Multiplica un vector por un escalar.
    :param vector: vector a multiplicar.
    :param scalar: escalar para multiplicar.
    :return: void.
    '''
    for i in range(len(vector)):
        vector[i] *= scalar


def addScaledVector(vector1, vector2, scalar):
    '''
    Suma un a un vector, otro multiplicado por un escalar.
    :param vector1: vector que sera modificado.
    :param vector2: vector que se suma.
    :param scalar: escalar por el que se multiplica.
    :return: void
    '''
    if len(vector1) != len(vector2):
        raise Exception("vectors must be the same size")

    N = len(vector1)
    for i in range(N):
        vector1[i] += scalar * vector2[i]


def oneOnOneElement(x, y):
    '''
    Realiza la multiplicacion uno a uno de cada elemento de dos vectores.
    :param x: un vector.
    :param y: otro vector
    :return: un vector, que tiene la multiplicacion de componentes homologos.
    '''

    if len(x) != len(y):
        raise Exception("x and y must be the same size")

    N = len(x)
    result = [None] * N

    for i in range(N):
        result[i] = x[i] * y[i]
    return result


def scalarProduct(a, b):
    '''
    Realiza el producto escalar entre dos vectores.
    :param a: un vector.
    :param b: otro vector.
    :return: el producto escalar.
    '''
    return sum(oneOnOneElement(a, b))


def copyVectorToColumn(mat, col, vec):
    '''
    Copia un vector a una columna de una matriz.
    :param mat: matriz que se modifica.
    :param col: numero de culumna que se modifica.
    :param vec: vector a copiar.
    :return: void.
    '''
    tam = len(mat)
    for i in range(tam):
        mat[i][col] = vec[i]


##################################
###### METODOS PARA STRING #######
##################################


def twoEqualedMatricesToString(T, X):
    '''
    Presenta la igualdad entre dos vectores.
    :param T: primer vector.
    :param X: segundo vector.
    :return: string resultante de la igualacion.

    e.g.:


        C1     =    -3.926
        C0     =     2.647
        C2     =    -2.338
        C3     =     5.107
        C4     =     2.488


    '''
    resultString = ""
    resultString += "\n"
    N = len(T)
    for i in range(N):
        resultString += "\n" + str(T[i]).rjust(10, " ") + " " * 5 + "=" + str(round(X[i], 3)).rjust(10, " ")
    resultString += "\n"
    return resultString


def matToString(mat, tag="M"):
    '''
    Escribe una matriz como string.
    :param mat: matriz a escribir.
    :param tag: nombre de la matriz.
    :return: string resultante.

    e.g.:


                                 A
    99.105         65.55        67.324        57.066        54.761
    44.588        91.011        56.162         1.351        31.262
    14.614        63.639        83.869        16.271        39.689
    62.517        59.312        20.988        23.107        30.081
     81.29         34.61         9.868         15.96        98.662


    '''
    resultStr = "\n"

    columns = len(mat[0])
    startSpace = ((columns // 2))
    finishSpace = columns - startSpace

    resultStr += (" " * 10 + " " * 4) * startSpace + tag + (" " * 10 + " " * 4) * finishSpace

    for row in mat:
        resultStr += "\n"
        for elemen in row:
            resultStr += str(round(elemen, 3)).rjust(10, " ") + " " * 4

    resultStr += "\n"

    return resultStr


def vectToString(vector, tag="V"):
    '''
    Escribe un vector como String.
    :param vector: vector a escribir.
    :param tag: nombre del vector.
    :return: string resultante.

    e.g.:

        B
    54.7886
    19.3093
    96.9097
    55.3931
    76.4493

    '''
    resultStr = "\n"
    resultStr += " " * 6 + tag + " " * 3
    for elem in vector:
        if isinstance(elem, str):
            text = elem.strip()
        else:
            text = str(round(elem, 4)) if not (elem is None) else "None"
        resultStr += "\n" + text.rjust(10, " ")
    resultStr += "\n"

    return resultStr


def systemToString(A, C, B, tagA="A", tagC="C", tagB="B"):
    '''
    Escribe un sistema de una matriz y dos vectores A . C = B como string.
    :param A: matriz.
    :param C: vector.
    :param B: vector.
    :param tagA: nombre de la matriz A.
    :param tagC: nombre del vector C.
    :param tagB: nombre del vector B.
    :return: string resultante.

    e.g.:

    ___________A____________|_______C______|_______B______|
          2275          91  |      C0      |         441  |
            91           6  |      C1      |          21  |


    '''


    resultStr = "\n\n"

    columns = len(A[0])
    rows = len(A)

    # Factors to set the tags.
    numberOfSpace = (6 * columns) - 1
    sizeOfATag = len(tagA)

    resultStr += ("_" * numberOfSpace) + tagA + ("_" * (numberOfSpace - sizeOfATag + 2))
    resultStr += "|__" + tagC.rjust(6, "_") + "_" * 4 + "_" * 2
    resultStr += "|__" + tagB.rjust(6, "_") + "_" * 4 + "__|"
    for i in range(rows):
        resultStr += "\n"
        for j in range(columns):
            resultStr += str(round(A[i][j], 3)).rjust(10, " ") + " " * 2
        resultStr += "|" + " " * 2 + str(C[i]).rjust(6, " ") + " " * 6
        resultStr += "|" + " " * 2 + str(round(B[i], 3)).rjust(10, " ") + " " * 2 + "|"
    resultStr += "\n\n"

    return resultStr
