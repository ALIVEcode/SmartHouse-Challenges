from alimata.core.board import Board
from alimata.actuators.led import Led
from time import sleep

"""
DEFI : Convertir une séquence de caractères de code morse en un signal lumineux grâce à la LED.
Dans cet exercice, la séquence à convertir sera le signal SOS --> ...---...
Pour représenter un point, la lumière reste allumée pendant ? secondes.
Pour représenter un tiret, la lumière reste allumée pendant ? secondes.
"""
#------------------------------------------
# Initialiser les composantes électroniques
#------------------------------------------
board = Board()

led_pin = None # Configurer le pin
led = Led(board, led_pin)

#------------------------------------------
# Exemple : LED clignotante
#------------------------------------------
def led_exemple():
    led.on()    # Allumer la lumière
    sleep(1)    # Garder la lumière allumée pendant 1 seconde
    led.off()   # Éteindre la lumière
    sleep(1)    # Attendre 1 seconde avant de poursuivre

#------------------------------------------
# Compléter les fonctions suivantes 
#------------------------------------------

# Séquence à lire
SOS_CODE = '...---...'

def led_morse_dot():
    # Comportement de la LED pour représenter un point 
    pass

def led_morse_dash():
    # Comportement de la LED pour représenter un tiret
    pass

def lire_code(morse_code):
    # Traverser la séquence de caractères 
    # Et déterminer le comportement de la LED selon le caractère
    pass

#------------------------------------------
# Ajouter les bonnes fonctions à l'endroit approprié
#------------------------------------------
def setup():
    print("Starting challenge #1 ...")

def loop():
    # Appeler la fonction led_exemple() pour observer l'exemple
    # Ensuite, compléter le défi
    pass

board.start(setup, loop)