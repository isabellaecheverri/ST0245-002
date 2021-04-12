import numpy as np
import glob
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


# get data file names
path =r'C:/Users/User/Desktop/Semestre 2/Estructura Datos y Algoritmos/Proyecto Estructuras/csv/ganado_enfermo'
filenames = glob.glob('C:/Users/User/Desktop/Semestre 2/Estructura Datos y Algoritmos/Proyecto Estructuras/csv/ganado_enfermo'+ "/*.csv")

vacas_enfermas = []
for filename in filenames:
    vacas_enfermas.append(pd.read_csv(filename))

# Concatenate all data into one DataFrame
big_frame = pd.concat(vacas_enfermas, ignore_index=True)
    
#print(vacas_enfermas)

path =r'C:/Users/User/Desktop/Semestre 2/Estructura Datos y Algoritmos/Proyecto Estructuras/csv/ganado_sano'
filenames = glob.glob('C:/Users/User/Desktop/Semestre 2/Estructura Datos y Algoritmos/Proyecto Estructuras/csv/ganado_sano'+ "/*.csv")

vacas_sanas = []
for filename in filenames:
    vacas_sanas.append(pd.read_csv(filename))

# Concatenate all data into one DataFrame
#big_frame = pd.concat(vacas_sanas, ignore_index=True)
    
#print(vacas_sanas)

def descomprimir(arr):
    img = np.matrix(arr)
    #U, sigma, V = np.linalg.svd(imgmat)
    U, sigma, V = np.linalg.svd(img)
    reconstimg = np.matrix(U[:, :1]) * np.diag(sigma[:1]) * np.matrix(V[:1, :])
    plt.imshow(reconstimg, cmap='gray');
    for i in range(2, 4):
        reconstimg = np.matrix(U[:, :i]) * np.diag(sigma[:i]) * np.matrix(V[:i, :])
        plt.imshow(reconstimg, cmap='gray')
        title = "n = %s" % i
        plt.title(title)
    #if(i==3):
        #reconstimg.save("Comprimida_","JPEG",optimize=True,quality=85)
    plt.show()
    for i in range(5, 51, 5):
        reconstimg = np.matrix(U[:, :i]) * np.diag(sigma[:i]) * np.matrix(V[:i, :])
        plt.imshow(reconstimg, cmap='gray')
        title = "n = %s" % i
        plt.title(title)
        plt.show()
descomprimir(vacas_enfermas[1]) 

#CARGAR LA IMAGEN
imagen = Image.open('Compressed_04be43ab919b6b22d950d3b59834f4a1.jpg')
file = 'Compressed_04be43ab919b6b22d950d3b59834f4a1.jpg'

def matriz_imagen(img):
    #CONVERTIR LA IMAGEN A ESCALA DE GRISES
    img2 = img.convert('LA')
    matrix_img = np.array(list(img2.getdata(band=0)), float)
    print(matrix_img)
    matrix_img.shape = (img2.size[1], img2.size[0])
    print(matrix_img.shape)
    imgmat = np.matrix(matrix_img)
    plt.figure(figsize=(9,6))
    plt.imshow(imgmat, cmap='gray');
    return imgmat
    
def comprimir(img):
    matriz = matriz_imagen(imagen)
    #U, sigma, V = np.linalg.svd(imgmat)
    U, sigma, V = np.linalg.svd(matriz)
    reconstimg = np.matrix(U[:, :1]) * np.diag(sigma[:1]) * np.matrix(V[:1, :])
    plt.imshow(reconstimg, cmap='gray');
    for i in range(2, 4):
        reconstimg = np.matrix(U[:, :i]) * np.diag(sigma[:i]) * np.matrix(V[:i, :])
        plt.imshow(reconstimg, cmap='gray')
        title = "n = %s" % i
        plt.title(title)
    if(i==3):
        imagen.save("Comprimida_"+file,"JPEG",optimize=True,quality=85)
    plt.show()
    for i in range(5, 51, 5):
        reconstimg = np.matrix(U[:, :i]) * np.diag(sigma[:i]) * np.matrix(V[:i, :])
        plt.imshow(reconstimg, cmap='gray')
        title = "n = %s" % i
        plt.title(title)
        plt.show()
comprimir(imagen) 
    






