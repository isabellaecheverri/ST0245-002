# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 11:02:44 2021

@author: mimar
"""

class Fecha():
   
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año
        
    def get_dia(self):
        return self.dia 
    
    def get_mes(self):
        return self.mes
    
    def get_año(self):
        return self.año
    
    # -1 si la fecha es menor que la otra
    # 0 si las fechas son iguales
    # 1 si la fecha es mayor que la otra
    def comparar(self, other):
        if (self.año < other.get_año()):
            return -1
        
        if (self.año > other.get_año()):
            return 1
        
        if (self.mes < other.get_mes()):
            return -1
        
        if (self.mes > other.get_mes()):
            return 1

        if (self.dia < other.get_dia()):
            return -1
        
        if (self.dia > other.get_dia()):
            return 1
        
        return 0
    
    def toString(self):
        return str(self.dia) + "-"+ str(self.mes) + "-" + str(self.año)
    
    
class Main():
    Fecha1 = Fecha(1,3,2017)
    Fecha2 = Fecha(29,2,2018)
    if Fecha1.comparar(Fecha2)==-1:
        print("La fecha es menor a la ingresada")
    elif Fecha1.comparar(Fecha2)==1:
        print("La fecha es mayor a la ingresada")
    elif Fecha1.comparar(Fecha2)==0:
        print("Las fecha son iguales ")
    
    print(Fecha1.toString())