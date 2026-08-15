import os
from producto import *

def cargar_productos(ruta: str) -> list:
    with open(ruta, "r", encoding="utf-8") as prod:
        archivo = prod.readlines()

    productos = []
    for n in archivo:
        n = n.strip().split(',')
        nombre = n[0]
        precio = int(n[1])
        stock = int(n[2])
        Nuevo_Producto = Producto(nombre, precio, stock)
        productos.append(Nuevo_Producto)
    return productos


def simular_ventas(productos: list) -> None:
    for producto in productos:
        producto.vender()


if __name__ == '__main__':
    ruta = os.path.join('data', 'menu.txt')

    productos = cargar_productos(ruta)

    print('=== DCCafeteria ===')
    for producto in productos:
        print(producto.descripcion())
    print(f'Productos registrados: {Producto.total_productos}')
    simular_ventas(productos)
    simular_ventas(productos)
