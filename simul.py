from matplotlib import pyplot as plt
from scipy.spatial import distance
import random
import antAlgorit as aco

x = [4, 4, 1, 0, 0, 4, 10, 6, 6, 7] # pontos (x,y) escolhidos aleatoriamente
y = [7, 3, 4, 7, 6, 6, 6, 6, 10, 4]
print("x=",x,"\ny=",y)

def dist(a,b): #faz grafo com a distancia entre todos os pontos
    d = []
    for i in range(len(a)):
        aux = []
        for j in range(len(b)):
            aux.append(distance.euclidean((a[i],b[i]),(a[j],b[j])))
        d.append(aux)
        aux=[]
    return d

grafo = dist(x,y)

test = aco.ACO(grafo,2500)
caminho = test.mcaminho
print(test.hdistancia)
print(caminho)

i =[]
j=[]
for n in caminho:
    i.append(x[n])
    j.append(y[n])

plt.plot(x,y,'go')
plt.plot(i,j)

plt.show()