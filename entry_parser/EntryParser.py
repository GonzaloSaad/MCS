import re
from entry_parser.function_parser.FunctionParser import FunctionParser

from queue import Queue


class EntryParser():
    '''
    Clase encargada de separar constantes de funciones y retornar constantes y funciones por separado.

    Se cuenta con tres fases.
    Fase 1:
        Se realiza un analisis lexico para determinar si los elementos perteneces an un alfabeto matematico.
            A) frena la ejecucion si lo ingresado no es una expresion matematica.

    Fase 2:
        Se separan los terminos.
            A) frena la ejecucion si los parentesis no estan bien emparejados.
            B) frena la ejecucion si se declaran mas de una constante por termino.

    Fase 3:
        Se evaluan las funciones.
            A) frena la ejecucion si hay un error de sintaxis.

    '''

    def __init__(self, inputString):

        self.__constants = []
        self.__stringFunctions = []
        self.__lambdaFunctions = []
        self.__determineConsAndFunc(inputString.replace(" ",""))

    def __determineConsAndFunc(self, string):

        '''
        Obtiene constantes y funciones de una expresion matematica.

        :param string: expresion matematica.
        '''

        terms = self.__splitTerms(string)

        for term in terms:
            cons, func = self.__splitFunctionsAndConstants(term)

            func = re.sub(r'\^','**',func)  # Se cambia la notacion ^ por ** aceptada por eval()

            p = FunctionParser(func)
            lambdaFunc = p.getFunction()

            self.__constants.append(cons)
            self.__stringFunctions.append(func)
            self.__lambdaFunctions.append(lambdaFunc)

    def __splitTerms(self, string):
        '''
        Separa una expresion matematica en terminos, obviando parentesis.
                Falta: trabajar los signos menos.

        :param string: expresion matematica a trabajar.
        :return: lista de terminos de la expresion.
        '''

        terms = []
        i = 0
        last = 0

        while i < len(string):
            c = string[i]
            if c == '+':  # Si se encuentra un +, se agrega desde el ultimo indice hasta el actual.
                terms.append(string[last:i])
                i += 1
                last = i
                continue

            elif c == '(':  # Si se encuentra '(' se buscara el final del parentesis.
                q = Queue()
                q.put(c)
                while not q.empty():
                    i += 1
                    c = string[i]
                    if c == '(':
                        q.put(c)
                    elif c == ')':
                        q.get()

                    if not i <= len(string):
                        raise SyntaxError("Los parentesis no estan bien emparejados.")

            i += 1
        terms.append(string[last:i])

        return terms

    def __splitFunctionsAndConstants(self, term):
        '''

        Separa funcion de constante.

        :param term: termino que sera analizado.
        :return: constante y funcion separadas.
        '''

        pat = re.finditer(r'[A-Z][0-9]*', term)  # Se busca todo lo que coincida con regex de constante de lexer.
        matches = [(m.start(), m.end()) for m in pat]  # Se guarda inicio y fin de cada uno.

        if len(matches) == 0:  # Se evalua que solo haya una constante.
            raise SyntaxError('No se declararon constantes.')
        elif len(matches) > 1:
            raise SyntaxError('No se puede declarar mas de una constante por termino.')

        start, stop = matches[0]  # Se obtiene inicio y fin por separado.

        cons = term[start:stop]  # Se extrae la constante.

        func = term[0:start] + term[stop:]  # Se arma el string de la funcion.

        if len(func) == 0:  # Si el largo es cero, la funcion es constante 1.
            func = '1'
        elif start == 0:  # Si el inicio es 0, se extrae el * del inicio.
            func = func[1:]
        elif stop == len(term):  # Si el final es el largo del string, se extrae el * del final.
            func = func[:-1]
        else:  # Como no estuvo ni al inicio ni al fin, se combinan los ** por un solo *.
            func = re.sub(r'\*\*', '*', func)

        return cons, func

    def getStringFunctions(self):
        return self.__stringFunctions

    def getConstants(self):
        return self.__constants

    def getLambdaFunctions(self):
        return self.__lambdaFunctions



