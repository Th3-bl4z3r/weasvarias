def fila(matriz: list, num: int, fila: int) -> bool:
    '''
    Función que verifica si se puede colocar un número en la fila dada.
    retorna True en caso de no estar el número en esa fila y False en caso contrario
    '''
    if num < 1 or num > 9:
        raise ValueError("El número debe ser entre 1 y 9!")
    verificacion = False
    p = matriz[fila]
    if str(num) not in p[0]:
        verificacion = True

    return verificacion

def columna(matriz: list, num: int, columna: int):
    '''
    Función que verifica si se puede colocar un número en la columna dada.
    retorna True en caso de no estar en la columna y False en caso contrario
    '''
    if num < 1 or num > 9:
            raise ValueError("El número debe ser entre 1 y 9!")
    verificacion_columna = False
    j = []
    for n in matriz:
        j.append(n[0][columna])
    if str(num) not in j:
        verificacion_columna = True

    return verificacion_columna

def Grilla(matriz: list, num: int, fila: int, columna: int):
    '''
    Función que verifica si es posible colocar un número (num) en
    la sub-grilla correspondiente a matriz[fila][columna]
    '''
    sub_grilla = False
    # voy a tener que hacer todos los casos aaaaaaaaaaaaaaaaaaaa
    '''
       0 1 2  3 4 5  6 7 8
      __________________
    0 |3 0 7  0 6 0  0 4 0
    1 |0 0 0  0 0 0  0 0 0
    2 |2 5 0  0 0 7  1 9 6
    
    3 |4 0 2  9 0 1  3 6 0
    4 |0 0 0  0 3 6  0 0 0
    5 |9 0 3  0 0 0  7 0 1
    
    6 |0 4 0  0 0 0  2 0 0
    7 |0 0 0  8 0 0  6 1 4
    8 |0 2 0  5 0 0  9 0 0
    
    '''

    grilla = []
    
    print("N° de celda: ",matriz[fila][0][columna])

    if fila < 3:
        if columna < 3:
            grilla.append([matriz[0][0][0:3], matriz[1][0][0:3], matriz[2][0][0:3]])

        elif columna >= 3 and columna < 6:
            grilla.append([matriz[0][0][3:6], matriz[1][0][3:6], matriz[2][0][3:6]])

        elif columna >= 6 and columna <= 8:
            grilla.append([matriz[0][0][6:], matriz[1][0][6:], matriz[2][0][6:]])

    elif fila >= 3 and fila < 6:
        if columna < 3:
            grilla.append([matriz[3][0][0:3], matriz[4][0][0:3], matriz[5][0:3]])

        elif columna >= 3 and columna < 6:
            grilla.append([matriz[3][0][3:6], matriz[4][0][3:6], matriz[5][3:6]])

        elif columna >= 6 and columna <= 8:
            grilla.append([matriz[3][0][6:], matriz[4][0][6:], matriz[5][6:]])

    elif fila >= 6:
            if columna < 3:
                grilla.append([matriz[6][0][0:3], matriz[7][0][0:3], matriz[8][0][0:3]])

            elif columna >= 3 and columna < 6:
                grilla.append([matriz[6][0][3:6], matriz[7][0][3:6], matriz[8][0][3:6]])

            elif columna >= 6 and columna <= 8:
                grilla.append([matriz[6][0][6:], matriz[7][0][6:], matriz[8][0][6:]])


    return grilla[0]