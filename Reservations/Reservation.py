from datetime import datetime
from Passager import *

numReservation=0
class Reservation:
    
    def __init__(self, vol, passager):
        self._date=datetime.now()
        self._etatReservation="ouverte"
        self._vol=vol
        self._passager=passager
        global numReservation
        numReservation+=1
        self._id=numReservation
        
    def annuler(self):
        self._etatReservation="fermee"
        
    def confirmer(self):
        self._etatReservation="confirmee"
        
    def _get_etat(self):
        return self._etatReservation
        
    def _get_numero(self):
        return _id
        
    def __str__(self):
        print("RESERVATION ", self._id,":",
        "\nPassager : ",self._passager._get_prenom()," ",self._passager._get_nom(),
        "\nDate reservation : ",self._date.day,"/",self._date.month,"/",self._date.year,
        "\nEtat : ",self._etatReservation,
        "\nVol : ", self._vol,
        "\n**********")
    