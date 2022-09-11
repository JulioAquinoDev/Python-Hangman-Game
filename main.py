import os
from time import sleep

def header():
    print('\n\t********************')
    print('\t**                **')
    print('\t**  Hangman game  **')
    print('\t**                **')
    print('\t********************')

def menu():
    print('\n\t(1) Start')
    print('\t(2) Exit')

while True:
	os.system("cls")
	header()
	menu()
	op = input('\tSelect a option: ')

	# star game
	if op == '1':

		lista_secreta = []
		lista_exibida = []
		letras_acertadas = []
		letras_erradas = []

		acertou = False
		enforcou = False
		erros = 0
		acertos = 0

		os.system("cls")
		palavra_secreta = input('\n\tSecret word:')

		os.system("cls")
		dica = input('\n\tClue: ')

		tam = len(palavra_secreta)
		secreta = palavra_secreta.upper()

		for i in secreta:
			lista_secreta.append(i)

		for i in lista_secreta:
			lista_exibida.append("-")
		
		while acertou == False and enforcou == False :
			os.system("cls")

			# This command block to be removing empty space.
			# If secret word more of a word.
			aux = 0
			for i in lista_secreta:
				x = i
				if i == " ":
					lista_exibida[aux] = " "
				aux += 1

			count_exibida = lista_exibida.count("-")
			count_espace = lista_exibida.count(" ")
			tam_total = tam - count_espace

			print ("\n\tHits: " + str(acertos))
			print ("\tError: " + str(erros))
			print ("\tClue: " + dica)
			print ("\t"+ str(tam_total) + " Letters")
			print("\n\tWrong: " + str(letras_erradas) + "\n")
			
			if erros == 0:
				print("\t __________")
				print("\t|          |")
				print("\t|")
				print("\t|")
				print("\t|")
				print("\t|")
				print("\t|")
				print("\t|")
				print("\t|")
				print("\t|")
				print("\t|")

			if erros == 1:
				print("\t __________")
				print("\t|          |")
				print("\t|         ,,,")
				print("\t|        ('.')")
				print("\t|")
				print("\t|")
				print("\t|")
				print("\t|")
				print("\t|")
				print("\t|")
				print("\t|")

			if erros == 2:
				print("\t __________")
				print("\t|          |")
				print("\t|         ,,,")
				print("\t|        ('.')")
				print("\t|         /|")
				print("\t|        / |")
				print("\t|")
				print("\t|")
				print("\t|")
				print("\t|")
				print("\t|")

			if erros == 3:
				print("\t __________")
				print("\t|          |")
				print("\t|         ,,,")
				print("\t|        ('.')")
				print("\t|         /|\\")
				print("\t|        / | \\")
				print("\t|")
				print("\t|")
				print("\t|")
				print("\t|")
				print("\t|")

			if erros == 4:
				print("\t __________")
				print("\t|          |")
				print("\t|         ,,,")
				print("\t|        ('.')")
				print("\t|         /|\\")
				print("\t|        / | \\")
				print("\t|          |")
				print("\t|         /-")
				print("\t|        /   ")
				print("\t|       /     ")
				print("\t|")

			if erros == 5:
				print("\t __________")
				print("\t|          |")
				print("\t|         ,,,")
				print("\t|        ('.')")
				print("\t|         /|\\")
				print("\t|        / | \\")
				print("\t|          |")
				print("\t|         /-\\")
				print("\t|        /   \\")
				print("\t|       /     \\")
				print("\t|")

			print("\t| " + ' '.join(map(str, lista_exibida)))
			chute = input('\n\tEnter a letter: ')
			chute_up = chute.upper()
			count = 0

			for i in lista_secreta:
				letra = i
				if chute_up == letra and lista_exibida[count] == "-":
					lista_exibida[count] = chute_up
					acertos += 1
				count +=1

			count_2_exibida = lista_exibida.count("-")

			if count_exibida == count_2_exibida:
				letras_erradas.append(chute_up)
				erros +=1

			if acertos == tam_total:
				os.system("cls")
				print('\n\tYou Won..')
				print("\tWord: " + ' '.join(map(str, lista_exibida)))
				print ("\tHits: " + str(acertos))
				print ("\tError: " + str(erros))
				sleep(5)
				acertou = True

			if erros == 5:
				sleep(2)				
				os.system("cls")
				print('\n\tYou Lose..')
				print("\tWord: " + ' '.join(map(str, lista_secreta)))
				print("\tWord: " + ' '.join(map(str, lista_exibida)))
				print ("\tHits: " + str(acertos))
				print ("\tError: " + str(erros))
				sleep(5)
				enforcou = True

	# exit
	elif op == '2':
		os.system("cls")
		print('\n\tGoing out...')
		sleep(2)
		break

	else:
		os.system("cls")
		print('\n\tTry again!')
		sleep(3)