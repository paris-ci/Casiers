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
		print (JAUNE + "DEBUG : " + message + NORMAL )
#MAIN

debug = raw_input (VERT + "Tape 0 pour lancer le programme >>>" + NORMAL)
fdebug("Initialisation")

fdebug("Demande du nom ")
nom = raw_input (VERT + "Bonjour ! Entre ton nom ! >>>" + NORMAL)
fdebug("""enregistrement du nom dans la variable "Nom" """)


print(VERT + "Bonjour " + nom + NORMAL)
fdebug("Demande du nom de la personne cible")
cible = raw_input ( VERT + "Quel est le nom de la personne cible ? >>>" + NORMAL )
fdebug ("""Enregistrement la cible dans la variable "cible". """)
fdebug (" Demande de la remarque ")
raison = raw_input (VERT + "Entre la remarque" + NORMAL)
fdebug ("""Enregistrement de la remarque dans la variable "raison". """)

#TODO
#PROGRAMME
