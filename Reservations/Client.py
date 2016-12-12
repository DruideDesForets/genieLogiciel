from datetime import datetime
from Passager import *
from Reservation import *

numClient=0

class Client:
    

    def __init__(self,nom,prenom,adresse,numTel,numFax):
        self._nom=nom
        self._prenom=prenom
        self._adresse=adresse
        self._numTel=numTel
        self._numFax=numFax
        self._listReservations=[]
        global numClient
        numClient+=1
        self._id=numClient
        
    def _get_nom(self):
        return self._nom
        
    def _get_prenom(self):
        return self._prenom
        
    def reserver(self,nom, prenom, vol):
        p=Passager(nom, prenom)
        r=Reservation(vol, p)
        self._listReservations.append(r)
        return r
        
    def __str__(self):
        print("CLIENT ", self._id, " : \nPrenom : ",self._prenom,"\nNom : ", self._nom,"\nAdresse : ",self._adresse,"\nTelephone : ",self._numTel,"\nFax : ",self._numFax,"\n**********")
    