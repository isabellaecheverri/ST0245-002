from matplotlib import pyplot as pl
import time
from random import randint

def insertion_sort(list):
   for i in range(len(list)):
      for j in range(len(list)):
         if (list[i]>list[j]):
            aux=list[i]
            list[i]=list[j]
            list[j]=aux
lista=[]
xis=[]
yis=[]
for i in range(10):
    for j in range(20):
        num = randint(0,10)
        lista.append(num)
        timeIN = time.time()
        insertion_sort(lista)
        timeFIN =time.time()
        xis.append(i)
        yis.append(timeFIN-timeFIN)
        
pl.xlabel("n array")
pl.ylabel("Tiempo de ejecucion")
pl.title("insertion_sort")
pl.plot(xis, yis, 'r', label = "Insertion_sort")
pl.show

def tablas(n):
    for i in range(0,n):
        for j in range(0,n):
            ans = i*j
            print(str(i)+'*'+str(j)+'='+str(ans))

xtab = []
ytab = []

for i in range(20):
    tiemin =time.time()
    tablas(i)
    tiemfin = time.time()
    print(str(i)+' '+str(tiemfin-tiemin))
    xtab.append(i)
    ytab.append(tiemfin-tiemin)
pl.xlabel("n array")
pl.ylabel("Tiempo de ejecucion")
pl.title("tablas")
pl.plot(xtab, ytab, 'r', label = "Tablas")
pl.show   
            
def ArraySum(arr):
    result =0
    for i in range(0,len(arr)):
        result =arr[i]+result     
    print(result)

xsum = []
ysum = []

for i in range(10):
    for j in range(20):
        num = randint(0,10)
        lista.append(num)
        timeINi = time.time()
        insertion_sort(lista)
        timeFINa =time.time()
        xsum.append(i)
        ysum.append(timeFINa-timeINi)
pl.xlabel("n array")
pl.ylabel("Tiempo de ejecucion")
pl.title("arraysum")
pl.plot(xtab, ytab, 'r', label = "Arraysum")
pl.show   
            
            
            