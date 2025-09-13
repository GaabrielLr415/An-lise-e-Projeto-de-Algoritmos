import numpy as np

def determina_moda(lista):
    mais_freq = 0
    moda = None
    for i in range(len(lista)):
        contagem = 0
        for j in range(len(lista)):
            if lista[j] == lista[i]:
                contagem += 1
        if contagem > mais_freq:
            mais_freq = contagem
            moda = lista[i]
    return moda

np.random.seed(0)
lista_teste_1 = (np.random.rand(100) * 50).astype(int).tolist()
lista_teste_2 = (np.random.randn(500) * 10).astype(int).tolist()
lista_teste_3 = (np.abs(np.random.randn(800)) * 5).astype(int).tolist()

moda1 = determina_moda(lista_teste_1)
moda2 = determina_moda(lista_teste_2)
moda3 = determina_moda(lista_teste_3)

print(f'Moda 1 = {moda1},', end=' ')
print(f'moda real = {max(lista_teste_1, key=lista_teste_1.count)}')

print(f'Moda 2 = {moda2},', end=' ')
print(f'moda real = {max(lista_teste_2, key=lista_teste_2.count)}')

print(f'Moda 3 = {moda3},', end=' ')
print(f'moda real = {max(lista_teste_3, key=lista_teste_3.count)}')