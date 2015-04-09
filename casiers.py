#!/usr/bin/python
# -*- coding: UTF-8 -*-
print "------[DEMMARAGE!]------"

print "------[ LISTES ! ]------"
fonctions = []

#### IMPORTS ####
print "------[ IMPORTS !]------"

import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")
import os
import subprocess
from random import randrange
import time
import webbrowser
import platform
import urllib2
from config import *

#### FUNCTIONS ###
print "------[FUNCTONS!]------"

# Graphiques #


def progressbar():
	# setup toolbar
	sys.stdout.write("[%s]" % (" " * toolbar_width))
	sys.stdout.flush()
	sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

	for i in xrange(toolbar_width):
		time.sleep(60) # do real work here
		# update the bar
		sys.stdout.write("~")
		sys.stdout.flush()
	sys.stdout.write("\n")

def printinfo(text):

	text = str(text)
	print( "[" + info + "] " + text)

def printok(text):
	text = str(text)
	print(VERT + "[" + ok + "] " + NORMAL + text)
	
def printerror(text):
	text = str(text)
	print(ROUGE + "[" + error + "] " + NORMAL + text)

def printfatal(text):
	text = str(text)
	print(ROUGE + "[" + fatalerror + "] " + NORMAL + text)
	sys.exit(2)

def printdebug(text):
	if debugactivated == True:
		text = str(text)
		print(JAUNE + "[" + debug + "] " + NORMAL + text)
	else:
		return 0
			
def clearscreen():
	if platform.system() == 'Windows':
		os.system('cls')
	else:
		os.system('clear')
		
# Utilisateur #

def changeuser():
	global user
	user = raw_input("[?] Bonjour, quel est votre nom ? >")
	printinfo("Bonjour " + user + " !")
	
def synctoserver(opts="q"):
	os.system("rsync -azh" + opts +  " --progress --delete-before "  + "./data/ " + sshlogin + "@" + sshserver + ":/" + sshrept + "/ ")
	
def syncfromserver(opts="q"):
	os.system("rsync -azh" + opts +  " --progress --delete-before " + sshlogin + "@" + sshserver + ":/" + sshrept + "/ " + "./data/")
# Casiers #

