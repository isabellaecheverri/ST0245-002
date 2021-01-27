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
    
    
    def comparar(self, other):
        if (self.año < other.get_año()):
            return "La fecha es anterior a la ingresada"
        
        if (self.año > other.get_año()):
            return "La fecha es posterior a la ingresada"
        
        if (self.mes < other.get_mes()):
            return "La fecha es anterior a la ingresada"
        
        if (self.mes > other.get_mes()):
            return "La fecha es posterior a la ingresada"

        if (self.dia < other.get_dia()):
            return "La fecha es anterior a la ingresada"
        
        if (self.dia > other.get_dia()):
            return "La fecha es posterior a la ingresada"
        
        return "Las fechas son iguales"
    
    def toString(self):
        return str(self.dia) + "-"+ str(self.mes) + "-" + str(self.año)
    
    
class Main():
    Fecha1 = Fecha(1,3,2017)
    Fecha2 = Fecha(29,2,2018)
    print(Fecha1.comparar(Fecha2))
    print(Fecha1.toString())