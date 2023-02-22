#declarem la classe amb les seves definicions
class user:
    # definim els atributs i fem el getter i el setter de cadascu
    def __init__(self, nom, cognom, alias, id, genere, naixement):
        self.nom = nom
        self.cognom = cognom
        self.alias = alias
        self.id = id
        self.genere = genere
        self.naixement = naixement

    def getNom(self):
        return self.nom

    def setNom(self, nom):
        self.nom = nom

    def getCognom(self):
        return self.cognom

    def setCognom(self, cognom):
        self.cognom = cognom

    def getAlias(self):
        return self.alias

    def setAlias(self, alias):
        self.alias = alias

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getGenere(self):
        return self.genere

    def setGenere(self, genere):
        self.genere = genere

    def getNaixement(self):
        return self.naixement

    def setNaixement(self, naixement):
        self.naixement = naixement

    def salutacio (self):
        # fem el print de cada definicio
        print("El nom es: " + self.nom)
        print("El cognom es: " + self.cognom)
        print("L'alias es: " + self.alias)
        print("L'id es: " + self.id)
        print("El genere es: " + self.genere)
        print("La data de naixement es: " + self.naixement)