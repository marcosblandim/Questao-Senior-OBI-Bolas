def mais_de_cinco(contador):
	'''
	confere se ao menos 
	uma bola apareceu 
	5 ou mais vezes
	'''
	true_ou_false = map(lambda bola: True if contador[bola] >= 5 else False, contador)
	return any(true_ou_false)	

bolas = input().split(' ')
contador = dict() # {numero da bola : quantas vezes apareceu}
for bola in bolas:
	contador[bola] = contador.get(bola, 0) + 1
print('N' if mais_de_cinco(contador) else 'S')
