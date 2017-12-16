from entry_parser.function_parser.functions import *


class FunctionParser():
    '''
    Clase para parseo de strings que contienen funciones.
    El objetivo de esta clase es crear una funcion lambda
    en base a un string.
    '''

    def __init__(self, inputString):
        '''
        Constructor.
        Define el atributo 'inputString' para almacenar la funcion entrante.
        :param inputString: string que contiene la expresion de la funcion.
        '''

        self.__f = self.__convertToFunction(inputString)

    def __convertToFunction(self, inputString):
        '''
        Metodo privado que realiza la conversion del string.

        :param inputString: string de la funcion.
        :return: la funcion que define el string.
        :raise SyntaxError: si el string de entrada no esta bien escrito.
        '''

        # Se realiza la ccnversion.
        # Se utiliza eval(), quien es que tirara la excepcion si no esta bien escrita.

        return lambda x: eval(inputString)

    def getFunction(self):
        return self.__f
