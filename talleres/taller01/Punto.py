# -*- coding: utf-8 -*-
import math

class Punto2D():
    """Representacion de punto en 2 dimenciones"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x
        
    def get_y(self):
        return self.y
      
    def radio_polar(self):
       return math.sqrt((self.x*self.x)+(self.y*self.y))

    def angulo_polar(self):
        return math.atan(self.y/self.x)
    
    def dist_euclidiana(self, other):
        dx = self.x - other.get_x()
        dy = self.y- other.get_y()
        return math.sqrt((dx*dx)+(dy*dy))
    
    
class main():
    punto1 = Punto2D(10,20)
    print ("El valor de x es: "+ str(punto1.get_x()))
    print("El radio polar es de: "+str(punto1.radio_polar()))
    print("El angulo polar es de: "+ str(punto1.angulo_polar()))
    punto2 = Punto2D(0,0)
    print("La distancia entre los dos puntos es de: "+ str(punto1.dist_euclidiana(punto2)))
