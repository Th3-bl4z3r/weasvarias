print("| Python Sudoku Solver |\n")
archivo = input("ingresa el nombre del archivo a resolver: \n~ ")


with open(f"xd/archivos/{archivo}") as xd:
    j = xd.readlines()

puzle = []
for n in j:
    puzle.append([n[0:].strip()])


for p in puzle:
    print(p)

def verificar_fila(matriz: list, num: int, fila: int) -> bool:
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


while True:
    x = int(input("num: "))
    if x == -1:
        break
    f = int(input("fila: "))
    print(verificar_fila(puzle, x, f))

def verificar_columna(matriz: list, num: int, columna: int):
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

print(verificar_columna(puzle, 1, 8))