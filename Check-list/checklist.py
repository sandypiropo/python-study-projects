lista_metas = [] 
contador = 1
continuar = True
     
print('{:=^20}'.format(' Escreva suas metas '))

while continuar:
    meta = str(input(f'Digite sua meta n°{contador}: '))
    lista_metas.append(meta)  
    contador += 1
    mais_metas = str(input('Continua? [S/N]')).upper().strip()[0] 
    if mais_metas == 'N':
        break
     
print('{:=^20}'.format(' CHECK LIST '))
for cont, meta in enumerate(lista_metas):
    print(f'{cont + 1}° = {meta}')
print('Total de metas =', len(lista_metas))