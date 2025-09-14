#Instituto Tecnologico de San Juan Del Río
#Estructura de datos 
#Tema: Ejercicios de Recursividad en Python 
#Rocio Molina Monroy

def aplanar(x):
    """
    Aplana una lista potencialmente anidada de enteros,
    preservando el orden.
    Ejemplo: [1, [2, [3,4], 5], [], 6] -> [1,2,3,4,5,6]
    """
    if not x:
        return []
    cabeza, resto = x[0], x[1:]
    if isinstance(cabeza, int):
        return [cabeza] + aplanar(resto)
    return aplanar(cabeza) + aplanar(resto)


# Pruebas
assert aplanar([]) == []
assert aplanar([1,2,3]) == [1,2,3]
assert aplanar([1,[2,[3,4],5],[],6]) == [1,2,3,4,5,6]

# Mostrar resultados
print(aplanar([]))                    # []
print(aplanar([1,2,3]))               # [1,2,3]
print(aplanar([1,[2,[3,4],5],[],6]))  # [1,2,3,4,5,6]