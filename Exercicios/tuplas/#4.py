listagem = 'Computador', 2500, 'Celular', 1700, 'Tablet', 900, 'Ipod', 500, 'Mouse', 25

produtos = []
for i in range(0, len(listagem), 2):
    produto = (listagem[i], listagem[i+1])
    produtos.append(produto)
print('-'*30)
print('{:^30}'.format('LISTAGEM DE PREÇOS'))
print('-'*30)
for produto in produtos:
    print(f'{produto[0]:.<20}R$ {produto[1]:>7.2f}')
print('-'*30)