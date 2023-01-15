from alimata.core.board import Board

"""
Ce programme représente la structure de base nécessaire au fonctionnement d'un programme arduino.
DÉFI : Afficher "Hello World!" une seule fois à la connection du board. 
"""

board = Board()

def setup():
    # print("Hello world!")
    pass

def loop():
    pass

board.start(setup, loop)