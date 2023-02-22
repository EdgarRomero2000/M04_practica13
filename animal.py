#Declaracio de la clase
class animal:

    #Declaracio del constructor
    def __init__(self,familia,nomCientific,potes,vertebrat,reproducio,tamany):
        self.familia = familia
        self.nomCientific = nomCientific
        self.potes = potes
        self.vertebrat = vertebrat
        self.reproducio = reproducio
        self.tamany = tamany

    #Declaracio dels getters i setters
    def getFamilia(self):
        return self.familia

    def setFamilia(self,familia):
        self.familia = familia

    def getNomCientific(self):
        return self.nomCientific

    def setNomCientific(self,nomCientific):
        self.nomCientific = nomCientific

    def getPotes(self):
        return self.potes

    def setPotes(self,potes):
        self.potes = potes

    def getVertebrat(self):
        return self.vertebrat

    def setVertebrat(self,vertebrat):
        self.vertebrat = vertebrat

    def getReproducio(self):
        return self.reproducio

    def setReproducio(self,reproducio):
        self.reproducio = reproducio

    def getTamany(self):
        return self.tamany

    def setTamany(self,tamany):
        self.tamany = tamany

    #Declaracio del metode salutacio que imprimeix tots els atributs
    def salutacio(self):
        print(f" Familia: {self.familia} \n Nom Cientific: {self.nomCientific} \n Potes: {self.potes} "
              f"\n Vertebrat: {self.vertebrat} \n Reproducio: {self.reproducio} \n Tamany: {self.tamany}m\n")