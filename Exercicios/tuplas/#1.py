top20 = ('America', 'Athletico', 'Atletico', 'Bahia', 'Botafogo', 'Corinthians', 'Coritiba', 'Cruzeiro', 'Cuiába', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio', 'Internacional', 'Palmeiras', 'Bragantino', 'Santos', 'São Paulo', 'Vasco')

while True: 
  print('-' * 30)
  menu = int(input(''' BRASILEIRÃO
[1] Os 5 primeiros colodados
[2] Últimos 4 colocados
[3] Ordem alfabética dos top 20
[4] Qual posição está o Chapecoense?
[5] SAIR
: '''))
  print('-' * 30)
  if menu == 1:
    top5 = (top20[0:5])
    for time in top5:
      print(time)
  if menu == 2:
    ult4 = (top20[-4:])
    for i, time in enumerate(ult4):
      posicao = len(top20) - len(ult4) + i + 1
      print(f'{posicao}° - {time}')
  if menu == 3:
    for i, time in enumerate(top20): #enumerate mostra o dado e a posição
      print(f'{f"{i + 1}°":^3} - {time}') 
  if menu == 4:
    Chapeco = str(input('Digite nome do seu time: '))
    if Chapeco in top20:
       posicao = top20.index(Chapeco) + 1
       print(f'O {Chapeco} está na {posicao}° posição no brasileirão')
    else: 
        print(f'O {Chapeco} não foi encontrado no top 20 brasileirão')
  if menu == 5:
    break