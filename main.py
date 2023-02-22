from animal import animal
from vehicle import vehicle
from school import school

#Cridem l'objecte animal
Huma = animal("Mamiferos","Homo Sapiens Sapiens",2,True,"Sexual",1.7)
Huma.salutacio()
Kiwi = animal("Aves","Apterygidae Apteryx",2,True,"Sexual",0.35)
Kiwi.salutacio()
Huma.setTamany(2.0)
Huma.salutacio()
Kiwi.setReproducio("Asexual")
Kiwi.salutacio()

#Cridem l'objecte vehicle
McLaren = vehicle(2,"McLaren",100000,2,1.5,4)
McLaren.salutacio()
Renault = vehicle(4,"Renault",15000,5,3,4)
Renault.salutacio()
McLaren.setPreu(300000)
McLaren.salutacio()
Renault.setRodes(3)
Renault.setPortes(2)
Renault.setSeients(2)
Renault.salutacio()

#Cridem l'objecte school
Lestonnac = school("Bachillerat","Ciencies","Concertada",True,False,"Barcelona")
Lestonnac.salutacio()
Baguette = school("Secundaria","Sin especializacion","Publico",False,True,"Narvona")
Baguette.salutacio()
Lestonnac.setFinanciacio("Privat")
Lestonnac.salutacio()
Baguette.setExtraescolars(False)
Baguette.salutacio()