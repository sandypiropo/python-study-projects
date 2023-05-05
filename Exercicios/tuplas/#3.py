numeros = []
for i in range(4):
    numeros.append(int(input(f'Digite o {i+1}º número: ')))
tupla = tuple(numeros)
print(f'Você digitou os valores: {tupla}')  
if 3 in tupla:
    num3 = tupla.index(3) + 1
    print(f'O valor 3 apareceu na {num3}° posição')
else:
   print(f'O valor 3 não foi citado')
num9 = tupla.count(9)
if 9 in tupla:
    print(f'O valor 9 apareceu {num9} vezes')
else:
    print('O valor 9 não foi citado')
pares = []
for valor in tupla:
    if valor % 2 == 0:
        pares.append(valor)
print(f'Os valores pares digitados foram: {", ".join(str(x) for x in pares)}')
