from entry_parser.lexical_analyzer.Lexer import Lexer  # Se importa la clase Lexer, que tiene el nucleo de un Analizador Lexico.
from entry_parser.lexical_analyzer.Lexeme import Lexeme  # Se importa la clase Lexeme, que tiene la logica de un lexema.


class FunctionLexer():
    '''
    Clase que realiza el analisis lexico de una expresion matematica.
    Originalmente la clase es iterable, ya que en el metodo tokenize() retorna los tokens que se encuentran.
    Usa la clase Lexer.
    '''

    def __init__(self, inputString, variable='x', *args):
        '''
        Contructor de la clase.

        :param inputString: string que representa la funcion.
        :param variable: string que indica cual es la variable a usar.
        :param args: arreglo que contiene el resto de las variables si hubiere.
        '''

        self.__lexer = Lexer(inputString.replace(" ",""))  # Se intancia la clase Lexer.
        self.__defineLexemes()  # Se defiene los lexemeas que no son de variables.
        self.__defineVariablesLexemes(variable, args)  # Se definen los lexemas de variables.

    def __defineLexemes(self):
        '''
        Ordena la invocacion de los distintos lexemas.
        '''

        self.__setSimpleLexemes()  # Lexemas de largo 1.
        self.__setDualLexemes()  # Lexemas de largo 2.
        self.__setTriLexemes()  # Lexemas de largo 3.
        self.__setMultipleLexemes()  # Lexemas de largo multiple.

    def tokenizeOK(self):
        '''
        Realiza la busqueda de tokens dentro del string.
        El metodo original devuelve los tokens con yield permitiendo iterar, pero esta version no retorna nada,
        simplemente levanta una excepcion si lo que se encuentra no esta dentro de los lexemas definidos.

        :return None si la expresion fue reconocida o el simbolo no reconocido.
        '''

        return self.__lexer.tokenizeOK()  # Delega el metodo al objeto de la clase Lexer.

    def __defineVariablesLexemes(self, first, vars):
        '''
        Crea y agrega los lexemas que pertenecen a variables.

        :param first: variable obligatoria minima.
        :param vars: otras variables que pueden ser definidas.
        '''

        lexemes = [Lexeme('VAR', r'' + first)]  # Se crea una lista con el lexema de la variable obligatoria.

        for i in range(len(vars)):
            lexemes.append(Lexeme('VAR', r'' + vars[i]))  # Se crea un lexema por cada vairable adicional y se lo agrega
        self.__lexer.addLexemes(lexemes)  # Se agrega todos los lexemas creados al lexer.

    def __setSimpleLexemes(self):
        '''
        Crea y agrega los lexemas de largo 1.
        '''

        lexemes = [

            Lexeme('OP', r'\+'),
            Lexeme('OP', r'-'),
            Lexeme('OP', r'\*'),
            Lexeme('OP', r'/'),
            Lexeme('OP', r'\^'),
            Lexeme('LPAREN', r'\('),
            Lexeme('RPAREN', r'\)'),

            Lexeme('CONSTANT', r'e')

        ]  # Se crean los lexemas.


        #Saco este lexema para probar coeficientes con numeros; Lexeme('COEFF', r'[A-Z]'),

        self.__lexer.addLexemes(lexemes)  # Se los agrega.

    def __setDualLexemes(self):
        '''
        Crea y agrega los lexemas de largo 2.
        '''

        lexemes = [
            Lexeme("FUNCTION", r'ln'),
            Lexeme("FUNCTION", r'tg'),
            Lexeme("CONSTANT", r'pi')
        ]  # Se crean los lexemas.
        self.__lexer.addLexemes(lexemes)  # Se agregan los lexemas.

    def __setTriLexemes(self):
        '''
        Se crean y agregan los lexemas de largo 3.
        '''

        lexemes = [
            Lexeme("FUNCTION", r'sin'),
            Lexeme("FUNCTION", r'cos'),
            Lexeme("FUNCTION", r'log')
        ]  # Se crean los lexemas.
        self.__lexer.addLexemes(lexemes)  # Se agregan.

    def __setMultipleLexemes(self):
        lexemes = [
            Lexeme('NUMBER', r'[0-9]+(?!.)'),
            Lexeme('NUMBER',r'\.[0-9]*(?!.)'),
            Lexeme('COEFF',r'[A-Z][0-9]*')
        ]  # Se crean los lexemas.
        self.__lexer.addLexemes(lexemes)  # Se los agrega.

    def __str__(self):
        '''
        Se redefine el metodo de string, para que refleje el estado del lexer.
        :return: un string representantivo de la clase.
        '''
        return self.__lexer.__str__()




