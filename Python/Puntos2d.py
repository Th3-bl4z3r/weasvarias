# Stefano Gay
class punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distancia(self, other):
        if self.x == other.x and self.y == other.y:
            return "Los puntos son iguales, la distancia es 0"
        distancia = round(((other.x - self.x)**2 + (other.y - self.y)**2)**(1/2), 3)
        return f"la distancia de ({self.x},{self.y}) a ({other.x}, {other.y}) es {distancia}"
    
    def recta(self, other):
        if other.y != self.y and self.x != other.x:
            pendiente = (other.y - self.y)/(other.x - self.x)
            interseccion = pendiente*(-self.x) + self.y
            recta = f"Y = {pendiente}X + {interseccion}"
            return f"la ecuación de la recta es: {recta}"  
              
        if self.x == other.x and self.y == other.y:
            return "Los puntos son iguales"
        
        elif other.y == self.y:
            return "recta horizontal"
        
        elif other.x == self.x:
            return "recta vertical"

    def __str__(self):
        return f"({self.x},{self.y})"

coord_x = int(input("ingresa las coordenadas del eje X: "))
coord_y = int(input("ingresa las coordenadas del eje Y: "))

punto2d = punto2D(coord_x, coord_y)

punto2_x = int(input("ingresa las coordenadas X del segundo punto: "))
punto2_y = int(input("ingresa las coordenadas Y del segundo punto: "))

otro = punto2D(punto2_x, punto2_y)

print(f"punto 1: {punto2d}")
print(f"punto 2: {otro}")
print(punto2d.distancia(otro))
print(punto2d.recta(otro))