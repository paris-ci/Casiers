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

#FONCTIONS

def fdebug(message) :
	global debug
	if "d" in debug :
		print (JAUNE + "DEBUG : " + message)
#MAIN

debug = raw_input (VERT + "Tape 0 pour lancer le programme")
fdebug("init terminée")
nom = raw_input (VERT + "Bonjour ! Entre ton nom !")
fdebug("""Nom enregistré dans la variable "Nom" """)

print(VERT + "Bonjour " + nom)

#TODO
#PROGRAMME
