class ArbolBinarioBusqueda:

    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def longitud(self):
        return self.tamano

    def __len__(self):
        return self.tamano

    def __iter__(self):
        return self.raiz.__iter__()
    
class NodoArbol:
   def __init__(self,clave,izquierdo=None,derecho=None):
        self.clave = clave
        self.Izquierdo = izquierdo
        self.Derecho = derecho

def agregar(self,clave,valor):
    if self.raiz:
        self._AUXagregar(clave)
    else:
        self.raiz = NodoArbol(clave)
    self.tamano = self.tamano + 1

def _AUXagregar(self,clave,valor,nodoActual):
    if clave < nodoActual.clave:
        if nodoActual.Izquierdo!=None:
               self._AUXagregar(clave,valor,nodoActual.hijoIzquierdo)
        else:
               nodoActual.Izquierdo = NodoArbol(clave,valor,padre=nodoActual)
    else:
        if nodoActual.Derecho!=None:
               self._AUXagregar(clave,valor,nodoActual.hijoDerecho)
        else:
               nodoActual.Derecho = NodoArbol(clave)
               
def __setitem__(self,c,v):
    self.agregar(c,v)
    
def obtener(self,clave):
    if self.raiz:
        res = self._obtener(clave,self.raiz)
        if res:
            return res.cargaUtil
        else:
            return None
    else:
        return None

def _AUXobtener(self,clave,nodoActual):
    if not nodoActual:
        return None
    elif nodoActual.clave == clave:
        return nodoActual
    elif clave < nodoActual.clave:
        return self._AUXobtener(clave,nodoActual.hijoIzquierdo)
    else:
        return self._AUXobtener(clave,nodoActual.hijoDerecho)

def __getitem__(self,clave):
    return self.obtener(clave)

def __contains__(self,clave):
    if self._obtener(clave,self.raiz):
        return True
    else:
        return False
    
def eliminar(self,clave):
   if self.tamano > 1:
      nodoAEliminar = self._obtener(clave,self.raiz)
      if nodoAEliminar:
          self.remover(nodoAEliminar)
          self.tamano = self.tamano-1
      else:
          raise KeyError('No existe en el arbol')
   elif self.tamano == 1 and self.raiz.clave == clave:
      self.raiz = None
      self.tamano = self.tamano - 1
   else:
      raise KeyError('No existe en el arbol')

def __delitem__(self,clave):
    self.eliminar(clave)

def printPostorder(raiz):
 
    if raiz:
 
        printPostorder(raiz.Izquierdo)
 
        # the recur on right child
        printPostorder(raiz.Derecho)
 
        # now print the data of node
        print(raiz.clave)


def descifrarPreorder(arreglo):
    nuevoArbol = ArbolBinarioBusqueda()
    arreglo[1]= nuevoArbol.raiz()
    for i in range (1,len(arreglo)-1):
        agregar(arreglo[i])










               