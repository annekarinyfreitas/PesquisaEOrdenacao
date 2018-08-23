from random import randint
from timeit import timeit
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as interpolate

#tamanhos = [1000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]
tamanhos = [1000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
#tamanhos = [10, 100, 1000]
tempos = []
numOperacoes = []
numOperacoesFunc = 0

# Gera lista aleatoria de um determinado tamanho
def geraListaAleatoria(tam):
    lista = []
    while(len(lista) != tam):
        n = randint(1,1*tam)
        lista.append(n)
            return lista

# Gera lista decrescente de um determinado tamanho
def geraListaDecrescente(tam):
    lista = []
    for i in range(tam):
        lista.append(tam - i)
            
            return lista

# Ordenacao pelo metodo do Shell Sort
def shellSort(lista):
    global numOperacoesFunc
    n = len(lista)
    distancia = n // 2
    
    while distancia > 0:
        for i in range(distancia,n):
            numComparacao = lista[i]
            x = i
            while x >= distancia and lista[x - distancia] > numComparacao:
                numOperacoesFunc += 1
                lista[x] = lista[x - distancia]
                x -= distancia
            
            lista[x] = numComparacao
        
        distancia = distancia // 2
    return lista

# Calcula quanto tempo leva para ordenar cada lista
for i in range(len(tamanhos)):
    lista = geraListaDecrescente(tamanhos[i]) #pior caso
    #lista = geraListaAleatoria(tamanhos[i]) #caso medio
    tempo = timeit("shellSort({})".format(lista),setup="from __main__ import shellSort",number=1)
        tempos.append(tempo)
        numOperacoes.append(numOperacoesFunc)
        numOperacoesFunc = 0
            #print("Lista Tamanhos Tempo Numero de Operacoes")
            #print(lista)
            print(tamanhos[i])
            print(tempo)
            print(numOperacoes[i])


# Gera o grafico de tamanhos x tempos
def desenhaGraficoSuaveRepl1(x,y,xl = "Nº de Elementos", yl = "Tempo(s)"):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    xnew = np.linspace(min(x), max(x), 10 * (max(x) - min(x)))
    a, b, c = interpolate.splrep(x, y, s=0, k=2)
    suave = interpolate.BSpline(a, b, c, extrapolate=False)
    plt.plot(xnew, suave(xnew), label="Suave")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.title('Pior caso - Elementos', fontsize=18)
    fig.savefig('pce.png')

# Gera o grafico de tamanhos x numOperacoes
def desenhaGraficoSuaveRepl2(x,y,xl = "Nº de Operações", yl = "Tempo(s)"):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    xnew = np.linspace(min(x), max(x), 10 * (max(x) - min(x)))
    a, b, c = interpolate.splrep(x, y, s=0, k=2)
    suave = interpolate.BSpline(a, b, c, extrapolate=False)
    plt.plot(xnew, suave(xnew), label="Suave")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.title('Pior caso - Operacoes', fontsize=18)
    fig.savefig('pco.png')


# Desenha grafico tempos
x = tamanhos
y = tempos
desenhaGraficoSuaveRepl1(x,y)

# Desenha grafico operacoes
x = tamanhos
y = numOperacoes
desenhaGraficoSuaveRepl2(x,y)
