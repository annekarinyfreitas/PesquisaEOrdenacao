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

def controiMaxHeap(final, atual):   
  noEsquerda = 2 * atual + 1  
  noDireita = 2 * (atual + 1)   
  valorMaximoHeap = atual  

  if noEsquerda < final and lista[atual] < lista[noEsquerda]:   
    valorMaximoHeap = noEsquerda   
  if noDireita < final and lista[valorMaximoHeap] < lista[noDireita]:   
    valorMaximoHeap = noDireita   
  if valorMaximoHeap != atual:   
    lista[atual], lista[valorMaximoHeap] = lista[valorMaximoHeap], lista[atual]
    controiMaxHeap(final, valorMaximoHeap)   

# Ordena pelo metodo do Heap Sort
def heapSort(lista):     
  tamanho = len(lista)   
  comeco = (tamanho // 2) - 1
    
  for i in range(comeco, -1, -1):   
     controiMaxHeap(tamanho, i)   
     
  for i in range(tamanho-1, 0, -1):   
    lista[i], lista[0] = lista[0], lista[i]  
    controiMaxHeap(i, 0)

# Calcula quanto tempo leva para ordenar cada lista
for i in range(len(tamanhos)):
  #lista = geraListaDecrescente(tamanhos[i]) #pior caso
  lista = geraListaAleatoria(tamanhos[i]) #caso medio
  tempo = timeit("heapSort({})".format(lista),setup="from __main__ import heapSort",number=1)
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
    plt.title('Caso medio', fontsize=18)
    fig.savefig('caso medio.png')

# Desenha grafico
x = tamanhos
y = tempos
desenhaGraficoSuaveRepl(x,y)