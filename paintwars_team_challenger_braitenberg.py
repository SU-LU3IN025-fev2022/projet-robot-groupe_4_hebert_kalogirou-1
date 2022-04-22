# Projet "robotique" IA&Jeux 2021
#
# Binome:
#  Prénom Nom: Thomas Hebert
#  Prénom Nom: Vasiliki Eirini Kalogirou

from pyroborobo import Pyroborobo, Controller, AgentObserver, WorldObserver, CircleObject, SquareObject, MovableObject
# from custom.controllers import SimpleController, HungryController
import numpy as np
import random

import paintwars_arena

def get_team_name():
    return "[ Midnight Suns ]" # à compléter (comme vous voulez)

def get_extended_sensors(sensors):
    for key in sensors:
        sensors[key]["distance_to_robot"] = 1.0
        sensors[key]["distance_to_wall"] = 1.0
        if sensors[key]["isRobot"] == True:
            sensors[key]["distance_to_robot"] = sensors[key]["distance"]
        else:
            sensors[key]["distance_to_wall"] = sensors[key]["distance"]
    return sensors

def step(robotId, sensors):

    translation = 1 # vitesse de translation (entre -1 et +1)
    rotation = 0 # vitesse de rotation (entre -1 et +1)

    sensors = get_extended_sensors(sensors)

    """
    if sensors["sensor_front_left"]["distance"] < 1 or sensors["sensor_front"]["distance"] < 1:
        rotation = 0.5  # rotation vers la droite
    elif sensors["sensor_front_right"]["distance"] < 1:
        rotation = -0.5  # rotation vers la gauche

    if sensors["sensor_front"]["isRobot"] == True and sensors["sensor_front"]["isSameTeam"] == False:
        enemy_detected_by_front_sensor = True # exemple de détection d'un robot de l'équipe adversaire (ne sert à rien)
    """

    print("LEFT SIDE :", sensors["sensor_front_left"]["distance_to_wall"])
    print("RIGHT SIDE :", sensors["sensor_front_right"]["distance_to_wall"])
    translation = 1 * sensors["sensor_front"]["distance"]
    rotation = (-1) * sensors["sensor_front_left"]["distance_to_robot"] + (1) * sensors["sensor_front_right"]["distance_to_robot"] + (-1) * sensors["sensor_front_left"]["distance_to_wall"] + (1) * sensors["sensor_front_right"]["distance_to_wall"] + (-1) * sensors["sensor_back_left"]["distance_to_robot"] + (1) * sensors["sensor_back_right"]["distance_to_robot"] + (-1) * sensors["sensor_back_left"]["distance_to_wall"] + (1) * sensors["sensor_back_right"]["distance_to_wall"] + (-1) * sensors["sensor_left"]["distance_to_robot"] + 1 * sensors["sensor_right"]["distance_to_robot"] + (-1) * sensors["sensor_left"]["distance_to_wall"] + 1 * sensors["sensor_right"]["distance_to_wall"] + 1 * sensors["sensor_front"]["distance_to_wall"] - 1 * sensors["sensor_back"]["distance_to_wall"] + 1 * sensors["sensor_front"]["distance_to_robot"] - 1 * sensors["sensor_back"]["distance_to_robot"]
    print("ROTATION =", rotation)

    # limite les valeurs de sortie entre -1 et +1
    translation = max(-1,min(translation,1))
    rotation = max(-1, min(rotation, 1))


    return translation, rotation
