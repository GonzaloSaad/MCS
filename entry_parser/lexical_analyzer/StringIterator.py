

class StringIterator():
    '''
    Clase para iterar un string.
    '''

    def __init__(self, string):
        '''
        Constructor de la clase.
        '''

        self.__string = string
        self.__current = 0

    def getChar(self, cant=1):
        '''
        Retorna los siguientes 'cant' caracteres.
        :param cant: cantidad de caracteres.
        :return: los siguientes 'cant' caracteres.
        '''

        nextIndex = self.__current + cant

        if nextIndex > len(self.__string):
            return None

        return self.__string[self.__current:nextIndex]

    def moveNext(self):
        '''
        Mueve el señalador en una posicion hacia adelante.
        '''

        self.__current += 1

    def movePrev(self):
        '''
        Mueve el señalador en una posicion hacia atras.
        '''

        self.__current -= 1

    def hastNext(self):
        '''
        Indica si hay un caracter siguiente.
        :return: true si hay un caracter mas.
        '''

        return self.__current < len(self.__string)

    def next(self):
        '''
        Muestra el siguiente caracter.
        :return: el siguiente caracter.
        '''

        return self.getChar()
