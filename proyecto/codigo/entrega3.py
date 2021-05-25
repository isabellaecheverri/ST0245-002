import numpy as np
import glob
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import time
#import Image

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
##DESCOMPIMIR CON PERDIDAS
def descomprimirCP(arr):
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

#CARGAR LA IMAGEN
imagen = Image.open('3027309968_c8d7626265.jpg')
file = '3027309968_c8d7626265.jpg'

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
#COMPRIMMIR CON PERDIDAS  

def comprimirCP(img):
    tiempoinicial = time.time()
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
        #if(i==2):
                #reconstimg.save("Imagencomprimida"+file,"JPEG",optimize=True,quality=85)
    plt.show()
    """
    for i in range(5, 51, 5):
        reconstimg = np.matrix(U[:, :i]) * np.diag(sigma[:i]) * np.matrix(V[:i, :])
        plt.imshow(reconstimg, cmap='gray')
        title = "n = %s" % i
        plt.title(title)
        plt.show()
        """
    tiempofinal = time.time()
    #reconstimg.save("Imagencomprimida"+file+"JPEG",optimize=True,quality=85)
    print("El tiempo es",tiempofinal-tiempoinicial)
comprimirCP(imagen) 

#HUFFMAN COMPRESSION
def huffman_encode(alfa, prob, s):
    final = []
    for i in range(len(alfa)):
        final.append([alfa[i], prob[i]])
    final.sort(key = lambda x: x[1])
    tot = 0
    tree = []
    for i in range(len(final) - 1):
        i = 0
        left = final[i]
        final.pop(i)
        right = final[i]
        final.pop(i)
        tot = left[1] + right[1]
        tree.append([left[0], right[0]])
        final.append([left[0] + right[0],tot])
        final.sort(key = lambda x: x[1])
    code = []
    tree.reverse()
    alfa.sort()
    for i in range(len(alfa)):
        cd = ""
        for j in range(len(tree)):
            if alfa[i] in tree[j][0]:
                cd = cd + '0'
                if alfa[i] == tree[j][0]:
                    break
            else:
                cd = cd + '1'
                if alfa[i] == tree[j][1]:
                    break
        code.append([alfa[i],cd])
    encode = ""
    print("Codigos de Huffman")
    print("---------------------------------")
    print("Alfabeto", end = "\t")
    print("Palabra codigo")
    for i in range(len(code)):
        print(code[i][0], end = "\t\t")
        print(code[i][1])
    for i in range(len(s)):
        for j in range(len(code)):
            if s[i] == alfa[j][0]:
               encode = encode + str(code[j][1])
    print("Codigo Huffman para el  string " + s + " is " + encode)
    return [encode, code]


def huffman_decode(master_file):
    encode = list(master_file[0])
    code = master_file[1]
    s = ""
    count = 0
    flag = 0
    for i in range(len(encode)):
        for j in range(len(code)):
            if encode[i] == code[j][1]:
                s = s + str(code[j][0])
                flag = 1
        if flag == 1:
            flag = 0
        else:
            count = count + 1
            if count == len(encode):
                break
            else:
                encode.insert(i + 1,str(encode[i] + encode[i + 1]))
                encode.pop(i + 2)
    print("String decodificado" + str(master_file[0]) + " is " + s)


def convertiraString(arr):
    for ch in arr:
        ch = str(ch)
    return arr

def descomprimirHufffman(arr):
    tiempoinicial = time.time()
    acodificar = convertiraString(arr)
    
    string = str(acodificar)
    len_str = len(string)
    dictionary = dict()
    for i in string:
        if i in dictionary:
            dictionary[i] = dictionary[i] + 1
        else:
            dictionary[i] = 1
    alfabeto = []
    probabilidad = []
    for i in dictionary.items():
        alfabeto.append(i[0])
        probabilidad.append(i[1])
    for i in range(len(probabilidad)):
        probabilidad[i] = probabilidad[i] / len_str
    master_file = huffman_encode(alfabeto, probabilidad, string)
    huffman_decode(master_file)
    tiempofinal = time.time()
    print("El tiempo es",tiempofinal-tiempoinicial)
    #matriznueva = huffman_decode(master_file)
    import numpy
    numpo = numpy.array(vacas_enfermas[1])
    plt.imshow(numpo, cmap="gray")
    plt.savefig("huffman.jpg")
    plt.show() 

variable = descomprimirHufffman(vacas_enfermas[1])
print(variable)
