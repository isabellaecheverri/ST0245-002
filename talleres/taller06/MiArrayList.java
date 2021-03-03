/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Taller6;

/**
 *
 * @author User
 */
public class MiArrayList {
    private int size;
    private static final int DEFAULT_CAPACITY = 10;
    private int elements[]; 
    
    /**
    * El metodo constructor se utiliza para incializar
    * variables a valores neutros como 0 o null.
    * El contructor no lleva parámetros en este caso.
    */
    public void MiArrayLis() {
        size = 0;
        elements = new int[DEFAULT_CAPACITY];
    }     

    
    /**
    * Tiene la intención de retornar la longitud del objeto
    * @return longitud del objeto
    *
    * El size esta influenciado por las funciones add y del
    */
    public int size() {
        return size;
    }   
    
    /** 
    * @param e el elemento a guardar
    * Agrega un elemento e a la última posición de la lista
    *
    */
    public void add(int e) {
       if (size == elements.length){ // O(n)
            int[] nuevo = new int[elements.length+10]; //por defecto, es *2.0
            for(int i = 0; i < elements.length; i++)
                nuevo[i] = elements[i]; // copiar n elementos, se hace en n pasos
            elements = nuevo;
        }            
        else
            elements[size] = e;
        size = size + 1;
    }    
    
    
    /** 
    * @param i es un íncide donde se encuentra el elemento posicionado
    * Retorna el elemento que se encuentra en la posición i de la lista.
    *
    */
    public int get(int i) {
        for(int j=0;j<elements.length;j++){
            if(elements[j]==i){
                return j;
            }
            else{
                return -1;
            }
        }
    }
    
    
    /**
    * @param index es la posicion en la cual se va agregar el elemento
    * @param e el elemento a guardar
    * Agrega un elemento e en la posición index de la lista
    *
    */
    public void add(int index, int e) {
        if (size == elements.length){ // O(n)
            int[] nuevo = new int[elements.length+10]; //por defecto, es *2.0
            for(int i = 0; i < index; i++)
                nuevo[i] = elements[i]; // copiar n elementos, se hace en n pasos
            elements = nuevo;
            for(int i=index;i<nuevo.length;i++){
                nuevo[i]=elements[i-1];
            }
        }            
        else
            elements[size] = e;
        size = size + 1;
    } 

    /**
    * @param index es la posicion en la cual se va eliminar el elemento
    *
    * ELimina el elemento  en la posición index de la lista
    *
    */
    public void del(int index){
        if(index==elements.length-1){
            int[] nuevo = new int[elements.length-1];
            for(int i=0;i<nuevo.length;i++){
                nuevo[i]=elements[i];
            }
        }
        else{
            int[] nuevo= new int[elements.length-1];
            for(int i=0;i<index;i++){
                nuevo[i]=elements[i];
            }
            for(int i=index-1;i<nuevo.length;i++){
                nuevo[i]=elements[i+1];
            }
        }
    }
}