import random

numeros = random.sample(range(1, 11), 5)
t_numeros = tuple(numeros)
t_ordenada = sorted(t_numeros)
numeros_str = map(str, t_numeros)
print(f'Números sorteados: {" - ".join(numeros_str)}')
print(f'O menor numero sorteado foi {t_ordenada[0]}')
print(f'O maior numero sorteado foi {t_ordenada[-1]}')