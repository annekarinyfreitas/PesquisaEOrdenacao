from random import randint
from timeit import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as interpolate

tamanhos = [1000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000] 
#tamanhos = [5, 10, 15] 
tempos = [] 

# Gera uma lista aleatoria de um determinado tamanho
def geraListaAleatoria(tam):
  lista = []
  while(len(lista) != tam):
    n = randint(1,1*tam)
    lista.append(n)
  return lista

# Gera uma lista decrescente de um determinado tamanho
def geraListaDecrescente(tam):
  lista = []
  for i in range(tam):
      lista.append(tam-i)
  return lista

# Ordena uma lista por Selection Sort
def selectionSort(lista):
    for i in range(len(lista)-1):
      indiceMenorValor = i
      for j in range (i+1 , len(lista), 1):
        if lista[indiceMenorValor]>lista[j]:
          indiceMenorValor = j

      if lista[i] != lista[indiceMenorValor]:
        temp = lista[i]
        lista[i] = lista[indiceMenorValor]
        lista[indiceMenorValor] = temp
                
                
# Gera o grafico de tamanhos x tempos
mpl.use('Agg')
def desenhaGraficoSuave(x,y,xl = "Nº de Elementos", yl = "Tempo(s)"):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    xnew = np.linspace(min(x), max(x), 10 * (max(x) - min(x)))
    a, b, c = interpolate.splrep(x, y, s=0, k=2)
    suave = interpolate.BSpline(a, b, c, extrapolate=False)
    plt.plot(xnew, suave(xnew))
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.title('Caso Medio', fontsize=18)
    fig.savefig('medio.png')

 # Calcula quanto tempo leva para ordenar
def calculaTempos():
    for i in range(len(tamanhos)):
        lista = geraListaAleatoria(tamanhos[i])
        tempo = timeit("selectionSort({})".format(lista),setup="from __main__ import selectionSort",number=1)
        tempos.append(tempo)
        print(tamanhos[i])
        print(tempo)


# Main
calculaTempos()
x = tamanhos
y = tempos
desenhaGraficoSuave(x,y)
