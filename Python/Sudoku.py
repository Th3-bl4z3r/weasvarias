entrada = input().strip()
# el programa debe leer el nombre del archivo recibido para obtener la matriz.

def matrix(entrada):
    '''
    función que recibe como argumento una matriz 9x9
    y la ordena de 3 en 3 en una matriz.
    '''
    matriz = []
    for n in range(0, len(entrada), 9):
        matriz.append([entrada[n:n+9].replace("0", "_")])
    return matriz

'''
|| Las matrices 9x9 están en formato tal que los 0's significan que hay una celda vacía.
- Por ejemplo:

030000040
290000057
000002000
006000000
000010000
000000900
000900000
960000074
080000060
'''

m = matrix(entrada)
for n in m:
    print(n)

'''
Reglas usuales del Sudoku:
• Un tablero de Thermo Sudoku está compuesto de una grilla de 9x9 celdas. A su vez la grilla
está subdividida en 9 cajas de 3x3.
• La grilla además puede contar con dígitos iniciales en distintas celdas.
'''

def verificar_fila(matriz, num, f):
    '''
    recibe como argumento la matriz, un número a colocar y la fila.
    retorna True en caso de poder colocar el número en la fila.
    retorna False en caso contrario.
    '''
    Verif = False
    for n in matriz[f]:
        if str(num) not in n:
            Verif = True
    return Verif