def addaction(sujet):
	
	lecture(sujet,False)
	time.sleep(2)
	clearscreen()
	try:
		columns = int(subprocess.check_output(['stty', 'size']).split()[1])
		printdebug("Nombre de colonnes : " + str(columns))
	except:
		printerror("Impossible de trouver le nombre de colones. Setting a 80.")
		columns = 80
		
	print "".center(columns, menuchar)
	sys.stdout.write(ROUGE)
	sys.stdout.flush()
	print "Ajouter une action" .center(columns, menuchar)
	sys.stdout.write(GRAS)
	sys.stdout.flush()
	print "".center(columns, menuchar)
	print "Bans".center(columns, menuchar)
	sys.stdout.write(NORMAL)
	sys.stdout.flush()
	print " 11. Forcefield ".center(columns, menuchar)
	print " 12. Insultes ".center(columns, menuchar)
	print " 13. Fly ".center(columns, menuchar)
	print " 14. Cheats divers ".center(columns, menuchar)
	print " 15. Demande de give ".center(columns, menuchar)
	print "".center(columns, menuchar)
	sys.stdout.write(GRAS)
	sys.stdout.flush()
	print "Tempbans".center(columns, menuchar)
	sys.stdout.write(NORMAL)
	sys.stdout.flush()
	print " 21. Insultes ".center(columns, menuchar)
	print " 22. Cheat supposé ".center(columns, menuchar)
	print " 23. Refus de vérification ".center(columns, menuchar)
	print " 24. Spam ".center(columns, menuchar)
	print "".center(columns, menuchar)
	sys.stdout.write(GRAS)
	sys.stdout.flush()
	print " Mutes ".center(columns, menuchar)
	sys.stdout.write(NORMAL)
	sys.stdout.flush()
	print " 31. Insultes ".center(columns, menuchar)
	print " 32. Spam ".center(columns, menuchar)
	print " 33. Demande de give ".center(columns, menuchar)
	print "".center(columns, menuchar)
	sys.stdout.write(GRAS)
	sys.stdout.flush()
	print " Autres ".center(columns, menuchar)
	sys.stdout.write(NORMAL)
	sys.stdout.flush()
	print " 0. Autre raison/action ".center(columns, menuchar)
	
	choix = raw_input("[?] Quel est votre choix ? >")
	
	choix = int(choix)
	if choix is 11:
		addtofile(sujet,time.strftime('%d/%m/%y %H:%M',time.localtime()) + " $> " + "Ban pour forcefield" + " (" + user + ") "+ "\n")
	elif choix is 12:
		addtofile(sujet,time.strftime('%d/%m/%y %H:%M',time.localtime()) + " $> " + "Ban pour Insultes" + " (" + user + ") "+ "\n")
	elif choix is 13:
		addtofile(sujet,time.strftime('%d/%m/%y %H:%M',time.localtime()) + " $> " + "Ban pour fly" + " (" + user + ") "+ "\n")
	elif choix is 14:
		addtofile(sujet,time.strftime('%d/%m/%y %H:%M',time.localtime()) + " $> " + "Ban pour cheat" + " (" + user + ") "+ "\n")
	elif choix is 14:
		addtofile(sujet,time.strftime('%d/%m/%y %H:%M',time.localtime()) + " $> " + "Ban pour demande de give" + " (" + user + ") "+ "\n")
	elif choix is 21:
		temps = raw_input("[?] Cette action dure combien de temps ? >")
		addtofile(sujet,time.strftime('%d/%m/%y %H:%M',time.localtime()) + " $> " + "Tempban " + temps + " pour Insultes" + " (" + user + ") "+ "\n")
	elif choix is 22:
		temps = raw_input("[?] Cette action dure combien de temps ? >")
		addtofile(sujet,time.strftime('%d/%m/%y %H:%M',time.localtime()) + " $> " + "Tempban " + temps + " pour Cheat supposé" + " (" + user + ") "+ "\n")
	elif choix is 23:
		temps = raw_input("[?] Cette action dure combien de temps ? >")
		addtofile(sujet,time.strftime('%d/%m/%y %H:%M',time.localtime()) + " $> " + "Tempban " + temps + " pour refus de vérification" + " (" + user + ") "+ "\n")
	elif choix is 24:
		temps = raw_input("[?] Cette action dure combien de temps ? >")
		addtofile(sujet,time.strftime('%d/%m/%y %H:%M',time.localtime()) + " $> " + "Tempban " + temps + " pour spam" + " (" + user + ") "+ "\n")
	elif choix is 31:
		temps = raw_input("[?] Cette action dure combien de temps ? >")
		addtofile(sujet,time.strftime('%d/%m/%y %H:%M',time.localtime()) + " $> " + "Mute " + temps + " pour Insultes" + " (" + user + ") "+ "\n")
	elif choix is 32:
		temps = raw_input("[?] Cette action dure combien de temps ? >")
		addtofile(sujet,time.strftime('%d/%m/%y %H:%M',time.localtime()) + " $> " + "Mute " + temps + " pour spam" + " (" + user + ") "+ "\n")
	elif choix is 33:
		temps = raw_input("[?] Cette action dure combien de temps ? >")
		addtofile(sujet,time.strftime('%d/%m/%y %H:%M',time.localtime()) + " $> " + "Mute " + temps + " pour demande de give" + " (" + user + ") "+ "\n")
	elif choix == 0:
		message = raw_input("[?] Quelle est l'action a inscrire dans le casier de " + sujet + " ? >")
		addtofile(sujet,time.strftime('%d/%m/%y %H:%M',time.localtime()) + " $> " + message + "(" + user + ")"+ "\n")
	else:
		printerror("Je n'ai pas compris. Retour au menu")
		return
	printok("Action ajoutée !")
	
	
