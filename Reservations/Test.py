from Reservation import *
from Client import *
from Passager import *






c1=Client("Lopezio","Antonio","1 rue de la Biche","06 25 21 63 54","22 05 25 52")
r1=c1.reserver(c1._get_nom(),c1._get_prenom(),"vol")

c2=Client("Déno","charlulilo","5 rue de la loutre","06 25 21 63 66","22 88 25 52")
r2=c2.reserver(c2._get_nom(),c2._get_prenom(),"vol")

print("\n\n")
c1.__str__()
r1.__str__()
print("\n\n")
c2.__str__()
r2.__str__()
print("\n\n")