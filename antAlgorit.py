import random
import numpy as np

class Formiga():
    def __init__(self,n):
        self.posicao = n
        self.tabu = []
        self.dtuor = 0
        pass

    def mover(self,nvertices,feromonios,arestas):
        while nvertices>len(self.tabu):
            self.posicao = random.choices(range(nvertices),self.probabilidade(feromonios,arestas))[0]
            self.tabu.append(self.posicao)
            pass
        pass

    def marcar_rota(self,matriz,dferomonio):
        self.posicao = self.tabu[0]
        self.tabu.append(self.tabu[0])
        distancia = 0
        for d in range(len(self.tabu)-1):
            distancia += matriz[self.tabu[d]][self.tabu[d+1]]
            pass
        self.dtuor = distancia
        for f in range(len(self.tabu)-1):
            dferomonio[self.tabu[f]][self.tabu[f+1]] += 100/distancia
            dferomonio[self.tabu[f+1]][self.tabu[f]] += 100/distancia  # manter a matriz simetrica
            pass
        pass
    pass

    def probabilidade(self,feromonios,arestas):
        retorno = []
        soma = 0
        for f in range(len(arestas)):
            if arestas[f]!=0 and f not in self.tabu:
                soma += feromonios[f] * (1/arestas[f])**5
                pass
            pass
        for i in range(len(arestas)):
            if i in self.tabu:
                retorno.append(0)
            else:
                retorno.append(((1/arestas[i])**5)*feromonios[i]/soma)
            pass
        return retorno

class ACO():
    def __init__(self,grafo,ninteracoes=2500):
        self.hdistancia = []
        self.mcaminho = []
        self.best_distancia = None
        swarm = [Formiga(n) for n in range(len(grafo))]
        det_feromonio = np.array([[0]*len(grafo) for _ in range(len(grafo))])
        feromonio = np.array([[1]*len(grafo) for _ in range(len(grafo))])
        cont = 0
        while cont<ninteracoes:
            for f in swarm:
                f.tabu = [f.posicao]
                f.mover(len(grafo),feromonio[f.posicao],grafo[f.posicao])
                f.marcar_rota(grafo,det_feromonio)
                if self.best_distancia==None or f.dtuor<self.best_distancia:
                    self.best_distancia = f.dtuor
                    self.mcaminho = f.tabu
                    pass
            pass
            feromonio = 0.5*feromonio + det_feromonio
            det_feromonio = np.array([[0]*len(grafo) for _ in range(len(grafo))])
            cont+=1
            self.hdistancia.append(self.best_distancia)
        pass
    pass