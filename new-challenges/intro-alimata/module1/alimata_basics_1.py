from alimata.core.board import Board
from alimata.actuators.led import Led

"""
MODULE 1
--------
EXERCICE #1 - CONNECTER UNE LED 
--------
CONSIGNES : Attribuer la valeur appropriée pour la variable led_pin qui correspond à votre circuit.
Si la mauvaise valeur est attribuée à led_pin, la LED ne s'allumera pas.
"""

#------------------------------------------
# Initialiser les composantes électroniques
#------------------------------------------
board = Board()

#------------------------------------------
# NOUVEAU : Création d'un objet LED
#------------------------------------------
"""
Une LED est un actionneur (actuator) qui émet de la lumière. Pour actionner cet objet, il faut lui fournir de l'énergie
et des instructions par rapport à l'envoi de cette énergie. Cela s'effectue grâce au OUTPUT pin, que vous devrez identifier
selon votre circuit.
Lorsque la LED est ainsi connectée au board et que l'adresse du pin de sortie est définie,
il est possible de la contrôler à travers le programme.
"""
# Configurer le pin
led_pin = None

# Création d'un objet LED connecté au board et au pin identifié
led = Led(board, led_pin)

#------------------------------------------
# Corps du programme
#------------------------------------------
def setup():
    print("Starting challenge #1 ... ")

def loop():
    # La LED sera allumée tout au long de l'execution
    led.on()

#------------------------------------------
# Démarrer le programme
#------------------------------------------
board.start(setup, loop)
