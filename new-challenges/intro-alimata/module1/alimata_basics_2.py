from alimata.core.board import Board
from alimata.actuators.led import Led
from time import sleep

"""
MODULE 1
--------
EXERCICE #2 - LA FONCTION SLEEP
--------
CONSIGNES : Faire clignoter la LED. Les étapes à suivres ont été énoncées dans la fonction loop() afin de vous aider.
Utiliser la fonction sleep(float nbSecondes) pour attendre un certain nombre de secondes avant de poursuivre. 

RAPPEL : Ne pas oublier de configurer le pin de la LED
"""
#------------------------------------------
# Initialiser les composantes électroniques
#------------------------------------------
board = Board()

led_pin = None
led = Led(board, led_pin)

#------------------------------------------
# Compléter le corps du programme
#------------------------------------------
def setup():
    print("Starting challenge #2 ...")

def loop():
    # Allumer lumière
    # Attendre 1 seconde
    # Éteindre lumière
    # Attendre 1 seconde
    pass

#------------------------------------------
# Démarrer le programme
#------------------------------------------
board.start(setup, loop)




