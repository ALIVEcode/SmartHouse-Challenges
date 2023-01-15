from alimata.core.board import Board

"""
MODULE 1
--------
EXERCICE #0 - INTRODUCTION
--------
Ce programme représente la structure de base nécessaire au fonctionnement d'un programme Arduino.
Prenez le temps de lire le code et de comprendre le rôle de chaque partie.

CONSIGNES : Afficher "Hello World!" une seule fois dans la console lors de la connection du board.
"""

#---------------------------------------------
# ÉTAPE 1 : Initialiser les composantes électroniques
#---------------------------------------------
"""
Le board fait référence à la carte électronique Arduino. Le board doit être initialisé au début de chaque programme 
avec la fonction Board(). Cela permet d'établir la communication entre le programme et l'Arduino connecté à votre ordinateur.
"""
board = Board()

#---------------------------------------------
# ÉTAPE 2 : Compléter le corps du programme
#---------------------------------------------
"""
Les fonctions suivantes contiennent les instructions qui seront envoyées au board.
"""
def setup():
    # Cette fonction est executée une seule fois au début du programme
    pass

def loop():
    # Cette fonction est executée à répétition au cours du programme
    pass
    
#---------------------------------------------
# ÉTAPE 3 : Démarrer le programme
#---------------------------------------------
"""
Pour démarrer le programme, nous avons besoin des 3 parties clé 
d'un programme Arduino : Le board, la fonction setup et la fonction loop. 
Les instructions définies dans les fonctions setup et loop seront lues par l'objet board.
"""
board.start(setup, loop)