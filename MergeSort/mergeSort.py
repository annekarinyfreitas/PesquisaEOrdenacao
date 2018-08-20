from random import randint
from timeit import timeit
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as interpolate

tamanhos = [1000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
#tamanhos = [5]
tempos = []

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
    lista.append(tam -i)

  return lista

# Ordenacao pelo metodo do Merge Sort
def mergeSort(lista):
    i=0
    j=0
    k=0

    tamanhoLista = len(lista)

    if tamanhoLista > 1:
      metade = tamanhoLista//2
      medateDireita = lista[metade:tamanhoLista]
      medateEsquerda = lista[0:metade]

      tamanhoDireita = len(medateDireita)
      tamanhoEsquerda = len(medateEsquerda)

      mergeSort(medateDireita)
      mergeSort(medateEsquerda)

      while i < tamanhoEsquerda and j < tamanhoDireita:
        if medateEsquerda[i] < medateDireita[j]:
          lista[k] = medateEsquerda[i]
          i += 1
        else:
          lista[k] = medateDireita[j]
          j += 1
        k += 1

      while i < tamanhoEsquerda:
        lista[k] = medateEsquerda[i]
        i += 1
        k += 1

      while j < tamanhoDireita:
        lista[k]=medateDireita[j]
        j += 1
        k += 1

    return lista


# Calcula quanto tempo leva para ordenar cada lista
for i in range(len(tamanhos)):
  lista = geraListaDecrescente(tamanhos[i]) #pior caso
  tempo = timeit("mergeSort({})".format(lista),setup="from __main__ import mergeSort",number=1)
  tempos.append(tempo)
  print(tamanhos[i])
  print(tempo)


# Gera o grafico de tamanhos x tempos
def desenhaGraficoSuaveRepl(x,y,xl = "Nº de Elementos", yl = "Tempo(s)"):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    xnew = np.linspace(min(x), max(x), 10 * (max(x) - min(x)))
    a, b, c = interpolate.splrep(x, y, s=0, k=2)
    suave = interpolate.BSpline(a, b, c, extrapolate=False)
    plt.plot(xnew, suave(xnew), label="Suave")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.title('Pior caso', fontsize=18)
    fig.savefig('grafico-piorcaso.png')

# Desenha grafico
x = tamanhos
y = tempos
desenhaGraficoSuaveRepl(x,y)
