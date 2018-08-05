from random import randint
from timeit import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as interpolate

tamanhos = [1000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
#tamanhos = [5, 10, 15]
tempos = []


# Gera uma lista aleatoria de um determinado tamanho
def geraListaAleatoria(tam):
    lista = []
    while (len(lista) != tam):
        n = randint(1, 1 * tam)
        lista.append(n)
    return lista


# Gera uma lista decrescente de um determinado tamanho
def geraListaDecrescente(tam):
    lista = []
    for i in range(tam):
        lista.append(tam - i)
    return lista


# Ordena uma lista por Bubble Sort
def bubbleSort(lista):
    teveTroca = False
    for num in range(len(lista) - 1):
        for i in range(num, len(lista) - 1, 1):
            if lista[i] > lista[i + 1]:
                temp = lista[i + 1]
                lista[i + 1] = lista[i]
                lista[i] = temp
                teveTroca = True

    if teveTroca == True:
        bubbleSort(lista)
    else:
        return lista
    return lista


# Gera o grafico de tamanhos x tempos
mpl.use('Agg')


def desenhaGraficoSuave(x, y, xl="Nº de Elementos", yl="Tempo(s)"):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    xnew = np.linspace(min(x), max(x), 10 * (max(x) - min(x)))
    a, b, c = interpolate.splrep(x, y, s=0, k=2)
    suave = interpolate.BSpline(a, b, c, extrapolate=False)
    plt.plot(xnew, suave(xnew))
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.title('Pior caso', fontsize=18)
    fig.savefig('pior.png')


# Calcula quanto tempo leva para ordenar
def calculaTempos():
    for i in range(len(tamanhos)):
        lista = geraListaDecrescente(tamanhos[i]) #Pior caso
        # lista = geraAleatoria(tamanhos[i]) #Caso medio
        tempo = timeit(
            "bubbleSort({})".format(lista),
            setup="from __main__ import bubbleSort",
            number=1)
        tempos.append(tempo)
        #print(lista)
        print(tamanhos[i])
        print(tempo)


# Main
calculaTempos()
x = tamanhos
y = tempos
desenhaGraficoSuave(x, y)
