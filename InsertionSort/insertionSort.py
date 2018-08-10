from random import randint
from timeit import timeit
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as interpolate

tamanhos = [1000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]
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

# Ordenacao pelo metodo do Insertion Sort
def insertionSort(lista):
  for i in range (1, len(lista), 1):
      pivo = lista[i]
      indicePivo = i
      for j in range (i-1, -1, -1):
        anterior = lista[j]
        #print("pivo", pivo, " anterior", anterior)
        if pivo<anterior:
            #print("troca")
            temp = lista[j]
            lista[j] = lista[indicePivo]
            lista[indicePivo] = temp
            indicePivo = j
  return lista

# Calcula quanto tempo leva para ordenar cada lista
for i in range(len(tamanhos)):
  lista = geraListaDecrescente(tamanhos[i]) #pior caso
  tempo = timeit("insertionSort({})".format(lista),setup="from __main__ import insertionSort",number=1)
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
    fig.savefig('grafico.png')

# Desenha grafico
x = tamanhos
y = tempos
desenhaGraficoSuaveRepl(x,y)
