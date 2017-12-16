import re
from entry_parser.lexical_analyzer.lexer_exceptions.NoSuchSymbolException import NoSuchSymbolException
from entry_parser.lexical_analyzer.Token import Token
from entry_parser.lexical_analyzer.StringIterator import StringIterator


class Lexer():
    '''
    Clase que engloba el comportamiento y logica de un Analizador Lexico basico.
    '''

    def __init__(self, inputString):
        '''
        Contructor de la clase.

        :param inputString: string que contiene la funcion.
        '''
        self.__lexemes = []  # Se crea un arreglo que tendra por cada elemento un vector de lexemas de un largo dado.
        self.__inputString = inputString  # Se guarda el string de la funcion para iterarlo.

    def tokenizeOK(self):
        '''
        Crea un iterable de tokens del inputString.

        :return: originalment retorna el token con yield.
        '''

        chars = StringIterator(self.__inputString)  # Se crea el iterador del string.
        lexemeMatrix = self.__lexemes  # Se abrevia el nombre de la matriz de lexemas.

        while chars.hastNext():
            c = chars.getChar()  # Se obtiene el caracter actual.

            token = None  # Se inicializa el token en none para la vuelta actual.

            for i in range(1, len(lexemeMatrix)):  # Para cada largo de 1 hasta n se hace un escaneo.
                token = self.__scan(lexemeMatrix[i], i, chars)
                if token is not None:  # Si se ha encontrado un token, se frena de iterar.
                    break

            if token is None:  # Si el token todavia no se encontro, se prueba con los tokens de largo multiple.
                token = self.__scan(lexemeMatrix[0], 0, chars)

            if token is None:  # Si el token no se encontro, se retorna el simbolo no reconocido.
                return c

        return None  # Se retorna 'None' si todo simbolo fue reconocido.

    def __scan(self, lexemes, size, chars):
        '''
        Escanea un string en busqueda de un token de un largo determinado.

        :param lexemes: lista de lexemas a considerar, todos de un mismo largo.
        :param size: tamaño de los tokens.
        :param chars: iterador del string.
        :return: un token.
        '''

        if size == 0:  # Si el largo pasado por parametro es nulo, significa busqueda de largo multiple.
            return self.__scanMultiple(lexemes, chars)

        c = chars.getChar(size)  # Se obtiene los siguientes 'size' caracteres.

        ret = None  # Se inicializa el retorno en None
        if c is not None:  # Si el caracter no es nulo, se hace la busqueda.
            for lex in lexemes:  # Para cada lexema de la lista se compara.
                if re.match(lex.getPat(), c):  # Si alguno coincide, se retorna un token del lexema.
                    ret = Token(lex.getType(), c)

        if ret is not None:  # Si se encontro token, se avanza el iterador 'size' pasos.
            for i in range(0, size):
                chars.moveNext()
        return ret  # Se retorna el token o none.

    def __scanMultiple(self, lexemes, chars):
        '''
        Escanea un string en busqueda de un token de un largo no determinado.

        :param lexemes: lista de lexemas a considerar, todos de largo multiple.
        :param chars: iterador del string.
        :return: un token.
        '''

        for lex in lexemes:  # Se prueba con cada lexema.
            step = 1  # Se inicializa el paso en 1, y luego se amplia.
            found = False
            c = chars.getChar(step)  # Se obtiene 'size' caracteres adelante.
            while c is not None:  # Se itera hasta que el caracter sea nulo.
                if not re.fullmatch(lex.getPat(), c):  # Si no se produce un match, se frena.
                    break
                found = True
                step += 1  # Se incrementa el paso, para ver si la coincidencia continua.
                c = chars.getChar(step)

            if found:  # Si se ha encontrado, se retorna el token y avanza el iterador la cantidad necesaria.
                c = chars.getChar(step - 1)
                for i in range(len(c)):
                    chars.moveNext()
                return Token(lex.getType(), c)

        return None

    def addLexemes(self, lexemes):
        '''
        Agrega los lexemas en donde correspondan dentro de la matriz de lexemas.
        :param lexemes:
        :return:
        '''
        for lex in lexemes:
            lexemeSize = lex.size()  # Se obtiene el largo del lexema.
            lexerSize = len(self.__lexemes)  # Se obtiene el largo de la matriz de lexemas.
            if lexerSize - 1 < lexemeSize:  # Si el lexema es mayor que el largo, se agregan listas vacias hasta completar
                for i in range(lexemeSize - lexerSize + 1):
                    self.__lexemes.append([])

            self.__lexemes[lexemeSize].append(lex)  # Se agrega en la lista de lexemas del largo correcto.

    def __str__(self):
        '''
        Crea un string representativo del objeto de la clase.
        :return: string del objeto.
        '''

        string = "Lexer.\t\t\nInput String: '" + self.__inputString + "'\n"
        for i in range(len(self.__lexemes)):
            string += "Lenght " + str("*" if i == 0 else i) + " lexemes\n"
            lexemes = self.__lexemes[i]

            if len(lexemes) == 0:
                string += "\tNone\n"

            for lex in lexemes:
                string += "\t" + str(lex) + "\n"

        return string
