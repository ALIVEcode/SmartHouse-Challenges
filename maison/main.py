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

def sonner_et_ouvrir(etat: bool):
    if etat:
        print("sonner")
        maison.porte_entree.ouvrir()
        maison.sonnette_entre.sonner()

    else:
        maison.porte_entree.fermer()

def setup():

    maison.salle_de_bain.sur_mouvement(mouvement_salle_de_bain)
    maison.salon.sur_mouvement(mouvement_salon)
    maison.chambre.sur_mouvement(mouvement_chambre)
    maison.sonnette_entre.sur_clic(sonner_et_ouvrir)

    # maison.cuisine.sur_mouvement(mouvement_cuisine)

deactivate_lcd = False

def loop():
    humidite = maison.salle_de_bain.capteur_dht.humidite
    temperature = maison.salle_de_bain.capteur_dht.temperature

    print("Hum : " + str(humidite))
    print("Temp : " + str(temperature))
    if not deactivate_lcd:
        maison.lcd.afficher(
            "Humidite : " + str(humidite), 
            "Temperature : " + str(temperature)
        )
    maison_iot.update_doc(maison.as_doc())

    if maison.salle_de_bain.capteur_dht.humidite >= 50:
        maison.son.sonner()
    else:
        maison.son.stop()
    sleep(1)

    
def start_maison():
    maison.start(setup, loop)

def ouvrir_porte_aliot(data):
    sonner_et_ouvrir(True)
    sleep(1)
    sonner_et_ouvrir(False)

def ecrire_lcd_aliot(data):
    global deactivate_lcd
    deactivate_lcd = True
    lines = ["", ""]
    if "lignes" in data:
        lines = data["lignes"]
    elif "lines" in data:
        lines = data["lines"]

    maison.lcd.effacer()
    maison.lcd.afficher(lines[0], lines[1])
    sleep(3)
    maison.lcd.effacer()
    deactivate_lcd = False

def allumer_lumiere_aliot(data):
    if "salon" in data:
        maison.salon.lumiere.allumer()
    if "salle_de_bain" in data:
        maison.salle_de_bain.lumiere.allumer()
    if "chambre" in data:
        maison.chambre.lumiere.allumer()
    if "cuisine" in data:
        maison.cuisine.lumiere.allumer()

def eteindre_lumiere_aliot(data):
    if "salon" in data:
        maison.salon.lumiere.eteindre()
    if "salle_de_bain" in data:
        maison.salle_de_bain.lumiere.eteindre()
    if "chambre" in data:
        maison.chambre.lumiere.eteindre()
    if "cuisine" in data:
        maison.cuisine.lumiere.eteindre()
     
maison_iot.on_start(callback=start_maison)
maison_iot.on_action_recv(action_id="ouvrir_porte", callback=ouvrir_porte_aliot)
maison_iot.on_action_recv(action_id="ecrire_lcd", callback=ecrire_lcd_aliot)
maison_iot.on_action_recv(action_id="allumer_lumiere", callback=allumer_lumiere_aliot)
maison_iot.on_action_recv(action_id="eteindre_lumiere", callback=eteindre_lumiere_aliot)
maison_iot.run()