#!/usr/bin/python
from matplotlib import pyplot as pl
import time


def arrayMax_aux(arr, i, max):
   if i == len(arr):
        return max
   else:
        if arr[i] > max:
            max = arr[i]
        return arrayMax_aux(arr, i+1, max)

arr = []
x1 =[]
y1=[]
for i in range(1,30):
    for j in range(1,100):
        arr.append(j)
    tiempoin = time.time()
    arrayMax_aux(arr,0,0)
    tiempofin = time.time()
    x1.append(i)
    y1.append(tiempofin-tiempoin)
    print(i,tiempofin-tiempoin)
    i*5
pl.xlabel('Maximo de un arreglo')
pl.ylabel('Tiempo de ejecucion')
pl.title('Ejecucion maximo')
pl.plot(x1,y1,'r') # domain of x(n) vs time
pl.legend(( 'Recursive', ) )
pl.show()
x=[]
y=[]
def fib_r(n):    
            if(n==0):
                return 0;
            else:
                if(n==1):
                    return 1
                else:
                    return fib_r(n-1)+fib_r(n-2)

for i in range (1,100):
    inicio = time.time()
    fib_r(i)
    fin = time.time()
    x[i]=i
    y[i]=fin-inicio
    print(i,fin-inicio)
    i*5
    
pl.xlabel('Numero de Fibonacci')
pl.ylabel('Tiempo de ejecucion')
pl.title('Recursive fibonacci vs interative fibonacci')
pl.plot(x,y,'r') # domain of x(n) vs time
pl.legend(( 'Recursive', ) )
pl.savefig("Fibor.png")  # produce a .png file
pl.show()
def groupSum( start, nums, target):
     if (start == len(nums)):
         return target == 0    
     else:
        anormal = groupSum(start+1, nums, target - nums[start]);
        normal = groupSum(start+1, nums, target)
        return anormal || normal
  
    