def addcomm(sujet):
	
	lecture(sujet,False)
	time.sleep(2)
	clearscreen()
	try:
		columns = int(subprocess.check_output(['stty', 'size']).split()[1])
		printdebug("Nombre de colonnes : " + str(columns))
	except:
		printerror("Impossible de trouver le nombre de colones. Setting a 80.")
		columns = 80

	print "".center(columns, menuchar)
	sys.stdout.write(ROUGE)
	sys.stdout.flush()
	print "Ajouter un commentaire" .center(columns, menuchar)
	sys.stdout.write(GRAS)
	sys.stdout.flush()
	print "".center(columns, menuchar)
	print "Positifs".center(columns, menuchar)
	sys.stdout.write(NORMAL)
	sys.stdout.flush()
	print " 11. Serviable ".center(columns, menuchar)
	print " 12. Aide ".center(columns, menuchar)
	print " 13. Dénonce ".center(columns, menuchar)
	print " 14. Vérification négative ".center(columns, menuchar)
	print "".center(columns, menuchar)
	sys.stdout.write(GRAS)
	sys.stdout.flush()
	print "Negatifs".center(columns, menuchar)
	sys.stdout.write(NORMAL)
	sys.stdout.flush()
	print " 21. Insultes ".center(columns, menuchar)
	print " 22. Cheat supposé ".center(columns, menuchar)
	print " 23. Refus de vérification ".center(columns, menuchar)
	print " 24. Verification positive ".center(columns, menuchar)
	print " 25. Spam".center(columns, menuchar)
	print " 26. Demande de give".center(columns, menuchar)
	print "".center(columns, menuchar)

	sys.stdout.write(GRAS)
	sys.stdout.flush()
	print "Autres".center(columns, menuchar)
	sys.stdout.write(NORMAL)
	sys.stdout.flush()
	print " 0. Autre raison/commentaire ".center(columns, menuchar)
	
	choix = raw_input("[?] Quel est votre choix ? >")
	
	choix = int(choix)
	if choix is 11:
		addtofile(sujet,time.strftime('%d/%m/%y %H:%M',time.localtime()) + " #> " + "Cette personne est serviable" + " (" + user + ") "+ "\n")
	elif choix is 12:
		addtofile(sujet,time.strftime('%d/%m/%y %H:%M',time.localtime()) + " #> " + "Cette personne m'as aidée" + " (" + user + ") "+ "\n")
	elif choix is 13:
		nom = raw_input("[?] Qui as t'elle dénoncé ? >")
		raison = raw_input("[?] Et pourquoi ? >")
		addtofile(sujet,time.strftime('%d/%m/%y %H:%M',time.localtime()) + " #> " + "Cette personne as dénoncé " + nom + " pour " + raison + " (" + user + ") "+ "\n")
	elif choix is 14:
		addtofile(sujet,time.strftime('%d/%m/%y %H:%M',time.localtime()) + " #> " + "Cette personne n'avais pas de cheat actif lors de la vérification." + " (" + user + ") "+ "\n")
	elif choix is 21:
		addtofile(sujet,time.strftime('%d/%m/%y %H:%M',time.localtime()) + " #> " + "Cette personne en insulte d'autres..." + " (" + user + ") "+ "\n")
	elif choix is 22:
		addtofile(sujet,time.strftime('%d/%m/%y %H:%M',time.localtime()) + " #> " + "Cette personne triche peut etre." + " (" + user + ") "+ "\n")
	elif choix is 23:
		addtofile(sujet,time.strftime('%d/%m/%y %H:%M',time.localtime()) + " #> " + "Cette personne as refusé ma vérification, ou s'est déconéctée avant." + " (" + user + ") "+ "\n")
	elif choix is 24:
		addtofile(sujet,time.strftime('%d/%m/%y %H:%M',time.localtime()) + " #> " + "La verification est positive sur cette personne." + " (" + user + ") "+ "\n")
	elif choix is 25:
		addtofile(sujet,time.strftime('%d/%m/%y %H:%M',time.localtime()) + " #> " + "Cette personne spamme." + " (" + user + ") "+ "\n")
	elif choix is 26:
		addtofile(sujet,time.strftime('%d/%m/%y %H:%M',time.localtime()) + " #> " + "Cette personne demande du give." + " (" + user + ") "+ "\n")
	elif choix == 0:
		message = raw_input("[?] Quel est le commentaire a inscrire dans le casier de " + sujet + " ? >")
		addtofile(sujet,time.strftime('%d/%m/%y %H:%M',time.localtime()) + " $> " + message + "(" + user + ")"+ "\n")
	else:
		printerror("Je n'ai pas compris. Retour au menu")
		return
	printok("Commentaire ajouté !")
	
def addproof():
	url = raw_input("[?] Veuillez entrer l'url >")
	nom = raw_input("[?] Veuillez entrer le nom du fichier >")
	sujet = raw_input("[?] Veuillez entrer le nom de la personne >")
	syncfromserver("q")
	if not os.path.exists("./data/" + sujet + "/"):
		os.makedirs("./data/" + sujet + "/")	
	path = "./data/" + sujet + "/" + nom 
	if os.path.exists(path):
		printerror("Le fichier existe déja... Annulation ! ")
		return False
	printinfo("Téléchargement du fichier")	
	download(url,path)
	addtofile(sujet,time.strftime('%d/%m/%y %H:%M',time.localtime()) + " $> ajout d'une preuve : " + nom + " (" + user + ")"+ "\n")
	printinfo("Synchronisation avec le serveur")
	synctoserver("q")
	printok("Preuve telechargee et ajoutee")
	
	
# Fichiers #

def addtofile(sujet,phrase):
	if not os.path.exists("./data/" + sujet + "/"):
	    os.makedirs("./data/" + sujet + "/")
	fichier = open("./data/" + sujet + "/db.txt","a")
	fichier.write(phrase)
	fichier.close()
	synctoserver("q")

def lecture(sujet,signaler): # signaler [True/False], indique si il n'y a pas de casier
	try :
		syncfromserver("q")
		fichier = open("./data/" + sujet + "/db.txt","r")
		printinfo(ROUGE + sujet + NORMAL + " as déjà un casier... Affichage !")
		print ""
		for ligne in fichier:
			printinfo(ligne)
		fichier.close()
	except IOError:
		if signaler == True:
			printerror("Pas de casier pour " + sujet)
		pass
			
