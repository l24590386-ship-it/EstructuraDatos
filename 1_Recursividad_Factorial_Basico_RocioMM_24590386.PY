#Instituto Tecnologico de San Juan Del Río
#Estructura de datos 
#Tema: Ejercicios de Recursividad en Python 
#Rocio Molina Monroy 

def factorial(n: int) -> int: 
    """ 
    Calcula n! recursivamente. 
    Precondición: n >= 0 
    """ 
    if n < 0: 
        raise ValueError("factorial: n debe ser >= 0") 
    if n == 0 or n == 1: 
        return 1 
    return n * factorial(n - 1)

# Pruebas 
print(factorial(0))  # 1
print(factorial(1))  # 1
print(factorial(5))  # 120