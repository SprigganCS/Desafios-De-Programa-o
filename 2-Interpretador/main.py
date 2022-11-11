nprogramas = int(input())
temp = input()  #blank line

for i in range(nprogramas):
	register = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	instructions = " "
	k = 0
	ram = [0] * 1000
	for r in register:
		register[r] = 0
	for m in ram:
		ram[m] = 0

	while instructions != '100':
		instructions = input()
		ram[k] = instructions
		k += 1

	j = 0
	cont = 1

	while j < len(ram):

		x = ram[j]
		#print(x)
		a = int(x[0])
		b = int(x[1])
		c = int(x[2])

		if a == 1:
			cont = cont + 1
			j = j + 1
			break
		elif a == 2:
			register[b] = c
			cont = cont + 1
			j = j + 1

		elif a == 3:
			register[b] = int(register[b]) + int(c)
			register[b] %= 1000
			cont = cont + 1
			j = j + 1

		elif a == 4:
			register[b] *= c
			register[b] %= 1000
			cont = cont + 1
			j = j + 1

		elif a == 5:
			register[b] = register[c]
			cont = cont + 1
			j = j + 1

		elif a == 6:
			register[b] += register[c]
			register[b] %= 1000
			cont = cont + 1
			j = j + 1

		elif a == 7:
			register[b] *= register[c]
			register[b] %= 1000
			cont = cont + 1
			j = j + 1

		elif a == 8:
			register[b] = ram[register[c]]
			cont = cont + 1
			j = j + 1

		elif a == 9:
			ram[register[c]] = register[b]
			cont = cont + 1
			j = j + 1

		elif a == 0:
			if register[c] == 0:
				j = j + 1
				cont = cont + 1
				break
			else:
				j = j + 1
				j = register[b]
				cont = cont + 1
	print(cont, "\n")  #printa a quantidade de endereços processados
	try:
		aux = input()
	except EOFError as e:
			break

	#read until hits empty line
	while len(aux) == 3:
		try:
			aux = input()
		except EOFError as e:
			break
