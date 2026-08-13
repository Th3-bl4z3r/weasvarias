from Sudoku import *

print("| Python Sudoku Solver |\n")
archivo = input("ingresa el nombre del archivo a resolver: \n~ ")

# Abro el archivo y con un Context Manager:
with open(f"xd/archivos/{archivo}", "r") as xd:
    j = xd.readlines()

puzle = [] # defino la matriz que será el Sudoku a resolver como una lista

for n in j:
    puzle.append([n[0:].strip()]) # añado cada línea del archivo a la matriz sin los espacios al final


# Imprimo el puzle a resolver en un formato más "ordenado"
print("Puzzle a resolver: \n  -------------")
for p in puzle:
    print("  |", p[0], "|")
print("  -------------")


# probando las funciones importadas del archivo Sudoku.py ...

print(f'Prueba de columna número 1 y col. 8: {columna(puzle, 1, 8)}')


print("Prueba de grilla, número 5, fila 6, columna 7")
print(Grilla(puzle, 5, 6 , 7))
