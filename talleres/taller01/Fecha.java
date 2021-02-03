/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author User
 */

public class Fecha {
    

    /*
    varibales con atributo final indican que una variable es de tipo 
    constante, es decir, no admitir� cambios despu�s de su declaraci�n y asignaci�n de valor.
    final determina que un atributo no puede ser sobreescrito o redefinido.
    Se le asigna esta caracter�stica para evitar que se sobrescriban valores.
    tener en cuenta tipado de las 3 variables!.
    */

    private final int dia;
    private final int mes;
    private final int anio;


    /**
     * Se inicializan las variables globales en el constructor de manera que no posean valores nulos o 0s.
     */
    public Fecha(int dia, int mes, int anio) {
    this.dia = dia;
    this.mes = mes;
    this.anio = anio;

    }

    /**
     * M�todo para obtener la variable global dia.
     *
     * @return el dia
     */
    public int dia() {
				return dia;
    }

    /**
     * M�todo para obtener la variable global mes.
     *
     * @return el mes
     */
    public int mes() {
				return mes;
    }

    /**
     * M�todo para obtener la variable global anio.
     *
     * @return el a�o
     */
    public int anio() {
				return anio;
    }

    /**
    * @param otra representa la fecha con la cual se va a comparar.
    *
    * El m�todo comprar se encarga de devolvernos respuesta a tres posibilidades.
    * 1: si la fecha es menor que la otra retorna -1.
    * 2: si la fecha es igual que la otra retorna 0.
    * 3: si la fecha es mayor que la otra retorna 1.
    *
    * @return -1 s� es menor; 0 s� es igual; 1 s� es mayor.
    *
    */

    public int comparar(Fecha otra) {
					 if (this.anio <  otra.anio)
            return -1;
        if (this.anio > otra.anio)
            return 1;

        if (this.mes < otra.mes)
            return -1;
        if (this.mes > otra.mes)
            return 1;

        if (this.dia < otra.dia)
            return -1;
        if (this.dia > otra.dia)
            return 1;

        return 0 ;
    }


     /**
    * toString se encargar� de convertir el tipo abstracto fecha en un tipo cadena
    * para su posterior visualizaci�n
    *
    * @return una cadena que contiene la fecha
    */
    public String toString(Fecha fecha) {
        int[] arreglofecha = new int[3];
        arreglofecha[0] = fecha.dia;
        arreglofecha[1] = fecha.mes;
        arreglofecha[2] = fecha.anio;
        String fechita = " ";
        for(int i =0; i<3; i++){
          fechita = Integer.toString(arreglofecha[i]);
        }
        return fechita;
    }
}