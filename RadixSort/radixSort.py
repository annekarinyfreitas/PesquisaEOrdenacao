from random import randint
from timeit import timeit
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as interpolate

tamanhos = [1000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
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
    lista.append(tam - i)

  return lista

# Ordena pelo metodo do Radix Sort
def radixSort(lista):
    buckets = [[] for _ in range(10)]

    if lista:
        valorMaximoLista = max(lista)
        decimal = 1

        while valorMaximoLista > decimal:
            for num in lista:
                buckets[(num//decimal) % 10].append(num)

            decimal = decimal * 10

            lista = []
            for i in range(10):
                lista.extend(buckets[i])
                buckets[i] = []

    return lista

# Calcula quanto tempo leva para ordenar cada lista
for i in range(len(tamanhos)):
  lista = geraListaDecrescente(tamanhos[i]) #pior caso
  #lista = geraListaAleatoria(tamanhos[i]) #caso medio
  tempo = timeit("radixSort({})".format(lista),setup="from __main__ import radixSort",number=1)
  tempos.append(tempo)
  #print(lista)
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
    plt.title('Pior Caso', fontsize=18)
    fig.savefig('pior caso.png')

# Desenha grafico
x = tamanhos
y = tempos
desenhaGraficoSuaveRepl(x,y)