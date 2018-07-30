# Estou fazendo esse programinha porque gosto bastante de Pokemon, é baseado no Fire Red.
print('Olá! É um prazer conhecê-lo!\nBem-vindo ao MUNDO POKEMON.Meu nome é Professor Oak')
input('Professor Oak - Agora me fale sobre você, você é garoto ou garota(M/F)? ')
nome = input('Tudo bem!\nInforme seu nome: ')
neto = input('Professor Oak - Esse é meu neto.\nProfessor Oak - Ele tem sido seu rival desde pequeno, mas esqueci o nome dele, me informe por favor: ')
print(f'Professor Oak - Tudo pronto!\nProfessor Oak - Agora sua jornada Pokemon começa!!\nJovem - Ei {nome} vá até o laboratório do Professor Oak, ele tem uma surpresa.\nProfessor Oak - Olá {nome}, vi que você e {neto} estão me esperando!\n{neto} - Estou farto de esperar!\nProfessor Oak - Tenho 3 pokemons aqui e quero que vocês escolham entre eles.')
def escolha():
	pokemon = input('Entre "c" para escolher Charmander(FOGO), "s" para escolher Squirtle(ÁGUA), "b" para escolher Bulbasaur(FOLHA) ou "q" para sair: ')
	while pokemon != 'q':
		if pokemon == 'c':
			pokemon_charmander()
		elif pokemon == 's':
			pokemon_squirtle()
		elif pokemon == 'b':
			pokemon_bulbasaur()
		else:
			print('Comando incorreto\nTente novamente!!')
		pokemon = input('Entre "c" para escolher Charmander(FOGO), "s" para escolher Squirtle(ÁGUA), "b" para escolher Bulbasaur(FOLHA) ou "q" para sair: ')

def pokemon_charmander():
	print(f'Professor Oak - {nome} escolheu Charmander, espero que você cuide bem dele!\n{neto} escolheu Squirtle!')
	
def pokemon_squirtle():
	print(f'Professor Oak - {nome} escolheu Squirtle, espero que você cuide bem dele!\n{neto} escolheu Bulbasaur!')

def pokemon_bulbasaur():
	print(f'Professor Oak - {nome} escolheu Bulbasaur, espero que você cuide bem dele!\n{neto} escolheu Charmander!')

escolha()
