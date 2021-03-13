#LAB2
from matplotlib import pyplot as pl
import time
from random import randint

def insertionSort(x):
	for i in range(len(x)):#T(n)=c1*n
		j = i#c2*n
		while j > 0 and x[j-1]>x[j]:#(c3*n)*n
			temp = x[j]
			x[j] = x[j-1]
			x[j-1] = temp
			j -= 1
        
xis=[]
yis=[]

for i in range(1,200):#grafica con 200 arreglos diferentes 
    array = [randint(0,i) for x in range(i)]
    #print(array)
    timeIN = time.time()
    insertionSort(array)
    timeFIN =time.time()
    xis.append(i)
    yis.append(timeFIN-timeIN)
        
pl.xlabel("n array")
pl.ylabel("Tiempo de ejecucion")
pl.title("InsertionSort")
pl.plot(xis, yis, 'r', label = "InsertionSort")
pl.show

def mergeSort(x):
	result = []#c1
	if len(x) < 2:#c2
		return x#c3
	mid = int(len(x) / 2)#c4
	y = mergeSort(x[:mid])#T(n)=T(n/2)
	z = mergeSort(x[mid:])
	i = 0
	j = 0
	while i < len(y) and j < len(z):
		if y[i] > z[j]:
			result.append(z[j])
			j += 1
		else:
			result.append(y[i])
			i += 1
	result += y[i:]
	result += z[j:]
	return result

x=[]
y=[]
arreglo=[]
#for i in range(200,1):
    #arreglo=[arreglito = [randint(0,100) for x in range(i)] for y in range(i)]

for i in range(1,200):
    array = [randint(0,100) for x in range(i)]
    #array = [i for x in range(i)]
    #print(array)
    timeIN = time.time()
    mergeSort(array)
    timeFIN =time.time()
    x.append(i)
    y.append(timeFIN-timeIN)
        
pl.xlabel("n array")
pl.ylabel("Tiempo de ejecucion")
pl.title("mergeSort")
pl.plot(x, y, 'r', label = "mergeSort")
pl.show

arreglo=[[1,0],[2,1,0],[3,2,1,0],[4,3,2,1,0],[5,4,3,2,1,0],[6,5,4,3,2,1,0],[7,6,5,4,3,2,1,0],[8,7,6,5,4,3,2,1,0],[9,8,7,6,5,4,3,2,1,0],[10,9,8,7,6,5,4,3,2,1,0],[11,10,9,8,7,6,5,4,3,2,1,0],[12,11,10,9,8,7,6,5,4,3,2,1,0],[13,12,11,10,9,8,7,6,5,4,3,2,1,0],[14,13,12,11,10,9,8,7,6,5,4,3,2,1,0],[15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0],[16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0],[17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0],[18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0],[19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0],[20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]]
x20=[]
y20=[]

for i in range(0,20):
    #array = [randint(0,100) for x in range(i)]
    #array = [i for x in range(i)]
    #print(array)
    timeIN = time.time()
    mergeSort(arreglo[i])
    timeFIN =time.time()
    x20.append(i)
    print(str(timeFIN-timeIN))
    y20.append(timeFIN-timeIN)
 
pl.xlabel("n array")
pl.ylabel("Tiempo de ejecucion")
pl.title("insertionSort")
pl.plot(x20, y20, 'r', label = "insertionSort")
pl.show
