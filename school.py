#Declaracio de la clase
class school:

    # Declaracio del constructor
    def __init__(self, educacio, especialitat, financiacio, bilingue, extraescolars, ciutat):
        self.educacio = educacio
        self.especialitat = especialitat
        self.financiacio = financiacio
        self.bilingue = bilingue
        self.extraescolars = extraescolars
        self.ciutat = ciutat

    #Declaracio dels getters i setters
    def getEducacio(self):
        return self.educacio

    def setEducacio(self, educacio):
        self.educacio = educacio

    def getEspecialitat(self):
        return self.especialitat

    def setEspecialitat(self, especialitat):
        self.especialitat = especialitat

    def getFinanciacio(self):
        return self.financiacio

    def setFinanciacio(self, financiacio):
        self.financiacio = financiacio

    def getBilingue(self):
        return self.bilingue

    def setBilingue(self, bilingue):
        self.bilingue = bilingue

    def getExtraescolars(self):
        return self.extraescolars

    def setExtraescolars(self, extraescolars):
        self.extraescolars = extraescolars

    def getCiutat(self):
        return self.ciutat

    def setCiutat(self, ciutat):
        self.ciutat = ciutat

    #Declaracio del metode salutacio que imprimeix tots els atributs
    def salutacio(self):
        print(f" Educacio: {self.educacio}\n Especialitat: {self.especialitat} \n Financiacio: {self.financiacio} "
              f"\n Bilingue: {self.bilingue} \n Extraescolars: {self.extraescolars} \n Ciutat: {self.ciutat}\n")
