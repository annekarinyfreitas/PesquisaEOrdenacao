from random import randint
from timeit import timeit
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as interpolate

#tamanhos = [1000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]
tamanhos = [1000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
#tamanhos = [5, 10, 15]
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

# Ordenacao pelo metodo do Quick Sort
def quickSort(lista):
    if len(lista) <= 1:
        return lista
    
    pivo = lista[len(lista)//2]
    maiores = []
    menores = []
    igual = []
    
    for i in range(len(lista)):
        if lista[i]>pivo:
            maiores.append(lista[i])
        if lista[i]<pivo:
            menores.append(lista[i])
        if lista[i]==pivo:
            igual.append(lista[i])
    
    return quickSort(menores) + igual + quickSort(maiores)

# Calcula quanto tempo leva para ordenar cada lista
for i in range(len(tamanhos)):
  lista = geraListaDecrescente(tamanhos[i]) #pior caso
  #lista = geraListaAleatoria(tamanhos[i]) #caso medio
  tempo = timeit("quickSort({})".format(lista),setup="from __main__ import quickSort",number=1)
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
    plt.title('Pior caso', fontsize=18)
    fig.savefig('pior caso.png')

# Desenha grafico
x = tamanhos
y = tempos
desenhaGraficoSuaveRepl(x,y)
