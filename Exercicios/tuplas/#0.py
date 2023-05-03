tupla = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze'
numero = int(input('Digite um numero entre 0 e 20: '))
while numero < 0 or numero > 20:
  numero = int(input('Inválido. Digite um numero entre 0 e 20: '))
print(f'Você digitou o número {tupla[numero]}')
