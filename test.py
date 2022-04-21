# Projet "robotique" IA&Jeux 2021
#
# Binome:
#  Prénom Nom: Marwan TRAGHA
#  Prénom Nom: Koceila KEMICHE

"""
Stratégie : 
On se déplace de façon à remplir le maximum de surface. 
Quand on rencontre un robot adverse on le suit de façon à peindre juste derrière lui.
Si on croise un chemin on rentre dedans.
"""

import random

def get_team_name():
    return "Picasso" 

def step(robotId, sensors):

	translation = 1
	rotation = 0

	# Si un ennemi est derrière on se bloque 

	if sensors["sensor_back"]["isRobot"] ==  True and sensors["sensor_back"]["isSameTeam"] == False : 
		rotation = -1

	# Si on croise un allié proche on le fuit
	"""
	Pour fuir un allié on choisit une rotation aléatoire, ainsi on limite les comportements pré-définis ce qui nous permet de na pas avoir de "tendance de déplacements" et de couvrir un maximum de surface.
	"""
	if sensors["sensor_front"]["isRobot"] == True and sensors["sensor_front"]["isSameTeam"] == True: # Si un allié est devant
		rotation = random.uniform(-1,1)
		return translation, rotation	

	if sensors["sensor_front_left"]["isRobot"] == True and sensors["sensor_front_left"]["isSameTeam"] == True: # Si un allié est devant à gauche
		rotation = random.uniform(-1,1)
		return translation, rotation
	
	if sensors["sensor_front_right"]["isRobot"] == True and sensors["sensor_front_right"]["isSameTeam"] == True: # Si un allié est devant à droite
		rotation = random.uniform(-1,1)
		return translation, rotation

	if sensors["sensor_left"]["isRobot"] == True and sensors["sensor_left"]["isSameTeam"] == True: # Si un allié est à gauche
		rotation = random.uniform(-1,1)
		return translation, rotation

	if sensors["sensor_right"]["isRobot"] == True and sensors["sensor_right"]["isSameTeam"] == True: # Si un allié est à droite
		rotation = random.uniform(-1,1)
		return translation, rotation
	
	
	# Si on croise un ennemi proche on le suit 

	if sensors["sensor_front"]["isRobot"] == True: # Si un ennemi est devant
		return translation, rotation

	if sensors["sensor_front_left"]["isRobot"] == True: # Si un ennemi est devant à gauche
		rotation = -0.5
		return translation, rotation
	
	if sensors["sensor_front_right"]["isRobot"] == True: # Si un ennemi est devant à droite
		rotation = 0.5
		return translation, rotation 

	if sensors["sensor_left"]["isRobot"] == True: # Si un ennemi est à gauche
		rotation = -1
		return translation, rotation

	if sensors["sensor_right"]["isRobot"] == True: # Si un ennemi est à droite
		rotation = 1
		return translation, rotation

	#  On essaie de rentrer sur des chemins libres 

	if isWallLeft(sensors) and sensors["sensor_front_left"]["distance"] == 1: # Chemin à gauche
		# Si un chemin est à gauche, on a 90% de chance de l'emprunter, sinon on se retourne aléatoirement. Cela nous permet de ne pas boucler le long des murs.

		if random.random() < 0.9 : 
			rotation = -0.3
		else : 
			rotation = random.uniform(0,1)

		return translation, rotation

	if isWallRight(sensors) and sensors["sensor_front_right"]["distance"] == 1: # Chemin à droite	

		if random.random() < 0.9 : 
			rotation = 0.3
		else : 
			rotation = random.uniform(-1,0)

		return translation, rotation

	# Si on est bloqué au mur on tourne 

	if sensors["sensor_front"]["distance"] < 0.2 or sensors["sensor_front_left"]["distance"] < 0.2 or sensors["sensor_front_right"]["distance"] < 0.2 :
		if sensors["sensor_front_left"]["distance"] < sensors["sensor_front_right"]["distance"] : # Bloqué à  gauche
			rotation = 1  

		else: # Bloqué à droite
			rotation = -1  

		return translation , rotation 

	# Sinon on évite, comportement de Braitenberg

	translation = 1 * sensors["sensor_front"]["distance"]
	rotation = (-1) * sensors["sensor_front_left"]["distance"] + (1) * sensors["sensor_front_right"]["distance"] + (-1) * sensors["sensor_left"]["distance"] + sensors["sensor_right"]["distance"]
	translation = max(-1,min(translation,1))
	rotation = max(-1, min(rotation, 1))

	return translation, rotation

def isWallRight(sensors):
	"""
	Renvoie True si un mur est à droite, False sinon
	"""
	return sensors["sensor_right"]["isRobot"] == False and sensors["sensor_right"]["distance"] != 1 

def isWallLeft(sensors):
	"""
	Renvoie True si un mur est à gauche, False sinon
	"""
	return sensors["sensor_left"]["isRobot"] == False and sensors["sensor_left"]["distance"] != 1 