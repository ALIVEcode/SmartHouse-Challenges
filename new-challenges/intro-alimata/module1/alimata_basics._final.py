from alimata.core.board import Board
from alimata.actuators.led import Led
from time import sleep

"""
MODULE 1
--------
DÉFI FINAL
-------------------------------------------------------
CONSIGNES : Convertir une séquence de caractères de code morse en un signal lumineux grâce à la LED.
Dans cet exercice, la séquence à convertir sera le signal SOS --> ...---...
Pour représenter un point, garder la lumière allumée pendant 0.3 secondes.
Pour représenter un tiret, garder la lumière allumée pendant 0.8 secondes.

RAPPEL : Ne pas oublier de configurer le pin de la LED
"""
#------------------------------------------
# Initialiser les composantes électroniques
#------------------------------------------
board = Board()

led_pin = None
led = Led(board, led_pin)

#------------------------------------------
# DEFI : Compléter les fonctions suivantes 
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
    # Itérer chaque charactère dans la chaîne passée en paramètre (morse_code)
    # Et appeler la fonction appropriée selon le caractère lu (point ou tiret)
    pass

#------------------------------------------
# Compléter le corps du programme
#------------------------------------------
def setup():
    print("Starting final challenge ...")

def loop():
    # Faire appel à la bonne fonction
    pass

#------------------------------------------
# Démarrer le programme
#------------------------------------------
board.start(setup, loop)