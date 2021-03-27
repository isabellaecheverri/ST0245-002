package co.com.prueba;

public class List {

	private Nodo head;

	public void insertHead(Nodo nodo) {
		nodo.setNext(head);
		head = nodo;
	}

	public void insertEnd(Nodo nodo) {
		Nodo end = head;
		if (end == null) {
			head = nodo;
		} else {
			while (end.getNext() != null) {
				end = end.getNext();
			}
			end.setNext(nodo);
		}
	}

	public Nodo getHead() {
		return head;
	}

}
