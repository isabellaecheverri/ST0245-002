/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Taller7;

/**
 *
 * @author User
 */


   import java.lang.IndexOutOfBoundsException; // Usar esto cuando se salga el índice
// Una lista simplemente enlazada
public class LinkedListMauricio {
private Node first;
private int size;
public LinkedListMauricio()
{
	size = 0;
	first = null;	
}

	/**
	 * Returns the node at the specified position in this list.
	 * @param index - index of the node to return
	 * @return the node at the specified position in this list
	 * @throws IndexOutOfBoundsException
	 */
	private Node getNode(int index) throws IndexOutOfBoundsException {
		if (index >= 0 && index < size) {
			Node temp = first;
			for (int i = 0; i < index; i++) {
				temp = temp.next;
			}
			return temp;
		} else {
			throw new IndexOutOfBoundsException();
		}
	}

	/**
	 * Returns the element at the specified position in this list.
	 * @param index - index of the element to return
	 * @return the element at the specified position in this list
         * @throws IndexOutOfBoundsException
	 */
	public int get(int index) throws IndexOutOfBoundsException {
		temp = getNode(index);
		return temp.data;
}

public void insertarAlInicio(int data){
    Nodo nuevoNodo = new Node(data);
    nuevoNodo.next = first; //porque el primero puede ya existir
    first = nuevoNodo;
    size = size + 1;
}

// Retorna el tamaño actual de la lista
public int size()
{
	return size;
}

// Inserta un dato en la posición index
public void insert(int data, int index)
{
	//1. Me paro en el nodo anterior, es decir, el nodo en pos index - 1
  //2. Guardo en un temporal el siguiente del nodo anterior, es decir el nodo en pos index
  //3. Borro la flecha que va del anterior al siguiente del anterior
  //4. Creo un nuevo nodo con dato data
  //5. EL nuevo nodo es apuntado por el anterior, o sea el siguiente del anterior es el nuevo
  //6. El nuevo nodo apunta al que antes era el siguiente, que guardamos en un temporal
}

// Borra el dato en la posición index
public void remove(int index)
{
	...
}

// Verifica si está un dato en la lista
public boolean contains(int data)
{
	...
}











//¿Cuál es el peor caso? !!!
   def insertionSort (array):
    	  n = len(array)
        for i in range(1,n): //La barrita verde
        	for j in range(i, 0, -1): # Insertar en la parte ordenada
             bailar(a, j, j-1) #C3 =  1 + 1 + 1
    
    def bailar (array,  i,  j):
       temp = array[i]
       array[i] = array[j]  
       array[j] = temp
        
    /**
    * @param array es un arreglo de números desordenados
    * El método insertionSort tiene la intención ordenar los números
    * del arreglo array por el método insertion:
    * @see <a href=""> Insertion Sort <a/>
    * mediante la anidación de funciones cíclicas (while/for/...)
    * 
    */
    public static int[] insertionSort (int[] array){
    	  int n = array.length;
        for(int i = 1; i < n; i++) // La barrita verde
        	for(int j = i; j >= 0; j--) // Insertar en la parte ordenada
             bailar(a, j, j-1);
    } 
    public static void bailar (int[] array, int i, int j){
       int temp = array[i];
       array[i] = array[j];  
       array[j] = temp;
    }
}
    

