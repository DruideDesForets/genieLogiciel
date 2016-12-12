numPassager=0
class Passager:
    
    def __init__(self, nom, prenom):
        self._nom=nom
        self._prenom=prenom
        global numPassager
        numPassager+=1
        self._id=numPassager
    def _get_nom(self):
        return self._nom
        
    def _get_prenom(self):
        return self._prenom
        
    def __str__(self):
        print("PASSAGER ", self._id, " : \nPrenom : ",self._prenom,"\nNom : ", self._nom,"\n**********")