def sumar(n1,n2):
    """Permite sumar dos números."""
    print(f"El resultado de la suma es {n1+n2}")

def restar(n1,n2):
    """Permite restar dos números."""
    print(f"El resultado de la resta es {n1-n2}")

def multiplicar(n1,n2):
    '''Permite multiplicar dos números.'''
    print(f"El resultado del producto es {n1*n2}")

def dividir(n1,n2):
    '''
    Permite dividir dos números.
    Si el denominador es cero se avisa.
    '''
    if n2:
        print(f"El resultado de la división es {n1/n2}")
    else:
        print("División por Cero")
