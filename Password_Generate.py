#!/usr/bin/python3
import string
import random


## caractères à partir des caractères à partir des chiffres du mot de passe
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
	## longueur du mot de passe de l'utilisateur
	length = int(input("Entrez la longueur du mot de passe: "))

	## nombre de types de caractères
	alphabets_count = int(input("Entrez le nombre d'alphabets dans le mot de passe: "))
	digits_count = int(input("Entrez le nombre de chiffres dans le mot de passe: "))
	special_characters_count = int(input("Entrez le nombre de caractères spéciaux dans le mot de passe: "))

	characters_count = alphabets_count + digits_count + special_characters_count

	## vérifier la longueur totale avec le nombre de caractères
	## imprimer non valide si la somme est supérieure à la longueur
	if characters_count > length:
		print("Le nombre total de caractères est supérieur à la longueur du mot de passe")
		return


	## initialisation du mot de passe
	password = []


	## choisir des alphabets aléatoires
	for i in range(alphabets_count):
		password.append(random.choice(alphabets))


	## choisir des chiffres aléatoires
	for i in range(digits_count):
		password.append(random.choice(digits))


	## choisir des alphabets aléatoires
	for i in range(special_characters_count):
		password.append(random.choice(special_characters))


	## si le nombre total de caractères est inférieur à la longueur du mot de passe
	## ajouter des caractères aléatoires pour le rendre égal à la longueur
	if characters_count < length:
		random.shuffle(characters)
		for i in range(length - characters_count):
			password.append(random.choice(characters))


	## mélanger les personnages
	random.shuffle(characters)



	## sélection de caractères aléatoires dans la liste
	password = []
	for i in range(length):
		password.append(random.choice(characters))



	## mélanger le mot de passe résultant
	random.shuffle(password)

	## conversion de la liste en chaîne
	## impression de la liste
	print("".join(password))

## appel de la fonction
generate_random_password()