def download(url,nom):
	# url = "http://download.thinkbroadband.com/10MB.zip"

	opener = urllib2.build_opener()
	opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36')]
	response = opener.open(url)
	htmlData = response.read()
	f = open(nom,'w')
	f.write(htmlData)
	f.close()
# Main #

	
def mainmenu():
	try:
		columns = int(subprocess.check_output(['stty', 'size']).split()[1])
		printdebug("Nombre de colonnes : " + str(columns))
	except:
		printerror("Impossible de trouver le nombre de colones. Setting a 80.")
		columns = 80
		
	print "".center(columns, menuchar)
	sys.stdout.write(ROUGE)
	sys.stdout.flush()
	print "Menu Principal" .center(columns, menuchar)
	sys.stdout.write(GRAS)
	sys.stdout.flush()
	print "".center(columns, menuchar)
	print " Casiers Existants ".center(columns, menuchar)
	sys.stdout.write(NORMAL)
	sys.stdout.flush()
	print " 1. Lire le casier d'une personne ".center(columns, menuchar)
	print "".center(columns, menuchar)
	sys.stdout.write(GRAS)
	sys.stdout.flush()
	print " Creer/ Ajout aux Casiers ".center(columns, menuchar)
	sys.stdout.write(NORMAL)
	sys.stdout.flush()
	print " 2. Ajouter une action ".center(columns, menuchar)
	print " 3. Ajouter un commentaire ".center(columns, menuchar)
	print "".center(columns, menuchar)
	sys.stdout.write(GRAS)
	sys.stdout.flush()
	print " Autres méthodes ".center(columns, menuchar)
	sys.stdout.write(NORMAL)
	sys.stdout.flush()
	print " 4. Télécharger un fichier / ajout d'une preuve".center(columns, menuchar)
	print " 5. Changer d'utilisateur ".center(columns, menuchar)
	print " 6. Sync avec le serveur".center(columns, menuchar)
	if debugactivated == True:
		print "".center(columns, menuchar)
		sys.stdout.write(GRAS)
		sys.stdout.flush()
		print " Devloppeur ".center(columns, menuchar)
		sys.stdout.write(NORMAL)
		sys.stdout.flush()
		print " 7. Reload Menu".center(columns, menuchar)
		
	print "".center(columns, menuchar)
	sys.stdout.write(ROUGE)
	sys.stdout.flush()
	print " 0. Quitter ".center(columns, menuchar)
	
	sys.stdout.write(NORMAL)
	sys.stdout.flush()
	print "".center(columns, menuchar)
	
def main():

	if clearscreenbeforeopeningmenu == True:
		clearscreen()
	mainmenu()		
	choix = raw_input("[?] Que souhaitez vous faire ? >")
	try:
		choix = int(choix)
	except:
		printerror("Humm ... Entrée incomphréncible")
		
		return
	if choix is 1:
		sujet = raw_input("[?] Quelle est la personne dont vous voulez voir le casier ? >")
		lecture(sujet.lower(),True)
	elif choix is 2:
		sujet = raw_input("[?] Quelle est la personne a qui vous souhaitez ajouter une action ? >")
		addaction(sujet.lower())
	elif choix is 3:
		sujet = raw_input("[?] Quelle est la personne a qui vous souhaitez ajouter un commentaire ? >")
		addcomm(sujet.lower())
	elif choix == 4:
		addproof()
	elif choix is 5:
		changeuser()
	elif choix == 6:
		choix = raw_input("[?] Que souhaitez vous faire : 1 pour recevoir les données et 2 pour les envoyer >")
		try:
			choix = int(choix)
		except:
			printerror("Humm ... Entrée incomphréncible")
			return
		if choix is 1:
			printinfo("Réception des données.")
	 		syncfromserver("vv")
			printok("Toutes les donnés du serveurs ont été recues")
		elif choix is 2:
			printinfo("Envoi des données.")
			synctoserver("vv")
			printok("Toutes vos donnés ont été envoyées")
		printok("Vous etes synronisé avec le serveur !")
	elif choix == 7:
		pass
	elif choix == 0:
		printinfo("Envoi des données.")
		synctoserver("vv")
		clearscreen()
		printok("Au revoir !")
		sys.exit(0)
	else:
		printerror("Humm ... Entrée incomphréncible")
		



print "------[LANCEMENT!]------"

#### Starting ####
printinfo("Téléchangement des dernieres données si disponibles.")
syncfromserver("vv")
clearscreen()
#changeuser()
while True:
	main()
	time.sleep(5)

	
	
