def countingSortModificado(lista):
  dicionarioContador = {}
  listaOrdenada = []

  # Verifica se cada chave existe no dicionario, se existir soma +1
  for num in lista:
    if num in dicionarioContador:
      dicionarioContador[num] += 1
    else:
      dicionarioContador[num] = 1

  print(dicionarioContador)

  # Itera as chaves de forma ordenada
  for chave in sorted(dicionarioContador):
    numVezes = dicionarioContador[chave]

    # Adiciona no array de ordenadas a chave quantas vezes ela apareceu no array original 
    for _ in range(numVezes):
      listaOrdenada.append(chave)

  return listaOrdenada