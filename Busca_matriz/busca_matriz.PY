import numpy as np

def busca_matriz(matriz, elemento):
    for i in range(len(matriz)):
        linha = matriz[i]
        for j in range(len(linha)):
            if linha[j] == elemento:
                return (i, j)
    return None

np.random.seed(0)
matriz_teste_1 = (np.random.rand(100, 100) * 5000000).astype(int).tolist()
elemento_teste_1 = 362
matriz_teste_2 = (np.random.randn(50, 20) * 10000).astype(int).tolist()
elemento_teste_2 = 30196
matriz_teste_3 = (np.abs(np.random.randn(100, 8)) * 5000).astype(int).tolist()
elemento_teste_3 = 14620
matriz_teste_4 = (np.abs(np.random.randn(100, 8)) * 5000).astype(int).tolist()
elemento_teste_4 = -10

linha_coluna_1 = busca_matriz(matriz_teste_1, elemento=elemento_teste_1)
linha_coluna_2 = busca_matriz(matriz_teste_2, elemento=elemento_teste_2)
linha_coluna_3 = busca_matriz(matriz_teste_3, elemento=elemento_teste_3)
linha_coluna_4 = busca_matriz(matriz_teste_4, elemento=elemento_teste_4)

print(f'Índices do elemento {elemento_teste_1} na matriz 1 = {linha_coluna_1},',
      end=' ')
print(f'índices reais = {next(((int(i), int(j)) for i, j in zip(*np.where(np.array(matriz_teste_1) == elemento_teste_1))), None)}')

print(f'Índices do elemento {elemento_teste_2} na matriz 2 = {linha_coluna_2},',
      end=' ')
print(f'índices reais = {next(((int(i), int(j)) for i, j in zip(*np.where(np.array(matriz_teste_2) == elemento_teste_2))), None)}')

print(f'Índices do elemento {elemento_teste_3} na matriz 3 = {linha_coluna_3},',
      end=' ')
print(f'índices reais = {next(((int(i), int(j)) for i, j in zip(*np.where(np.array(matriz_teste_3) == elemento_teste_3))), None)}')

print(f'Índices do elemento {elemento_teste_4} na matriz 4 = {linha_coluna_4},', end=' ')
print(f'índices reais = None')