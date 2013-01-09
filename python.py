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
	pasdefichier = open(cible + ".txt", presence) # Ouvre le fichier
	fdebug("Ouvert / cree le fichier")
	
	pasdefichier.write(time.strftime('%d/%m/%y %H:%M',time.localtime()) + " >>> " + raw_input (VERT + "Entre la remarque >>>" + NORMAL) + "(" + nom + ")"+ "\n")
	fdebug("Enregistrement dans le fichier")
	pasdefichier.close() # Je ferme la porte derriere mon fichier
#MAIN

debug = raw_input (VERT + "Tape 0 pour lancer le programme >>>" + NORMAL)
fdebug("Initialisation")


fdebug("Demande du pseudo ")
nom = raw_input (VERT + "Bonjour ! Entre ton pseudo ! >>>" + NORMAL)
fdebug("""Enregistrement du pseudo dans la variable "Nom" """)

fdebug("Boucle initialisée")
while "1" == "1" :
	print(VERT + "Bonjour " + nom + NORMAL)
	fdebug("Demande du nom de la personne cible")
	cible = raw_input ( VERT + "Quel est le nom de la personne cible ? >>>" + NORMAL )
	fdebug ("""Enregistrement la cible dans la variable "cible". """)
	
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
	
ferror("EOF !")
#TODO
#PROGRAMME
