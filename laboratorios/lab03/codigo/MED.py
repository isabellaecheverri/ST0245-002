import pandas as pd

dataVertices = pd.read_csv('Vertices.csv')
print(dataVertices.head())

dataArcos = pd.read_csv('Arcos.csv')
print(dataArcos.head())

diccArcos = {}
for i in range(len(dataArcos)):
    diccArcos[(dataArcos.iloc[i]['ID'],dataArcos.iloc[i]['ID1'])] = dataArcos.iloc[i]['ID'],dataArcos.iloc[i]['ID1']

print("El diccionario de los arcos es:")
print(diccArcos)

diccVert = {}
for i in range(len(dataVertices)):
    diccVert[(dataVertices.iloc[i]['ID'])] = dataVertices.iloc[i]['ID']

print("El diccionario de los vertices es:")
print(diccVert)