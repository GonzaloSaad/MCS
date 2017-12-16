import math

'''
Este modulo contiene todas las funciones que se utilizaran en el function_parser y que son reconocidad por 
el analizador lexico. 
La idea principal es que la signatura de las funciones coincidan con el lexeme que permite reconocerlas, 
por ende hay que tener siempre actualizada la relacion entre este archivo y FunctionLexer.
'''


def cos(x):
    return math.cos(x)

def sin(x):
    return math.sin(x)

def sen(x):
    return math.sin(x)

def tg(x):
    return math.tan(x)

def log(x):
    return math.log10(x)

def log2(x):
    return math.log2(x)

def ln(x):
    return math.log(x,math.e)

pi = math.pi

e = math.e




