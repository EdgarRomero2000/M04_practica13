#Declaracio de la clase
class vehicle:

    # Declaracio del constructor
    def __init__(self,portes,marca,preu,seients,pes,rodes):
        self.portes = portes
        self.marca = marca
        self.preu = preu
        self.seients = seients
        self.pes = pes
        self.rodes = rodes

    #Declaracio dels getters i setters
    def getPortes(self):
        return self.portes

    def setPortes(self,portes):
        self.portes = portes

    def getMarca(self):
        return self.marca

    def setMarca(self,marca):
        self.marca = marca

    def getPreu(self):
        return self.preu

    def setPreu(self,preu):
        self.preu = preu

    def getSeients(self):
        return self.seients

    def setSeients(self,seients):
        self.seients = seients

    def getPes(self):
        return self.pes

    def setPes(self,pes):
        self.pes = pes

    def getRodes(self):
        return self.rodes

    def setRodes(self,rodes):
        self.rodes = rodes

    #Declaracio del metode salutacio que imprimeix tots els atributs
    def salutacio(self):
        print(f" Portes: {self.portes}\n Marca: {self.marca} \n Preu: {self.preu} "
              f"\n Seients: {self.seients} \n Pes: {self.pes}T \n Rodes: {self.rodes}\n")

