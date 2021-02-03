/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Taller1;

/**
 *
 * @author User
 */
/**
 * La clase Punto tiene la intención de representar coordenadas en el espacio y calcular su distancia.
 * 
* @author Mauricio Toro, Andres Paez
 * @version 1
 */
 
public class Punto{??????
 
    private double x, y;

    public Punto(double x, double y) {??????
        this.x = x;
        this.y = y;
    }?????
    public double x(){??????
        return x;
    }???
 
    public double y() {??????
        return y;
    }?

    public double radioPolar() {??????
        return Math.sqrt(Math.pow(x,2) + Math.pow(y,2));
    }??????
 
    public double anguloPolar() {??????
        return Math.atan(y/x);
    }?????

    public double distanciaEuclidiana(Punto otro){??????
        double x2 = otro.x;
        double y2 = otro.y;
        return Math.sqrt( Math.pow((x2-x),2)+Math.pow((y2-y),2));
    }??????
}??????