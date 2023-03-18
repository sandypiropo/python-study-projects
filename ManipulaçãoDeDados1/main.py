# Aprendendo a manipular dados

# Escrevendo
file = open('poem.txt', 'w+')
file.write('XVII\n')
file.write('I do not love you as if you were salt-rose, or topaz\n')
file.write('or the arrow of carnations the fire shoots off\n')
file.write('I love you as certain dark things are to be loved\n')
file.write('in secret, between the shadow and the soul.\n')

# Lendo
file.seek(0)
with open('poem.txt', 'r') as file:
    print(file.read())

# Calculando numero de linhas
with open('poem.txt', 'r') as file:
    linhas = file.readlines()
    num_linhas = len(linhas)
    print('Número de linhas:', num_linhas)

file.close()
