package co.com.prueba;

public class Main {

	public static void main(String... args) {
		String line = "asd[gfh[[dfh]hgh]fdfhd[dfg[d]g[d]dg";
		String aux = "";
		boolean beginning = false;
		char ind;
		Nodo n = null;
		List lista = new List();

		int i = 0;
		while (i < line.length()) {
			if (line.charAt(i) == '[' || line.charAt(i) == ']' || i == line.length() - 1) {
				ind = line.charAt(i);
				aux = ind == '[' || ind == ']' ? line.substring(0, i).replace("[", "").replace("]", "") : line.substring(0, i + 1);
				line = line.substring(i + 1);
				i = 0;
				n = new Nodo(aux);
				if (beginning) {
					lista.insertHead(n);
				} else {
					lista.insertEnd(n);
				}
				beginning = ind == '[';
			} else {
				i++;
			}
		}

		Nodo ini = lista.getHead();
		while (ini != null) {
			System.out.print(ini.getValue());
			ini = ini.getNext();
		}
	}

}
