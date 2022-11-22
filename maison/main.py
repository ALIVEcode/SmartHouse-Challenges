from time import sleep
from aliot.aliot_obj import AliotObj
from smarthouse.core.maison import Maison
from alimata.sensors.motion import Motion

maison_iot = AliotObj("maison")
maison = Maison()


# Fonctions de retour (callback)
def mouvement_salle_de_bain(etat):
    if etat:
        print("mouvement salle bain")
        maison.salle_de_bain.lumiere.allumer()
    else:
        maison.salle_de_bain.lumiere.eteindre()



def mouvement_salon(etat):
    if etat:
        print("mouvement salon")
        maison.salon.lumiere.allumer()
    else:
        maison.salon.lumiere.eteindre()

def mouvement_chambre(etat):
    if etat:
        print("mouvement chambre")
        maison.chambre.lumiere.allumer()
    else:
        maison.chambre.lumiere.eteindre()
# def mouvement_cuisine():
#     print("mouvement cuisine")
#     pass

def sonner_sonnette(etat):
    if etat:
        print("sonner")
        maison.porte_entre.ouvrir()
        maison.sonnette_entre.sonner()

    else:
        maison.porte_entre.fermer()

def setup():

    maison.salle_de_bain.sur_mouvement(mouvement_salle_de_bain)
    maison.salon.sur_mouvement(mouvement_salon)
    maison.chambre.sur_mouvement(mouvement_chambre)
    maison.sonnette_entre.sur_clic(sonner_sonnette)
    # maison.cuisine.sur_mouvement(mouvement_cuisine)


def loop():
    print("Hum : " + str(maison.salle_de_bain.capteur_dht.humidite))
    print("Temp : " + str(maison.salle_de_bain.capteur_dht.temperature))
    maison.lcd.afficher(
        "Humidite : " + str(maison.salle_de_bain.capteur_dht.humidite), 
        "Temperature : " + str(maison.salle_de_bain.capteur_dht.temperature),
        "",
        "")

    if maison.salle_de_bain.capteur_dht.humidite >= 50:
        maison.son.sonner()
    else:
        maison.son.stop()
    sleep(0.5)

    
def start_maison():
    maison.start(setup, loop)
    
maison_iot.on_start(callback=start_maison)
maison_iot.run()