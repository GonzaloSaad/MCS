

class Token(object):
    '''
    Clase que encapsula el comportamiento de un token.
    '''

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def setType(self, type):
        self.type = type

    def getType(self):
        return self.type

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def __str__(self):
        return "Token(" + self.type + ",'" + self.value + "')"
