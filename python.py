#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Couleurs
VERT="\033[1;32m"
NORMAL="\033[0;39m"
ROUGE="\033[1;31m"
ROSE="\033[1;35m"
BLEU="\033[1;34m"
BLANC="\033[0;02m"
BLANCLAIR="\033[1;08m"
JAUNE="\033[1;33m"
CYAN="\033[1;36m"

#MODULES
import time  

#FONCTIONS

def fdebug(message) :
	global debug
	if "d" in debug :
		print (JAUNE + "DEBUG : " + message + NORMAL )
		
def ferror(message) :
	global debug
	if "d" in debug :
		print (ROUGE + "ERREUR : " + message + NORMAL)
		
def generateur(presence) : # a si le ficher et present, w sinon
	global cible
	global nom
	global type
	pasdefichier = open(cible + ".txt", presence) # Ouvre le fichier
	fdebug("Ouvert / cree le fichier")
	if type is "a" :
		pasdefichier.write(time.strftime('%d/%m/%y %H:%M',time.localtime()) + " *** " + raw_input (VERT + "Entre l'action que tu as effectué(e) >>>" + NORMAL) + "(" + nom + ")"+ "\n")
	else : 
		pasdefichier.write(time.strftime('%d/%m/%y %H:%M',time.localtime()) + " >>> " + raw_input (VERT + "Entre le commentaire que tu as effectué(e) >>>" + NORMAL) + " (" + nom + ")"+ "\n")
	fdebug("Enregistrement dans le fichier")
	pasdefichier.close() # Je ferme la porte derriere mon fichier
	
def lecteur() :
	fdebug("Lecture des questions")
	global cible
	fichier = open(cible + ".txt", "r")
	fdebug ("Ouverture du fichier")
	print (ROSE + "Cette cible est déja connu des forces de polices ..." + NORMAL)
	print (ROSE + "Impression du casier judiciaire\n\n" + NORMAL)
	fdebug("Lecture du fichier")
	for ligne in fichier :
		print (ROUGE + ligne + NORMAL)
		fdebug("Ligne lue")
	fichier.close()
#MAIN

debug = raw_input (VERT + "Tape 0 pour lancer le programme >>>" + NORMAL)
fdebug("Initialisation")


fdebug("Demande du pseudo ")
nom = raw_input (VERT + "Bonjour ! Entre ton pseudo ! >>>" + NORMAL)
fdebug("""Enregistrement du pseudo dans la variable "Nom" """)
print(VERT + "Bonjour " + nom + NORMAL)
fdebug("Boucle initialisée")
if "l" in debug :
	fdebug("Lecture du fichier")
	quitter = "c"
	while quitter is not "q" :
		cible = raw_input(VERT + "De qui veut tu lire les remarques ? >>>" + NORMAL)
		try :
			fichier = open( cible + ".txt", "r" )
		except IOError:
			ferror("fichier introuvable")
			continuer = raw_input (VERT + "Veut tu generer le fichier ? (o/n)" + NORMAL)
			fdebug("Reponse enregistrée")
			if "o" in continuer :
				fdebug ("Oui !")
				type = raw_input(VERT + "Veut tu faire une a(ction) ou un c(ommentaire) ? >>>" + NORMAL)
				generateur("w")
				fdebug("Generation finie")
				print(VERT + "Remarque ajoutée !" + NORMAL)
				print ("\n\n\n")
			else :
				fdebug ("non")
				print (ROUGE + "fichier introuvable !" +  NORMAL)
				quiter = "q"
		else :
			lecteur()
	
while "1" == "1" :
	fdebug("Demande du nom de la personne cible")
	cible = raw_input ( VERT + "Quel est le nom de la personne cible ? >>>" + NORMAL )
	fdebug ("""Enregistrement la cible dans la variable "cible". """)
	
	fdebug("Test de presence du fichier pour la lecture")
	try:
		fichier = open( cible + ".txt", "r") # TEST Ouvre le fichier
	except IOError:
		fdebug("fichier introuvable")
	else :
		fdebug ("Fichier trouvé")
		lecteur()
	
	fdebug("demande du type d'ajout")
	type = raw_input(VERT + "Veut tu faire une a(ction) ou un c(ommentaire) ? >>>" + NORMAL)
	if type is not "a" :
		fdebug("Ce n'est pas une action")
		if type is not "c" :
			fdebug("Ce n'est pas un commantaire")
			ferror("Pas de valeur correcte")
			print(ROUGE + "Tu n'as pas entrée une valeur correcte . Je pense donc que tu veux inscrire un commentaire" + NORMAL)
			fdebug("Mise de type a c")
			type = "c"
	
	fdebug("Test de presence en cours")
	
	try:
		fichier = open( cible + ".txt", "r") # TEST Ouvre le fichier
	except IOError:
		ferror("Le fichier n'existe pas")
		generateur("w")
	else :
		generateur("a")
	finally :
		fdebug("Generation finie")
		print(VERT + "Remarque ajoutée !" + NORMAL)
		print ("\n\n\n")
	
ferror("EOF !!")
#TODO
#PROGRAMME
