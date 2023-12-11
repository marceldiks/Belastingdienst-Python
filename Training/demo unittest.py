
def telop_maal_drie(a, b):
    """Doet een berekening
    
    >>> telop_maal_drie(3, 4)
    21

    >>> telop_maal_drie(300, 400)
    2100
    """
    
    return (a + b) * 3

    
    
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True) 
