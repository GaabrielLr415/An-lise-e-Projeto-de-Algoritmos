import numpy as np

def string_sort(lista):
    pares = []
    for i in range(len(lista)):
        s = lista[i]
        pares.append([len(s), s])

    for i in range(len(pares)):
        for j in range(len(pares) - 1):
            a = pares[j]
            b = pares[j + 1]
            if a[0] > b[0] or (a[0] == b[0] and a[1] > b[1]):
                pares[j] = b
                pares[j + 1] = a

    for i in range(len(lista)):
        lista[i] = pares[i][1]

letras = list('abcdefghijklmnopqrstuvwxyz')
np.random.seed(0)
strings_teste_1 = [''.join([np.random.choice(letras) for _ in range(np.random.randint(10, 50))]) for i in range(10)]
strings_teste_2 = [''.join([np.random.choice(letras) for _ in range(int(i**(1.2)) + 5)]) for i in range(20)]
strings_teste_3 = [''.join([np.random.choice(letras) for _ in range(3 + (i % 10))]) for i in range(50)]

strings_teste_1_original = strings_teste_1.copy()
strings_teste_2_original = strings_teste_2.copy()
strings_teste_3_original = strings_teste_3.copy()

string_sort(strings_teste_1)
string_sort(strings_teste_2)
string_sort(strings_teste_3)

print(f'Lista 1 está corretamente ordenada? {strings_teste_1 == sorted(strings_teste_1_original, key=lambda s: (len(s), s))}')
print(f'Lista 1 está corretamente ordenada? {strings_teste_2 == sorted(strings_teste_2_original, key=lambda s: (len(s), s))}')
print(f'Lista 1 está corretamente ordenada? {strings_teste_3 == sorted(strings_teste_3_original, key=lambda s: (len(s), s))}')