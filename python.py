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

def debug(message):
	if "d" in hidden :
		print(JAUNE + message)
#MAIN

hidden = input(VERT + "Tape 0 pour lancer le programme")
nom = input(VERT + "Bonjour ! Entre ton nom !")
print(VERT + "Bonjour " + nom)

#TODO
#PROGRAMME
#DEBUG
