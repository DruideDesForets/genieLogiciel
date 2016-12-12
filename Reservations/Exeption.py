import re

class RomanError(Exception) : 
    """ Exception generique """
    pass
class OutOfRangeError(RomanError) : 
    """ Le nombre n’est pas dans l’intervalle de valeur """ 
    pass
class NotIntegerError(RomanError) :
    """ Le nombre n’est pas un entier """
    pass
class InvalidRomanNumeralError(RomanError) :
    """ Le chi?re romain n’est pas valide """ 
    pass 