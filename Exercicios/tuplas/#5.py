tupla = 'Casa', 'Carro', 'Rua', 'Cidade', 'Apartamento'
for palavra in tupla:
    vogais = []
    for letra in palavra:
        if letra.lower() in 'aeiou':
          vogais.append(letra)
    print(f'Na palavra {palavra} temos: {" ".join(vogais):<30}')