class Nodo:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

	def __repr__(self):
		return f'{self.data}'

class BinaryTree:
    def __init__(self):
        self.root = None
    
    # ------------------------------------------------------
    def insertar(self, data):
        if self.root is None:
            self.root = Nodo(data)
        else:
            self.__insertar_aux(data, self.root)

    def __insertar_aux(self, data, actual):
        if actual.data == data:
            return 

        if data > actual.right:
            if actual.right is None:
                actual.right = data
            else:
                self.__insertar_aux(data, actual.rigth)
        else:
            if actual.left is None:
                actual.left = data
            else:
                self.__insertar_aux(data, actual.left)

    # ------------------------------------------------------    
    def buscar(self, data):
        return self.__buscar_aux(data, self.root)

    def __buscar_aux(self, data, actual):
        if actual is None:
            return False
        
        if actual.data == data:
            return True
        
        if data > actual.data:
            return self.__buscar_aux(data, data.rigth)
        else:
            return self.__buscar_aux(data, data.left)
            
    # -----------------------------------------------
    def borrar(self, data):
        self.__borrar_aux(data, self.root)

    def __borrar_aux(self, data, actual):
        if actual is None:
            return
        
        if data > actual.data:
            actual.right = self.__borrar_aux(data, actual.right())
        elif data < actual.data:
            actual.left = self.__borrar_aux(data, actual.left)
        else:
            if actual.left is None:
                temp = None
                return temp
            elif actual.right is None:
                temp = None
                return temp
            else:
                temp = self.__minValueNode(data, actual.data)
                actual.data = temp.data
                actual.right = self.__borrar_aux(temp.data, data)

        return actual

    def __minValueNode(self, actual):
        temp = actual
        while(temp.left is not None):
            temp = temp.left 
    
        return temp
        

    # ------------------------------------------------------
    # In-Orden        
    def imprimir(self):
        self.__imprimir_aux(self.root)
        
    def __imprimir_aux(self, actual):
        if actual is not None:
            self.__imprimir_aux(actual.left)
            print(actual.data)
            self.__imprimir_aux(actual.right)
            
    # ------------------------------------------------------
    def dibujar(self):
        return  f'digraph G {"{"} \n {self.__dibujar_aux(self.root)} \n{"}"}'
    
    def __dibujar_aux(self, actual):
        if actual is None:
            return 
        else:
            if actual.left is not None and actual.right is not None:
                return f'{actual} -> {actual.left} \n {actual} -> {actual.right}'
            if actual.left is not None:
                return f'{actual} -> {actual.left}'
            if actual.right is not None:
                return f'{actual} -> {actual.right}'


if __name__ == '__main__':
    b = BinaryTree()
    b.insertar(4)
    b.insertar(3)
    b.insertar(5)
    #b.imprimir()
    #b.borrar(3)
    print(b.buscar(3))
    b.imprimir()
    print(b.dibujar())