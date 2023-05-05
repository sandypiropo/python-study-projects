lista_metas = []
contador = 1
continuar = True

print('{:=^20}'.format(' Escreva suas metas '))

while continuar:
    meta = input(f'Digite sua meta n°{contador}: ')
    lista_metas.append(meta)
    contador += 1
    mais_metas = input('Continua? [S/N]').upper().strip()[0]
    if mais_metas != 'S':
        continuar = False

print('{:=^20}'.format(' CHECK LIST '))
for i, meta in enumerate(lista_metas, start=1):
    print(f'{i}° = {meta}')
print(f'Total de metas = {len(lista_metas)}')
