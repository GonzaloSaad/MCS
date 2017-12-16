import re


class Lexeme():
    '''
    Clase que encapsula el comportamiento deseado de un lexema.
    '''

    def __init__(self, type, pat):
        self.type = type
        self.pat = pat

    def setType(self, type):
        self.type = type

    def getType(self):
        return self.type

    def setPat(self, pat):
        self.pat = pat

    def getPat(self):
        return self.pat

    def __str__(self):
        return "Lexeme(" + self.type + "," + self.pat + ")"

    def size(self):

        if re.match(r'\[.-.\](?![\+\*\[])', self.pat):
            return 1

        tam = 0
        for c in self.pat:
            if c == "\\":
                continue
            tam += 1

        if tam > 1 and ("*" in self.pat or "+" in self.pat):
            tam = 0

        return tam
