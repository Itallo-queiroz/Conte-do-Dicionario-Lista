# tupla
chaves = ('Nome', 'Idade', 'Profissão') 

# lista de dicionarios
usuarios = [
    {
        chaves[0]: 'Itallo',
        chaves[1]: 17,
        chaves[2]: 'Programador',

    },
    {
        'Nome': 'Isabella',
        'Idade': 15,
        'Profissão': 'Medica',
    },
    {
        'Nome': 'Estefany',
        'Idade': 12,
        'Profissão': 'Empresaria',
    }

]

# Mostra a lisata de usuario
print(f'\n{'='*10} LISTA DE USUARIOS {'='*10}\n')

for usuario in usuarios:
    for chave in chaves:
        print(f'{chave}: {usuario[chave]}')

    print(f'\n{'-'*10}\n')

# adicionando novo usuario
usuario = {}

# adicionar novo dicionario á lista
for i in range(len(chaves)):
    usuario[chaves[i]] = input(f'Informe {chaves[i]}: ')

usuarios.append(usuario)
print(f'\nUsuário cadrastado com sucesso!')

# Reexibindo a nova lista de usuarios
print(f'\n{'='*10} LISTA DE USUARIOS {'='*10}\n')

for usuario in usuarios:
    for chave in chaves:
        print(f'{chave}: {usuario[chave]}')

    print(f'\n{'-'*10}\n')
